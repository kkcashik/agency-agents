#!/usr/bin/env python3
"""Filter a scrape result CSV down to the businesses actually worth calling.

    python3 scripts/qualify.py results-<id>.csv

Writes qualified.csv (sorted by review count, most reviews first) and prints the call list.
Three buckets, per NICHES.md:

  NO WEBSITE      website is empty          -> full-stack sell, not just the receptionist
  REPUTATION      >50 reviews, rating <4.0  -> already bleeding; lead with review collection
  BEST TARGET     10-150 reviews, >=4.0     -> established, has budget, not yet dominant

Everything else is dropped: under 10 reviews (too new, no money) and 4.0+ with a big review
count (already has an agency, or doesn't think they need one).

Stdlib only — no pip install. Uses the csv module rather than awk/grep because addresses
contain commas and would break naive line splitting.
"""
import csv
import sys

BUCKETS = {
    "NO WEBSITE": "full-stack sell",
    "REPUTATION": "review collection",
    "BEST TARGET": "receptionist",
}


def num(value):
    """Blank or non-numeric review fields are common — treat them as 0, never crash."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def bucket(row):
    rating = num(row.get("review_rating"))
    count = num(row.get("review_count"))
    if not (row.get("website") or "").strip():
        return "NO WEBSITE"
    if count > 50 and rating < 4.0:
        return "REPUTATION"
    if 10 <= count <= 150 and rating >= 4.0:
        return "BEST TARGET"
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python3 scripts/qualify.py results-<id>.csv")
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "qualified.csv"

    with open(src, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if rows and "review_count" not in rows[0]:
        sys.exit(
            f"{src} has no 'review_count' column. Did you scrape with --full or --fields?\n"
            "This filter needs the default lead columns."
        )

    keep = []
    for row in rows:
        label = bucket(row)
        if label:
            keep.append(dict(row, lead_type=label))
    keep.sort(key=lambda r: -num(r.get("review_count")))

    if not keep:
        print(f"0 of {len(rows)} qualified. Widen the scrape — try another city or --depth 10.")
        return

    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(keep[0].keys()))
        writer.writeheader()
        writer.writerows(keep)

    print(f"{len(keep)} of {len(rows)} qualified -> {out}\n")
    for r in keep:
        print(
            f"  [{r['lead_type']:11s}] {(r.get('title') or '')[:34]:34s} "
            f"{(r.get('phone') or '-'):16s} {r.get('review_rating') or '-'}* "
            f"({r.get('review_count') or '0'} reviews)"
        )
    print("\nCall the BEST TARGET rows first.")


if __name__ == "__main__":
    main()
