#!/usr/bin/env python3
"""Dry-run: report Europe PMC hit counts per query without harvesting records."""
import json
import urllib.parse
import urllib.request

from harvest import EPMC, NODATE, QUERIES, WINDOW


def count(query):
    params = urllib.parse.urlencode({"query": query, "format": "json", "pageSize": 1})
    req = urllib.request.Request(f"{EPMC}?{params}", headers={"User-Agent": "lit-syn/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.load(resp).get("hitCount", 0)


def main():
    total = 0
    for domain, queries in QUERIES.items():
        for i, q in enumerate(queries):
            modern = count(f"({q}) AND {WINDOW}")
            allt = count(f"({q}) AND {NODATE}")
            total += modern
            print(f"{domain}[{i}]: modern={modern} all={allt}")
    print(f"overlapping modern total: {total}")


if __name__ == "__main__":
    main()
