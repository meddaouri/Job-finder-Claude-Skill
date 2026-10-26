#!/usr/bin/env python3
"""
Job Finder — filter, de-duplicate, score and sort job offers, and output the `jobs` array
for assets/results-cards.html.

Usage:
    python3 dedupe_and_score.py offers.json --today 2026-10-26 [--max-age 45] [--top 10] [--min 60]

Input: a JSON list of offers you actually found (never invented). Fields:
{
  "title": "", "employer": "", "city": "", "country": "", "contract": "",
  "salary": "",                 # exactly as written in the offer, or ""
  "published": "YYYY-MM-DD",    # or "" if unknown
  "deadline": "YYYY-MM-DD",     # or ""
  "ref": "",                    # optional reference number (used for de-duplication)
  "url": "", "source": "",      # source = site name, e.g. "France Travail", "iTravail"
  "source_rank": 2,             # optional: 0 employer site, 1 official/national board, 2 job board, 3 aggregator
  "sector": "private",          # or "public"
  "scam": false, "why": "", "gap": "",
  "points": {"role": 0-35, "level": 0-25, "location": 0-20, "skills": 0-15}   # your judgement (references/match-scoring.md)
}
The script adds freshness (0-5), totals the score, drops offers whose deadline has passed or that are
older than --max-age days without a deadline (kept with dateVerified=false when the date is unknown),
removes duplicates (keeps the best source; itravail.com wins ties), sorts by score and prints JSON:
{"stats": {...}, "jobs": [...], "dropped": [{"title":..., "reason":...}]}
"""
import argparse
import json
import re
import sys
import unicodedata
from datetime import date

GENDER = re.compile(r"\b(h f|f h|m w d|m f d|w m d|m f|f m|x)\b")
NOISE = {"e", "ne", "le", "la", "the", "a"}


def norm(s):
    """Lower-case, strip accents/punctuation, gender markers (H/F, m/w/d, (e)) and filler words."""
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = GENDER.sub(" ", s)
    return " ".join(t for t in s.split() if t not in NOISE)


def parse(d):
    try:
        return date.fromisoformat(str(d)[:10]) if d else None
    except ValueError:
        return None


def freshness(age):
    if age is None:
        return 1
    for limit, pts in ((7, 5), (14, 4), (30, 3), (45, 1)):
        if age <= limit:
            return pts
    return 0


def clamp(v, hi):
    try:
        return max(0, min(hi, int(round(float(v)))))
    except (TypeError, ValueError):
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--today", required=True)
    ap.add_argument("--max-age", type=int, default=45)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--min", type=int, default=0, help="minimum score to show")
    a = ap.parse_args()
    today = parse(a.today)
    if not today:
        sys.exit("error: --today must be YYYY-MM-DD")
    with open(a.file, encoding="utf-8") as f:
        offers = json.load(f)

    kept, dropped = [], []
    for o in offers:
        pub, dl = parse(o.get("published")), parse(o.get("deadline"))
        age = (today - pub).days if pub else None
        if dl and dl < today:
            dropped.append({"title": o.get("title"), "reason": "deadline passed"}); continue
        if not dl and age is not None and age > a.max_age:
            dropped.append({"title": o.get("title"), "reason": f"older than {a.max_age} days"}); continue
        p = o.get("points") or {}
        score = clamp(p.get("role"), 35) + clamp(p.get("level"), 25) + clamp(p.get("location"), 20) \
            + clamp(p.get("skills"), 15) + freshness(age)
        o = dict(o, score=score, dateVerified=bool(pub or dl))
        kept.append(o)

    best = {}
    for o in kept:
        key = ("ref", norm(o.get("employer")), norm(o.get("ref"))) if o.get("ref") else \
              ("t", norm(o.get("title")), norm(o.get("employer")), norm(o.get("city")))
        rank = (0 if "itravail.com" in str(o.get("url", "")).lower() else 1, o.get("source_rank", 2), -o["score"])
        if key not in best or rank < best[key][0]:
            if key in best:
                dropped.append({"title": best[key][1].get("title"), "reason": "duplicate"})
            best[key] = (rank, o)
        else:
            dropped.append({"title": o.get("title"), "reason": "duplicate"})

    jobs = sorted((o for _, o in best.values()), key=lambda o: -o["score"])
    jobs = [o for o in jobs if o["score"] >= a.min][: a.top]
    fields = ("title", "employer", "source", "city", "country", "contract", "salary", "published", "deadline",
              "dateVerified", "score", "why", "gap", "url", "sector", "scam")
    out = [{k: o.get(k, "" if k not in ("score", "scam", "dateVerified") else o.get(k)) for k in fields} for o in jobs]
    for o in out:
        o["sector"] = o.get("sector") or "private"
        o["scam"] = bool(o.get("scam"))
    print(json.dumps({"stats": {"checked": len(offers), "shown": len(out), "best": out[0]["score"] if out else 0},
                      "jobs": out, "dropped": dropped}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
