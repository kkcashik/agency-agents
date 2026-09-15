# Which niche to scrape

Targeting guide for selling AI Receptionist / Off Hours Agent, GHL, local SEO, AEO and ads
management to local businesses. Ready-to-run keyword files live in
[`examples/niches/`](examples/niches/).

> **On the dollar figures below:** they're order-of-magnitude industry ranges to help you
> frame the pitch — *"one missed furnace call is worth more than a year of my fee"* — not
> measured data. Don't quote them to a prospect as research. The **qualifying filter** further
> down is the reliable part: it's built on fields the scraper actually returns.

---

## The rubric

A niche is worth a $1K/mo retainer only if it hits **4 of these 5**:

1. **Job ticket over $500** — one recovered missed call pays your fee
2. **Phone-first booking** — they call, they don't fill out forms
3. **After-hours or emergency demand** — this is what the Off Hours Agent *is*
4. **Repeat visits or high lifetime value** — they keep paying because the client does
5. **Dense on Google Maps, thin online** — good scrape yield, plus a visible gap to point at

Miss #1 or #2 and the offer doesn't land no matter how good the build is.

---

## Tier 1 — closest fit to the offer

| Niche | Ticket | Why it closes | Lead with |
|---|---|---|---|
| **Dental** | $200–3k+ | CDCP surge; staff repeat the same coverage questions all day | Receptionist + CDCP FAQ |
| **HVAC** | $5–15k | No heat in a Toronto January — they call until someone answers | Off Hours Agent |
| **Plumbing** | $300–5k | Flood at 11pm. First answer wins the job, every time | Off Hours Agent |
| **Med spa** | $500–3k | High no-show rate; reminders alone justify the retainer | GHL + reminders |
| **Law (PI/family/immigration)** | $5k+ per case | Case value is enormous; already spending heavily on ads | Ads + intake |

Files: `dental.txt` · `hvac.txt` · `plumbing.txt` · `medspa.txt` · `legal.txt`

**Trade-off worth knowing:** law has the biggest ticket but the longest sales cycle and the
most competition for your services. HVAC and plumbing close fastest on the after-hours pitch
because the pain is undeniable and seasonal.

---

## Tier 2 — easier close, lower ceiling

| Niche | Ticket | Why it closes | Lead with |
|---|---|---|---|
| **Veterinary** | $200–2k | Phone-swamped, after-hours emergencies, rarely automated | Receptionist |
| **Chiro / physio / RMT** | $80–200/visit | High LTV; no-shows are their #1 revenue leak | GHL + reminders |
| **Roofing / electrical** | $500–20k | Quote-appointment model; response time decides who wins | Local SEO + ads |
| **Auto / collision** | $300–8k | Insurance-driven, customers call while stranded | Receptionist |

Files: `veterinary.txt` · `health-clinics.txt` · `home-services.txt` · `auto.txt`

---

## Skip for now

**Restaurants, salons, barbers, nail salons, gyms, retail.** The Maps volume is enormous and
the scrape is easy — that's the trap. Ticket size is too low, churn is high, and $1K/mo is a
hard sell against their margins. Come back when you have case studies and a cheaper tier.

---

## The qualifying filter — where the money actually is

A raw scrape of "dentist in North York" returns everyone. These three cuts, run against the
columns `scrape.py` gives you (`title, phone, emails, website, category, address,
review_rating, review_count`), separate buyers from noise:

| Signal | Filter | What it means |
|---|---|---|
| 🎯 **Best target** | `review_count` 10–150 **and** `review_rating` ≥ 4.0 | Established, has budget, not yet dominant. Growth is still on their mind. |
| 💰 **Full-stack sell** | `website` is empty | No web presence at all. Sell the whole thing, not just the receptionist. |
| 🔧 **Reputation play** | `review_count` > 50 **and** `review_rating` < 4.0 | Already bleeding. Lead with review collection, expand later. |

**Who to skip:** `review_count` under 10 (too new, no money) and over 300 with a 4.8+ rating
(already has an agency, or doesn't think they need one).

### Doing the cut in a spreadsheet

Open the `results-<id>.csv` and sort by `review_count`, then filter `review_rating`. That's it.
Don't overbuild this — the list is a means to a phone call, not a data project.

---

## How to actually run it

Keyword files here are **location-agnostic** — `--city` geocodes for you, so one file works
across the whole GTA:

```bash
cd tools/google-maps-scraper-kit
docker compose up -d
python3 scripts/scrape.py --keywords-file examples/niches/hvac.txt --city "Mississauga, ON" --depth 5
```

Work through [`examples/gta-cities.txt`](examples/gta-cities.txt) one city at a time. **Slice
the map, don't raise the depth** — Google caps results per query, so eight neighbourhood runs
beat one "Toronto" run at the same depth, and they're gentler on your IP.

**One job at a time.** Back-to-back large jobs get your IP temporarily rate-limited.

---

## Before you contact anyone

Scraped phone numbers and emails are **personal data under PIPEDA**, and cold commercial
email is regulated by **CASL** — which, unlike US CAN-SPAM, generally requires consent rather
than just an unsubscribe link. Penalties are real.

The safer lane: business contact info the clinic publishes on its own site, and phone calls
rather than bulk email. Treat the scrape as a **research list to qualify and call**, not a
mailing list. Don't resell raw Google data.
