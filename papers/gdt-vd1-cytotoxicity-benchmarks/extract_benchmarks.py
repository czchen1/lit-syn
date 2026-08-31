#!/usr/bin/env python3
"""Mine downloaded full-text XML for the numbers this collection benchmarks against.

Three families of sentence are pulled out, each anchored to a number so the output can
be read as candidate benchmark values rather than prose:

  et      killing tied to an effector:target ratio (or a bare "10:1"-style ratio next to
          a lysis/cytotoxicity word)
  purity  Vdelta1 / Vdelta2 / gd TCR percentage of the product after expansion
  dn      CD4-CD8- double-negative fraction

Usage:
  extract_benchmarks.py                 write benchmarks.tsv for every indexed full text
  extract_benchmarks.py <pmid> [...]    print matching sentences for those papers
"""
import csv
import os
import re
import sys
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, "index.tsv")
OUT = os.path.join(BASE, "benchmarks.tsv")

RATIO = r"\d{1,3}\s?(?::|to)\s?\d{1,3}"
ET_RE = re.compile(
    r"(effector[ :/-]*(?:to|:)[ :/-]*target|effector ?: ?target|\bE ?[:/] ?T\b|"
    r"\bE ?: ?T ratio|" + RATIO + r"\s*\(?E ?[:/] ?T)", re.I)
LYSIS_RE = re.compile(
    r"(specific lysis|% ?lysis|percent(?:age)? (?:of )?lysis|cytotox|killing|"
    r"cell death|viabilit|apoptos|elimination of)", re.I)
PURITY_RE = re.compile(
    r"(V ?delta ?[12]|Vδ ?[12]|\bVd ?[12]\b|V ?gamma ?9|Vγ ?9|"
    r"gamma[- ]?delta|γδ|TCR ?δ|pan[- ]?δ|purity|CD3\+)", re.I)
DN_RE = re.compile(
    r"(CD4[-−]\s?CD8[-−]|CD4[-−]/CD8[-−]|double[- ]negative|\bDN\b(?! ?A)|"
    r"CD4 and CD8 (?:double )?negative)", re.I)
PCT = re.compile(r"\d{1,3}(?:\.\d+)?\s?(?:%|per cent)")


def text_of(el):
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def sentences(path):
    root = ET.parse(path).getroot()
    chunks = []
    for el in root.iter():
        if el.tag in ("p", "title", "caption"):
            t = text_of(el)
            if t:
                chunks.append(t)
        elif el.tag == "table-wrap":
            chunks.append("[TABLE] " + text_of(el)[:6000])
    out = []
    for c in chunks:
        for s in re.split(r"(?<=[.;])\s+(?=[A-Z0-9(])", c):
            s = s.strip()
            if 20 < len(s) < 700:
                out.append(s)
    return out


def classify(s):
    kinds = []
    has_pct = bool(PCT.search(s))
    has_ratio = bool(re.search(r"\b" + RATIO + r"\b", s))
    if ET_RE.search(s) and (has_pct or has_ratio) and LYSIS_RE.search(s):
        kinds.append("et")
    elif has_ratio and LYSIS_RE.search(s) and has_pct:
        kinds.append("et")
    if has_pct and PURITY_RE.search(s) and \
            re.search(r"(purity|expan\w+|product|after \d+ days|culture|enrich\w+|"
                      r"consisted of|comprised|represented|median|mean)", s, re.I):
        kinds.append("purity")
    if has_pct and DN_RE.search(s):
        kinds.append("dn")
    return kinds


def main():
    rows = list(csv.DictReader(open(IDX), delimiter="\t"))
    wanted = set(sys.argv[1:])
    hits = []
    for r in rows:
        ft = r.get("fulltext_xml") or ""
        if not ft:
            continue
        if wanted and r["pmid"] not in wanted:
            continue
        path = os.path.join(BASE, ft)
        if not os.path.exists(path):
            continue
        try:
            sents = sentences(path)
        except ET.ParseError:
            continue
        for s in sents:
            for kind in classify(s):
                hits.append({"kind": kind, "pmid": r["pmid"], "year": r["year"],
                             "first_author": r["authors"].split(",")[0],
                             "sentence": s})

    if wanted:
        for h in hits:
            print(f"[{h['kind']}] {h['first_author']} {h['year']} pmid{h['pmid']}: {h['sentence']}")
        return

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["kind", "pmid", "year", "first_author", "sentence"],
                          delimiter="\t")
        w.writeheader()
        for h in hits:
            h["sentence"] = h["sentence"].replace("\t", " ")
            w.writerow(h)
    from collections import Counter
    print(f"{len(hits)} candidate benchmark sentences from "
          f"{len({h['pmid'] for h in hits})} papers -> benchmarks.tsv")
    print(Counter(h["kind"] for h in hits))


if __name__ == "__main__":
    main()
