---
name: sg-bus-eta
version: 0.1.0
description: Quick /bus commands for SG bus ETAs (LTA DataMall) + optional NEA weather + optional NUS NextBus.
---

# sg-bus-eta

A simple skill to let your user type **`/bus <alias>`** in chat and get back:
- bus services sorted by the **soonest arriving**
- the **next 2 ETAs per service**
- fun urgency emojis (🔥⏳💤)
- (optional) NEA weather summary until 9pm
- (optional) NUS NextBus timings

## Setup (what to ask the user)

### 1) LTA DataMall API key (required)
Ask the user for their **LTA DataMall AccountKey**.
- Sign up / docs: https://datamall.lta.gov.sg/

Store it locally (example):
- create `secrets/lta_datamall.json`
  ```json
  {"account_key": "<PASTE_HERE>"}
  ```
- lock it down:
  ```bash
  chmod 600 secrets/lta_datamall.json
  ```

### 2) Configure their frequent stops + relevant services
Edit `scripts/config.json`.

You’ll define:
- aliases like `home`, `work`, `bishan`
- for each alias: one or more stops
- for each stop: bus stop code + services

Tips:
- If user doesn’t know the BusStopCode, you can search via LTA DataMall **BusStops** endpoint and match by description.

### 3) (Optional) Weather summary until 9pm
This uses **data.gov.sg / NEA 24-hour forecast** (no key).
- Collection: https://data.gov.sg/collections/1459/view

Note: NEA forecasts are regional; you’ll map user areas (e.g., Pasir Ris) to a region.

### 4) (Optional) NUS NextBus
NUS NextBus is protected by **HTTP Basic Auth**.

This skill supports:
- `GET https://nnextbus.nus.edu.sg/ShuttleService?busstopname=<STOP_CODE>`

You should ask the user whether they consent to using the known public credentials (or provide their own).

Store credentials in:
- `secrets/nus_nextbus.json`
  ```json
  {
    "base_url": "https://nnextbus.nus.edu.sg",
    "basic_auth": {"username": "...", "password": "..."}
  }
  ```
- `chmod 600 secrets/nus_nextbus.json`

## Run / test locally

```bash
python3 scripts/bus_eta.py home
python3 scripts/bus_eta.py nus
```

## Output rules

- next 2 ETAs per service
- services sorted by earliest ETA
- emojis:
  - 🔥 = arriving/soon (≤3m)
  - ⏳ = 4–10m
  - 💤 = >10m
- weather: if any rain occurs between now and 9pm, show ⛈️/🌧️ + time windows (e.g. `4–6pm`)
