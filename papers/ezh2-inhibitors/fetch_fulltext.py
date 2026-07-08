#!/usr/bin/env python3
"""Mirror open-access full-text XML (Europe PMC) for curated EZH2 papers.

Reads index.tsv, and for every row with a PMCID and OA status, downloads the
Europe PMC full-text XML into fulltext/<firstauthor>_<year>_pmid<pmid>.xml, then
writes the relative path back into the local_fulltext column.
"""
import csv, os, re, time, sys, urllib.request

BASE = "/home/ubuntu/repos/lit-syn/papers/ezh2-inhibitors"
IDX = f"{BASE}/index.tsv"
FT = f"{BASE}/fulltext"
FT_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"

os.makedirs(FT, exist_ok=True)


def first_author(authors):
    a = (authors or "").split(",")[0].strip()
    a = re.sub(r"\s+[A-Z]{1,3}$", "", a)  # drop trailing initials
    a = re.sub(r"[^A-Za-z]", "", a).lower()
    return a or "anon"


def fetch(pmcid):
    url = FT_URL.format(pmcid=pmcid)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                data = r.read()
                if data and b"<article" in data[:5000]:
                    return data
                return None
        except Exception as e:
            sys.stderr.write(f"retry {attempt} {pmcid}: {e}\n")
            time.sleep(2)
    return None


rows = list(csv.DictReader(open(IDX), delimiter="\t"))
cols = rows[0].keys() if rows else []
n_ok = 0
for r in rows:
    if r["status"] != "OA_available" or not r["pmcid"]:
        continue
    fn = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid']}.xml"
    path = os.path.join(FT, fn)
    if not os.path.exists(path):
        data = fetch(r["pmcid"])
        time.sleep(0.34)
        if not data:
            continue
        with open(path, "wb") as f:
            f.write(data)
    r["local_fulltext"] = f"fulltext/{fn}"
    n_ok += 1

with open(IDX, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(cols), delimiter="\t")
    w.writeheader()
    w.writerows(rows)

print(f"mirrored {n_ok} full-text XMLs")
