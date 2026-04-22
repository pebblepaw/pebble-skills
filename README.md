# pebble-skills

A growing collection of custom Copilot skills I've built and refined as an AI-native developer.

Some of these exist because I got tired of asking Claude to write clearly and it writing like a corporate memo. Some exist because I needed a bus ETA tool at 8am. All of them are real and in use.

---

## Coding Agent Skills

Skills that change *how* the agent thinks, writes, or plans — not what it does.

| Skill | What it does | Origin story |
|---|---|---|
| [`the-hemingway-rule`](./the-hemingway-rule/SKILL.md) | Forces the agent to write like a human being. No hedging, no filler, no "it is worth noting that". Every sentence must explain what's broken, why it matters, or what to do. | Distilled from Claude Opus 4.6. I got Opus to reflect on what made its own explanations actually readable, then prompted it to write a style guide that I could use to make Codex write the same way. Codex left to its own devices writes like it's being deposed. This fixes that. |

---

## OpenClaw Skills

Skills that add tool capabilities — fetching data, calling APIs, doing things.

| Skill | What it does | Needs keys? |
|---|---|---|
| [`sg-bus-eta`](./sg-bus-eta/) | `/bus …` quick commands for **LTA DataMall bus ETAs** + **NUS NextBus ETAs** | **Yes** (LTA key). NUS NextBus uses Basic Auth (public creds exist) |

---

## Adding a skill

Each skill lives in its own folder with a `SKILL.md`. The frontmatter `description` field is what tells the agent when to load it — write it like a search query, not a marketing tagline.
