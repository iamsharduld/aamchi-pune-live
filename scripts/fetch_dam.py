#!/usr/bin/env python3
"""Fetch live Khadakwasla-cluster dam storage and write dam.json.

Source: numerical.co.in's Pune dams page, which mirrors the Water Resources
Department (Maharashtra) daily reservoir figures. Each dam is described as
"... At X% of its full capacity of Y million litres ...". We parse the four
dams that supply Pune (Khadakwasla, Panshet, Varasgaon, Temghar), compute the
cluster total, and write a small dam.json the static site reads (same-origin,
no CORS). Run daily by .github/workflows/dam.yml.
"""
from __future__ import annotations
import json, re, sys, datetime, urllib.request

URL = "https://numerical.co.in/numerons/collection/5985e2501d6090dc136dc381"
DAMS = ["Khadakwasla", "Panshet", "Varasgaon", "Temghar"]
# Match patterns (some dams carry aliases on the page, e.g. "Warasgaon (aka Varasgaon)").
NAME_PAT = {
    "Khadakwasla": r"Khadakwasla",
    "Panshet": r"Panshet",
    "Varasgaon": r"(?:Warasgaon|Varasgaon)",
    "Temghar": r"Temghar",
}
ML_PER_TMC = 28316.85  # 1 TMC = 10^9 cubic feet ~= 28,316.85 million litres


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (AamchiPuneLive dam fetcher)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def parse(html: str):
    dams = []
    for name in DAMS:
        m = re.search(
            NAME_PAT[name] + r"[^.]{0,30}?Dam\.\s*At\s+([\d.]+)%\s+of its full capacity of\s+([\d,]+)\s+million litres",
            html,
        )
        if not m:
            continue
        pct = float(m.group(1))
        cap_ml = float(m.group(2).replace(",", ""))
        dams.append({"name": name, "percent": round(pct, 2), "capacity_ml": cap_ml,
                     "current_ml": round(cap_ml * pct / 100, 1)})
    return dams


def main() -> int:
    html = fetch(URL)
    dams = parse(html)
    if len(dams) < 3:  # need at least most of the cluster to trust it
        print(f"Only parsed {len(dams)} dams — aborting (source layout may have changed).", file=sys.stderr)
        return 1
    cap = sum(d["capacity_ml"] for d in dams)
    cur = sum(d["current_ml"] for d in dams)
    out = {
        "source": "numerical.co.in (mirrors WRD Maharashtra daily reservoir data)",
        "source_url": URL,
        "official_reference": "https://www.pmc.gov.in/en/b/current-status-dams-pune-region-2025",
        "fetched_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cluster": {
            "name": "Khadakwasla cluster",
            "dams_parsed": [d["name"] for d in dams],
            "percent": round(cur / cap * 100, 1),
            "current_tmc": round(cur / ML_PER_TMC, 2),
            "capacity_tmc": round(cap / ML_PER_TMC, 2),
        },
        "dams": dams,
    }
    with open("dam.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    c = out["cluster"]
    print(f"Wrote dam.json — cluster {c['percent']}% ({c['current_tmc']}/{c['capacity_tmc']} TMC) "
          f"from {len(dams)} dams.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
