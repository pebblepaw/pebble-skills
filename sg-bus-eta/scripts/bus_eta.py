#!/usr/bin/env python3
import json
import sys
import datetime
import urllib.request
import urllib.parse
import difflib
from pathlib import Path

BASE = "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival"
NEA_2HR = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
NEA_24HR = "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast"
SGT = datetime.timezone(datetime.timedelta(hours=8))


def load_json(p: Path):
    return json.loads(p.read_text())


def eta_minutes(iso: str | None):
    if not iso:
        return None
    try:
        t = datetime.datetime.fromisoformat(iso)
        if t.tzinfo is None:
            t = t.replace(tzinfo=SGT)
        now = datetime.datetime.now(SGT)
        return int((t - now).total_seconds() // 60)
    except Exception:
        return None


def urgency_icon(mins: int | None):
    if mins is None:
        return "❔"
    if mins <= 0:
        return "🔥"
    if mins <= 3:
        return "🔥"
    if mins <= 10:
        return "⏳"
    return "💤"


def forecast_to_emoji(text: str | None):
    t = (text or "").lower()
    if any(k in t for k in ["thunder", "t-storm"]):
        return "⛈️"
    if any(k in t for k in ["shower", "rain", "drizzle"]):
        return "🌧️"
    if "cloud" in t and "part" in t:
        return "🌤️"
    if "cloud" in t or "overcast" in t:
        return "☁️"
    if "haze" in t or "mist" in t or "fog" in t:
        return "🌫️"
    if "fair" in t or "sun" in t or "clear" in t:
        return "☀️"
    return "❔"


def fmt_window_compact(start_dt: datetime.datetime, end_dt: datetime.datetime):
    """Format like '4–6pm' if same am/pm, else '11am–1pm'."""

    def parts(dt: datetime.datetime):
        h = dt.hour
        ap = "am" if h < 12 else "pm"
        h12 = h % 12
        if h12 == 0:
            h12 = 12
        return h12, ap

    sh, sap = parts(start_dt)
    eh, eap = parts(end_dt)

    if sap == eap:
        return f"{sh}–{eh}{eap}"
    return f"{sh}{sap}–{eh}{eap}"


def is_rainy_text(text: str | None):
    t = (text or "").lower()
    return any(k in t for k in ["thunder", "shower", "rain", "drizzle"])


def is_thunder_text(text: str | None):
    t = (text or "").lower()
    return "thunder" in t


def summarize_weather_rest_of_day(area_names: list[str], until_hour: int = 21):
    """Summarize weather from now until 9pm using NEA 24-hour forecast periods.

    NEA 24-hour endpoint is regional (east/west/north/south/central).
    We map requested areas to a region.

    Returns dict area_name -> {emoji, windows[]}
    """

    # Hard mapping for our use-cases
    region_map = {
        "pasir ris": "east",
        "bishan": "central",
        "queenstown": "south",
    }

    now = datetime.datetime.now(SGT)
    end = now.replace(hour=until_hour, minute=0, second=0, microsecond=0)
    if end < now:
        end = now

    req = urllib.request.Request(NEA_24HR, headers={"accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as res:
        data = json.load(res)

    items = data.get("items") or []
    if not items:
        return {a: {"emoji": "❔", "windows": []} for a in area_names}

    periods = items[0].get("periods") or []

    # Build per-area tracking
    rainy_windows = {a: [] for a in area_names}
    saw_thunder = {a: False for a in area_names}
    last_emoji = {a: "❔" for a in area_names}

    for p in periods:
        t = p.get("time") or {}
        try:
            sdt = datetime.datetime.fromisoformat(t.get("start")).astimezone(SGT)
            edt = datetime.datetime.fromisoformat(t.get("end")).astimezone(SGT)
        except Exception:
            continue

        # Skip periods fully outside window
        if edt <= now or sdt >= end:
            continue

        # Clip window to now..end for display
        clip_s = max(sdt, now)
        clip_e = min(edt, end)
        window_str = fmt_window_compact(clip_s, clip_e)

        regions = p.get("regions") or {}

        for a in area_names:
            region = region_map.get(a.strip().lower())
            txt = regions.get(region) if region else None
            emo = forecast_to_emoji(txt)
            last_emoji[a] = emo
            if is_rainy_text(txt):
                rainy_windows[a].append(window_str)
            if is_thunder_text(txt):
                saw_thunder[a] = True

    out = {}
    for a in area_names:
        # dedupe windows while preserving order
        dedup = []
        for w in rainy_windows[a]:
            if w not in dedup:
                dedup.append(w)

        if dedup:
            out[a] = {"emoji": "⛈️" if saw_thunder[a] else "🌧️", "windows": dedup}
        else:
            out[a] = {"emoji": last_emoji[a], "windows": []}

    return out


def main():
    if len(sys.argv) < 2:
        print("usage: bus_eta.py <alias> [--json]")
        sys.exit(2)

    alias = sys.argv[1].strip().lower()
    as_json = (len(sys.argv) >= 3 and sys.argv[2] == "--json")

    root = Path(__file__).resolve().parent
    cfg = load_json(root / "config.json")
    lta_secrets = load_json((root / ".." / ".." / ".." / "secrets" / "lta_datamall.json").resolve())
    nus_secrets_path = (root / ".." / ".." / ".." / "secrets" / "nus_nextbus.json").resolve()
    nus_secrets = load_json(nus_secrets_path) if nus_secrets_path.exists() else None

    # Resolve alias via explicit synonym map, then fuzzy
    alias_map = cfg.get("aliasMap") or {}
    commands = cfg.get("commands") or {}

    # build reverse synonym lookup
    synonym_to_canonical = {}
    for canon, syns in alias_map.items():
        for s in (syns or []):
            synonym_to_canonical[str(s).strip().lower()] = canon

    if alias in synonym_to_canonical:
        alias = synonym_to_canonical[alias]

    if alias not in commands:
        known = sorted(commands.keys())
        # also allow fuzzy over synonyms
        all_tokens = sorted(set(list(known) + list(synonym_to_canonical.keys())))
        matches = difflib.get_close_matches(alias, all_tokens, n=3, cutoff=0.72)

        if len(matches) == 1:
            pick = matches[0]
            alias = synonym_to_canonical.get(pick, pick)
        elif len(matches) > 1:
            print(f"unknown alias: {alias}")
            print("did you mean:", ", ".join(matches))
            sys.exit(2)
        else:
            print(f"unknown alias: {alias}")
            print("known:", ", ".join(known))
            sys.exit(2)

    stops = commands[alias].get("stops") or []
    if not stops:
        print(f"no stops configured for alias: {alias}")
        sys.exit(2)

    payload_stops = []

    for stop_cfg in stops:
        stop_type = stop_cfg.get("type", "lta")

        if stop_type == "nus":
            if not nus_secrets:
                raise RuntimeError("NUS NextBus credentials missing: secrets/nus_nextbus.json")

            stop_code = stop_cfg["stopCode"]
            stop_name = stop_cfg.get("name") or stop_code
            services_filter = stop_cfg.get("services", "all")

            import base64
            u = nus_secrets["basic_auth"]["username"]
            p = nus_secrets["basic_auth"]["password"]
            token = base64.b64encode(f"{u}:{p}".encode()).decode()

            url = nus_secrets.get("base_url", "https://nnextbus.nus.edu.sg").rstrip("/")
            req = urllib.request.Request(
                f"{url}/ShuttleService?busstopname={urllib.parse.quote(stop_code)}",
                headers={"Authorization": f"Basic {token}", "accept": "application/json"},
            )

            with urllib.request.urlopen(req, timeout=20) as res:
                data = json.load(res)

            result = (data.get("ShuttleServiceResult") or {})
            shuttles = result.get("shuttles") or []
            out = []

            def parse_mins(x):
                try:
                    return int(str(x).strip())
                except Exception:
                    return None

            tmp = []
            for sh in shuttles:
                svc = str(sh.get("name") or "").strip()
                if not svc:
                    continue
                if services_filter != "all" and svc not in set(map(str, services_filter)):
                    continue

                m1 = parse_mins(sh.get("arrivalTime"))
                m2 = parse_mins(sh.get("nextArrivalTime"))
                if m1 is None and m2 is None:
                    continue

                tmp.append({"service": svc, "eta1": m1, "eta2": m2})

            # De-dupe by service (sometimes API returns multiple entries). Keep the one with earliest eta1.
            best = {}
            for x in tmp:
                svc = x["service"]
                cur = best.get(svc)
                key = (10**9 if x["eta1"] is None else x["eta1"], 10**9 if x["eta2"] is None else x["eta2"])
                if cur is None:
                    best[svc] = (key, x)
                else:
                    if key < cur[0]:
                        best[svc] = (key, x)

            out = [v[1] for v in best.values()]
            out.sort(key=lambda x: (10**9 if x["eta1"] is None else x["eta1"], x["service"]))

        else:
            stop_code = stop_cfg["busStopCode"]
            stop_name = stop_cfg.get("name") or stop_code
            services_filter = stop_cfg.get("services", "all")

            req = urllib.request.Request(
                f"{BASE}?BusStopCode={stop_code}",
                headers={
                    "AccountKey": lta_secrets["account_key"],
                    "accept": "application/json",
                },
            )

            with urllib.request.urlopen(req, timeout=20) as res:
                data = json.load(res)

            services = data.get("Services", [])
            out = []

            for s in services:
                svc = str(s.get("ServiceNo", "")).strip()
                if not svc:
                    continue

                if services_filter != "all" and svc not in set(map(str, services_filter)):
                    continue

                nb1 = s.get("NextBus", {})
                nb2 = s.get("NextBus2", {})

                m1 = eta_minutes(nb1.get("EstimatedArrival"))
                m2 = eta_minutes(nb2.get("EstimatedArrival"))

                # ignore services with no ETA at all
                if m1 is None and m2 is None:
                    continue

                out.append({
                    "service": svc,
                    "eta1": m1,
                    "eta2": m2,
                })

            out.sort(key=lambda x: (10**9 if x["eta1"] is None else x["eta1"], x["service"]))

        weather = None
        if stop_cfg.get("includeWeather"):
            areas = stop_cfg.get("weatherAreas") or []
            labels = []
            area_names = []
            for a in areas:
                labels.append(a.get("label") or a.get("neaArea"))
                area_names.append(a.get("neaArea"))

            area_names = [x for x in area_names if x]
            summary = summarize_weather_rest_of_day(area_names, until_hour=21)

            wx = []
            for a in areas:
                label = a.get("label") or a.get("neaArea")
                area = a.get("neaArea")
                if not area:
                    continue
                wx.append({
                    "label": label,
                    "emoji": summary[area]["emoji"],
                    "windows": summary[area]["windows"],
                })
            weather = wx

        payload_stops.append({
            "name": stop_name,
            "services": out,
            "weather": weather,
        })

    payload = {
        "alias": alias,
        "generatedAt": datetime.datetime.now(SGT).isoformat(timespec="seconds"),
        "stops": payload_stops,
    }

    if as_json:
        print(json.dumps(payload, indent=2))
        return

    # Pretty output for chat (simple + emoji-forward)
    # Example:
    # 🚌 Opp Blk 479
    # 6 • 🔥 ARR → 12m
    def fmt(m):
        if m is None:
            return "—"
        if m <= 0:
            return "ARR"
        return f"{m}m"

    lines = []

    for st in payload["stops"]:
        lines.append(f"🚌 {st['name']}")

        # services already sorted by earliest
        for s in st["services"]:
            svc = s["service"]
            m1 = s.get("eta1")
            m2 = s.get("eta2")
            icon = urgency_icon(m1)
            lines.append(f"{svc} • {icon} {fmt(m1)} → {fmt(m2)}")

        # optional weather block
        wx = st.get("weather")
        if wx:
            lines.append("")
            for w in wx:
                label = w.get("label")
                emo = w.get("emoji")
                windows = w.get("windows") or []
                if emo in ("🌧️", "⛈️") and windows:
                    lines.append(f"{emo} {label} ({', '.join(windows)})")
                else:
                    lines.append(f"{emo} {label}")

        lines.append("")

    print("\n".join(lines).rstrip())


if __name__ == "__main__":
    main()
