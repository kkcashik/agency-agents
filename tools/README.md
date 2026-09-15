# 🧰 Tools

Standalone tools that live alongside the agent roster. Each one is self-contained —
`cd` into its folder and follow its own README/SETUP.

| Tool | What it does | Start here |
|---|---|---|
| [`google-maps-scraper-kit/`](google-maps-scraper-kit/) | Runs a free, local Google Maps scraper (Docker) and lets Claude drive it. Give it a city + business type, get back a clean lead list: name, phone, email, website, category, address, rating, review count. | [SETUP.md](google-maps-scraper-kit/SETUP.md) |

## google-maps-scraper-kit — 60-second start

```bash
cd tools/google-maps-scraper-kit
docker compose up -d                      # starts the scraper on http://localhost:8080
curl http://localhost:8080/api/v1/jobs    # should print [] — it's alive
```

Then either run it yourself:

```bash
python3 scripts/scrape.py "dentists in Toronto ON" --city "Toronto, ON" --depth 5
```

…or open Claude Code **inside that folder** (`claude`) so its skill, `/scrape` commands and
pre-approved permissions load, and just say *"scrape dentists in North York, Toronto."*

A ready-made Toronto dental keyword list ships at
[`examples/toronto-dental.txt`](google-maps-scraper-kit/examples/toronto-dental.txt):

```bash
python3 scripts/scrape.py --keywords-file examples/toronto-dental.txt --city "Toronto, ON" --depth 5
```

> ⚠️ Scraping Google Maps is against Google's ToS and heavy use can get your IP temporarily
> rate-limited. One job at a time, start at `depth 5`. Scraped phones/emails are personal data —
> follow PIPEDA/CASL (Canada), GDPR/CCPA/CAN-SPAM as applicable. Result files are git-ignored.
> Upstream scraper: [`gosom/google-maps-scraper`](https://github.com/gosom/google-maps-scraper) (MIT).
