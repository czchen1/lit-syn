#!/usr/bin/env python3
"""Download open-access full-text XML from Europe PMC for curated rows.

Priority order: clinical trials, manufacturing/process papers and human
translational studies first, then preclinical work and reviews, so a partial run
still yields the rows that matter most for protocol-level detail. Local paths are
written back into index.tsv and curated.json.
"""
import csv
import json
import os
import re
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "index.tsv")
CURATED = os.path.join(HERE, "curated.json")
FT = os.path.join(HERE, "fulltext")
os.makedirs(FT, exist_ok=True)

PRIORITY = {"clinical_trial": 0, "process_method": 1, "translational_human": 2,
            "preclinical": 3, "systematic_review": 4, "review": 5, "mechanistic": 6}
MAX_FETCH = 220


def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"


def fetch(pmcid):
    pid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pid}/fullTextXML"
    req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read()


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    order = sorted(range(len(rows)),
                   key=lambda i: (PRIORITY.get(rows[i]["evidence"], 9),
                                  -int(rows[i]["cited"] or 0)))
    ok = fail = 0
    for i in order:
        r = rows[i]
        if ok >= MAX_FETCH:
            break
        pmcid = r["pmcid"].strip()
        if not pmcid:
            continue
        fname = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid'] or pmcid}.xml"
        dest = os.path.join(FT, fname)
        if os.path.exists(dest) and os.path.getsize(dest) > 2000:
            r["local_fulltext"] = f"fulltext/{fname}"
            ok += 1
            continue
        try:
            data = fetch(pmcid)
        except Exception:
            data = b""
        if data and len(data) > 2000 and b"<article" in data[:5000].lower():
            with open(dest, "wb") as f:
                f.write(data)
            r["local_fulltext"] = f"fulltext/{fname}"
            ok += 1
        else:
            fail += 1
        time.sleep(0.34)

    with open(IDX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    paths = {r["pmid"]: r.get("local_fulltext", "") for r in rows if r["pmid"]}
    curated = json.load(open(CURATED))
    for item in curated:
        item["local_fulltext"] = paths.get(item["pmid"], "")
    with open(CURATED, "w") as f:
        json.dump(curated, f, indent=1)

    print(f"fulltext available: {ok}, unavailable: {fail}")


if __name__ == "__main__":
    main()
