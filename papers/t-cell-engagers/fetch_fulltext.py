#!/usr/bin/env python3
"""Download open-access full-text XML from Europe PMC for OA rows with a PMCID.

Stores to fulltext/<firstauthor>_<year>_pmid<pmid>.xml and records the local
path back into index.tsv (local_pdf column reused for full-text path).
"""
import csv, os, re, time, urllib.request

BASE = "/home/ubuntu/repos/lit-syn/papers/t-cell-engagers"
IDX = os.path.join(BASE, "index.tsv")
FT = os.path.join(BASE, "fulltext")
os.makedirs(FT, exist_ok=True)

def first_author(authors):
    if not authors:
        return "anon"
    a = authors.split(",")[0].split(" ")[0]
    return re.sub(r"[^a-z0-9]", "", a.lower()) or "anon"

rows = list(csv.DictReader(open(IDX), delimiter="\t"))
ok = fail = 0
for r in rows:
    pmcid = r["pmcid"].strip()
    if not pmcid or r["status"] != "OA_available":
        continue
    pid = pmcid if pmcid.upper().startswith("PMC") else "PMC" + pmcid
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pid}/fullTextXML"
    fname = f"{first_author(r['authors'])}_{r['year']}_pmid{r['pmid'] or pmcid}.xml"
    dest = os.path.join(FT, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 2000:
        r["local_fulltext"] = f"fulltext/{fname}"
        ok += 1
        continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        head = data[:5000].lower() if data else b""
        if data and len(data) > 2000 and b"<article" in head:
            with open(dest, "wb") as f:
                f.write(data)
            r["local_fulltext"] = f"fulltext/{fname}"
            ok += 1
        else:
            fail += 1
    except Exception as e:
        fail += 1
    time.sleep(0.34)

cols = ["category","authors","title","venue","year","pmid","doi","pmcid","url","local_fulltext","supp_pdf","topics","status"]
with open(IDX, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
    w.writeheader()
    for r in rows:
        w.writerow(r)

print(f"fulltext downloaded: {ok}, failed/unavailable: {fail}")
