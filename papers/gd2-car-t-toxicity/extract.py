#!/usr/bin/env python3
"""Print plain text (or toxicity-relevant paragraphs) from downloaded full-text XML.

Usage:
  extract.py <pmid> [...]            whole article text
  extract.py --tox <pmid> [...]      only paragraphs matching the toxicity vocabulary
"""
import csv
import os
import re
import sys
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))

TOX_RE = re.compile(
    r"\b(toxicit|adverse|grade [1-5]|CRS\b|cytokine release|neurotox|ICANS|TIAN|"
    r"intracranial pressure|hydrocephalus|tocilizumab|anakinra|dexamethasone|"
    r"steroid|transaminas|\bALT\b|\bAST\b|bilirubin|liver|hepatic|creatinine|"
    r"renal|kidney|electrolyte|sodium|hyponatr|cytopeni|neutropeni|thrombocytopeni|"
    r"coagulop|fibrinogen|ferritin|HLH|hemophagocyt|pain|neuropath|"
    r"seizure|edema|oedema|ICU|vasopressor|hypotension|fever|"
    r"dose[- ]limiting|DLT|infection|CSF)", re.I)


def paths():
    rows = list(csv.DictReader(open(os.path.join(BASE, "index.tsv")), delimiter="\t"))
    return {r["pmid"]: r for r in rows if r["pmid"]}


def text_of(el):
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def article_text(path, tox_only=False):
    tree = ET.parse(path)
    root = tree.getroot()
    out = []
    for sec in root.iter():
        if sec.tag not in ("sec", "abstract"):
            continue
        title = sec.find("title")
        head = text_of(title) if title is not None else ""
        paras = [text_of(p) for p in sec.findall("./p")]
        paras = [p for p in paras if p]
        if tox_only:
            paras = [p for p in paras if TOX_RE.search(p)]
        if head or paras:
            if head:
                out.append(f"\n## {head}")
            out.extend(paras)
    # tables often carry the per-patient toxicity grades
    for tw in root.iter("table-wrap"):
        t = text_of(tw)
        if not tox_only or TOX_RE.search(t):
            out.append("\n[TABLE] " + t[:4000])
    return "\n".join(out)


def main():
    args = sys.argv[1:]
    tox_only = "--tox" in args
    args = [a for a in args if a != "--tox"]
    idx = paths()
    for pmid in args:
        row = idx.get(pmid)
        if not row or not row["fulltext_xml"]:
            print(f"### {pmid}: no full text in index")
            continue
        print(f"\n\n===== {pmid} {row['year']} {row['title']}\n")
        print(article_text(os.path.join(BASE, row["fulltext_xml"]), tox_only))


if __name__ == "__main__":
    main()
