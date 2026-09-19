#!/usr/bin/env python3
"""Harvest NK-cell cancer-therapy literature from Europe PMC.

Scope: what makes NK-cell therapy work better — (i) NK phenotypes and cell states,
(ii) genetic/protein engineering (CAR-NK, cytokine armouring, knockouts, engagers),
(iii) ex vivo expansion, culture media, feeders, cryopreservation and GMP
manufacturing, plus the clinical evidence and TME-resistance context.

Query construction mirrors the other collections in this repo: broad vocabulary is
title-anchored (`TITLE:"..."`), highly specific vocabulary (agent names, programme
codes, gene targets) is searched over title+abstract, and an NK anchor clause plus a
cancer clause are conjoined so generic immunology/virology work stays out. Boolean
grouping is built in Python so AND/OR precedence is explicit.

Sweeps per query:
  * `modern`       2018-2026, cursor-paginated, citation-ranked
  * `recent`       2024-2026, citation-ranked (offsets citation lag for new work)
  * `foundational` all years, one citation-ranked page (landmarks: CD56dim/bright,
                   missing-self, K562-mbIL21 feeders, NK-92, CIML NK)

Output: raw_harvest.json (consumed by curate.py) and harvest.log.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "raw_harvest.json")
LOG = os.path.join(HERE, "harvest.log")

WINDOW = 'FIRST_PDATE:[2018-01-01 TO 2026-12-31] AND (SRC:MED OR SRC:PMC OR SRC:PPR)'
RECENT = 'FIRST_PDATE:[2024-01-01 TO 2026-12-31] AND (SRC:MED OR SRC:PMC OR SRC:PPR)'
NODATE = '(SRC:MED OR SRC:PMC)'


def phrase(term):
    return '"' + term.replace('"', "") + '"'


def concept(term):
    """Title-or-abstract match for one term; 'a & b' requires co-occurrence of both."""
    if " & " in term:
        return "(" + " AND ".join(concept(p.strip()) for p in term.split(" & ")) + ")"
    q = phrase(term)
    return f"(TITLE:{q} OR ABSTRACT:{q})"


def any_of(terms):
    """OR over title/abstract concepts. Europe PMC's default field includes the full
    text of OA articles, so every clause is field-restricted to stay specific."""
    return "(" + " OR ".join(concept(t) for t in terms) + ")"


def title_any(terms):
    return "(" + " OR ".join(f"TITLE:{phrase(t)}" for t in terms) + ")"


def journal_any(journals):
    return "(" + " OR ".join(f'JOURNAL:"{j}"' for j in journals) + ")"


NK = any_of([
    "natural killer cell", "natural killer cells", "NK cell", "NK cells", "NK-cell",
    "CAR-NK", "CAR NK", "NK-92", "NK92", "iPSC-NK", "iPSC-derived NK", "CIML NK",
    "cytokine-induced memory-like", "adaptive NK", "NKG2C", "primary NK cells",
])
NK_TITLE = title_any([
    "natural killer", "NK cell", "NK cells", "NK-cell", "NK-cells", "CAR-NK", "CAR NK",
    "NK-92", "iPSC-NK", "NK92", "NKG2C", "NKG2D", "NKp46", "CD16", "innate lymphoid",
])
CANCER = any_of([
    "cancer", "cancers", "tumor", "tumour", "tumors", "tumours", "carcinoma",
    "adenocarcinoma", "melanoma", "glioma", "glioblastoma", "sarcoma", "neoplasm",
    "neuroblastoma", "leukemia", "leukaemia", "lymphoma", "myeloma", "malignancy",
    "malignancies", "oncology", "antitumor", "antitumour", "anti-tumor", "anti-tumour",
])
SOLID = any_of([
    "solid tumor", "solid tumors", "solid tumour", "solid tumours", "carcinoma",
    "adenocarcinoma", "melanoma", "glioma", "glioblastoma", "sarcoma", "neuroblastoma",
    "mesothelioma", "breast cancer", "lung cancer", "non-small cell lung",
    "colorectal cancer", "pancreatic cancer", "ovarian cancer", "gastric cancer",
    "hepatocellular carcinoma", "renal cell carcinoma", "prostate cancer",
    "head and neck", "bladder cancer", "brain tumor", "brain tumour", "osteosarcoma",
])
TRIAL = any_of([
    "phase 1", "phase I", "phase 2", "phase II", "phase 1/2", "phase 1b",
    "first-in-human", "clinical trial", "dose-escalation", "single-arm", "open-label",
    "patients with", "infusion", "adoptive transfer", "haploidentical",
])
INVIVO = any_of([
    "mice", "mouse", "murine", "xenograft", "PDX", "NSG mice", "orthotopic", "in vivo",
    "tumor-bearing", "tumour-bearing", "humanized mouse",
])
MANUF = any_of([
    "expansion", "expanded", "manufacturing", "GMP", "good manufacturing practice",
    "feeder cells", "feeder-free", "culture", "cultured", "bioreactor", "scale-up",
    "cryopreservation", "cryopreserved", "closed system", "clinical-scale",
    "potency assay", "release testing", "process development", "serum-free",
    "xeno-free", "media", "medium",
])

QUERIES = {
    # -------------------------------------------------- phenotype / cell state biology
    "nk_phenotype_states": [
        f'{title_any(["NK cell subset", "NK cell subsets", "CD56bright", "CD56dim", "CD56 bright", "adaptive NK cells", "adaptive natural killer", "memory-like NK", "memory NK cells", "NK cell memory", "NK cell differentiation", "NK cell maturation", "NK cell education", "licensing", "NK cell heterogeneity", "NK cell diversity", "tissue-resident NK", "intratumoral NK cells", "tumor-infiltrating NK", "NK cell repertoire", "single-cell atlas of NK", "innate lymphoid cell 1", "NK cell identity"])} AND {NK} AND {CANCER}',
        f'{any_of(["CD57 & NK cell", "NKG2C+ adaptive", "FcRgamma-deficient NK", "g-NK cells", "FcepsilonRIgamma", "CD16bright", "NKp30 isoform", "KIR repertoire & NK", "self-KIR", "single-cell RNA sequencing & NK cell", "scRNA-seq & natural killer", "CITE-seq & NK", "mass cytometry & NK cell", "NK cell phenotype & prognosis", "high-dimensional & NK cell"])} AND {CANCER}',
        f'{title_any(["NK cell dysfunction", "NK cell exhaustion", "exhausted NK", "NK cell impairment", "dysfunctional NK", "NK cell senescence", "NK cell anergy", "NK cell fitness", "NK cell persistence", "NK cell activation"])} AND {CANCER}',
    ],
    # -------------------------------------------------- cell source comparison
    "nk_cell_sources": [
        f'{title_any(["peripheral blood NK", "cord blood NK", "cord blood-derived NK", "umbilical cord blood NK", "iPSC-derived NK", "induced pluripotent stem cell-derived NK", "iNK cells", "hematopoietic progenitor-derived NK", "CD34+ derived NK", "NK-92", "KHYG-1", "NK cell line", "placental NK", "allogeneic NK cells", "autologous NK cells", "off-the-shelf NK"])} AND {CANCER}',
        f'{any_of(["iPSC-NK & differentiation", "iPSC-derived NK & cytotoxicity", "cord blood NK & expansion", "NK-92 & irradiated", "taNK", "haNK", "off-the-shelf & NK cell product", "universal donor NK", "NK cell source comparison", "donor selection & NK cell", "KIR-ligand mismatch & donor"])} AND {CANCER}',
    ],
    # -------------------------------------------------- CAR-NK engineering
    "car_nk_engineering": [
        f'{title_any(["CAR-NK", "CAR NK", "chimeric antigen receptor NK", "chimeric antigen receptor natural killer", "CAR-expressing NK", "CAR-engineered NK", "NK cell receptor engineering", "engineered NK cells", "synthetic receptor & NK"])} AND {CANCER}',
        f'{any_of(["CAR-NK & costimulatory domain", "NKG2D-based CAR", "DAP10", "DAP12 & CAR", "2B4 & CAR NK", "CD28H", "chimeric costimulatory", "NKG2D ligand & CAR", "CAR NK & signaling domain", "CAR NK & CD19", "CAR NK & BCMA", "CAR NK & HER2", "CAR NK & mesothelin", "CAR NK & GD2", "CAR NK & B7-H3", "CAR NK & EGFR", "CAR NK & CD33", "CAR NK & claudin", "CAR NK & PSMA", "CAR NK & GPC3", "CAR-NK & solid tumor", "NKCE", "NK cell engager & trispecific", "TriKE", "BiKE", "bispecific killer engager", "trispecific killer engager", "AFM13", "AFM24", "innate cell engager", "NKp46 engager", "CD16 engager", "IL-15 & TriKE"])} AND {CANCER}',
        f'{any_of(["transposon & NK cell", "Sleeping Beauty & NK", "mRNA electroporation & NK cell", "lentiviral & NK cell transduction", "baboon envelope pseudotyped", "BaEV & NK", "AAV & NK cell", "retroviral & NK cell", "non-viral & NK cell engineering", "CRISPR & NK cell", "Cas9 & NK cell", "base editing & NK", "gene delivery & NK cell", "electroporation & natural killer"])} AND {CANCER}',
    ],
    # -------------------------------------------------- gene editing / knockouts
    "nk_gene_editing_targets": [
        f'{any_of(["CISH knockout", "CIS & NK cell", "Cish deletion", "SOCS3 & NK", "TGFBR2 knockout", "dominant negative TGF-beta receptor & NK", "TGF-beta & NK cell function", "ADAM17 inhibition & NK", "CD16 shedding", "non-cleavable CD16", "CD16 ADAM17", "NKG2A knockout", "KLRC1 knockout", "TIGIT knockout & NK", "PD-1 knockout & NK", "CBLB", "Cbl-b & NK", "ZEB2 & NK", "AHR & NK cell", "regnase-1 & NK", "ZC3H12A & NK", "SMAD3 & NK", "hypoxia & NK cell function", "HIF-1alpha & NK cell", "metabolic reprogramming & NK cell", "glycolysis & NK cell", "OXPHOS & NK cell", "fatty acid & NK cell dysfunction", "cholesterol & NK cell", "mitochondrial & NK cell function"])} AND {CANCER}',
        f'{title_any(["NK cell metabolism", "metabolic fitness of NK", "NK cell metabolic", "NK cell armoring", "armored NK", "engineered cytokine & NK"])} AND {CANCER}',
    ],
    # -------------------------------------------------- cytokine support / armouring
    "cytokine_support": [
        f'{any_of(["IL-15 & NK cell", "IL-15 superagonist", "N-803", "ALT-803", "nogapendekin", "sIL-15", "membrane-bound IL-15", "mbIL15", "IL-15/IL-15Ralpha", "IL-15 transpresentation", "IL-21 & NK cell expansion", "IL-12 IL-15 IL-18", "IL-18 & NK cell", "decoy-resistant IL-18", "IL-2 & NK cell", "IL-2 variant & NK", "cytokine-induced memory-like NK", "preactivation & NK cell", "IL-27 & NK", "IL-7 & NK", "autocrine IL-15", "cytokine armoring & NK"])} AND {CANCER}',
        f'{title_any(["interleukin-15", "IL-15", "IL-21", "IL-18", "memory-like natural killer", "cytokine-induced memory-like"])} AND {NK} AND {CANCER}',
    ],
    # -------------------------------------------------- expansion & feeders
    "expansion_feeders": [
        f'{title_any(["NK cell expansion", "expansion of NK cells", "expansion of natural killer", "ex vivo expanded NK", "ex vivo expansion", "large-scale expansion", "clinical-scale expansion", "feeder cells", "feeder-free", "NK cell culture", "culture system & NK"])} AND {NK} AND {CANCER}',
        f'{any_of(["K562-mbIL21", "K562 & 4-1BBL & IL-21", "K562-mb15-41BBL", "mbIL21 & feeder", "PM21 particles", "plasma membrane particles & NK", "EBV-LCL feeder", "irradiated feeder cells & NK", "membrane particle & NK expansion", "exosome & NK expansion", "artificial antigen presenting cell & NK", "aAPC & NK cell", "G-Rex", "gas-permeable & NK expansion", "wave bioreactor & NK", "rocking bioreactor & NK cell", "static culture & NK expansion", "serum-free & NK cell expansion", "xeno-free & NK cell", "human platelet lysate & NK", "NK MACS", "CellGenix & NK", "GMP-compliant NK expansion", "closed-system & NK cell manufacturing", "automated & NK cell manufacturing", "CliniMACS Prodigy & NK"])}',
        f'{any_of(["cryopreservation & NK cell", "cryopreserved NK cells & cytotoxicity", "freeze-thaw & NK cell", "post-thaw & NK cell potency", "DMSO & NK cell viability", "shelf-life & NK cell product", "formulation & NK cell product", "potency assay & NK cell", "release criteria & NK cell", "critical quality attribute & NK", "comparability & NK cell manufacturing", "vector copy number & NK", "sterility & cell therapy product & NK"])}',
    ],
    # -------------------------------------------------- checkpoints / inhibitory axes
    "checkpoints_inhibitory": [
        f'{any_of(["NKG2A blockade", "monalizumab", "anti-NKG2A", "HLA-E & NK", "KIR blockade", "lirilumab", "IPH2101", "anti-KIR", "TIGIT blockade & NK", "PVRIG", "CD112R", "TIM-3 & NK", "LAG-3 & NK", "PD-1 & NK cell", "CD96", "CD226 & NK", "SIGLEC-7", "Siglec-9 & NK", "NKG2D ligand shedding", "soluble MICA", "MICA shedding", "B7-H6", "PVR & NK", "CD73 & NK cell", "adenosine & NK cell", "prostaglandin E2 & NK", "IDO & NK cell", "TGF-beta blockade & NK"])} AND {CANCER}',
        f'{title_any(["NK cell checkpoint", "inhibitory receptor", "immune checkpoint & NK", "NK cell immune evasion", "resistance to NK cell", "NK cell escape", "MHC class I & NK"])} AND {CANCER}',
    ],
    # -------------------------------------------------- antibody / ADCC combinations
    "adcc_combinations": [
        f'{any_of(["ADCC & NK cell", "antibody-dependent cellular cytotoxicity & NK", "rituximab & NK cell", "trastuzumab & NK cell", "cetuximab & NK cell", "dinutuximab & NK", "obinutuzumab & NK", "Fc engineering & NK", "afucosylated antibody & NK", "CD16 polymorphism & response", "FCGR3A polymorphism", "NK cell & checkpoint inhibitor combination", "NK cells & radiotherapy", "chemotherapy & NK cell function", "lymphodepletion & NK cell persistence", "IL-2 administration & NK cell", "proteasome inhibitor & NK sensitivity", "epigenetic & NK cell ligand", "HDAC inhibitor & NK cell", "EZH2 & NK cell", "bortezomib & NK"])} AND {CANCER}',
    ],
    # -------------------------------------------------- trafficking / solid-tumour TME
    "trafficking_solid_tme": [
        f'{any_of(["NK cell trafficking", "NK cell homing", "NK cell infiltration & solid tumor", "chemokine receptor & NK cell", "CXCR2 & NK cell", "CCR7 & NK cell", "CXCR4 & NK cell", "CXCR3 & NK", "intratumoral NK cell delivery", "intraperitoneal NK cell", "intracranial NK cell", "locoregional & NK cell", "hypoxic tumor microenvironment & NK", "immunosuppressive microenvironment & NK cell", "MDSC & NK cell", "Treg & NK cell suppression", "cancer-associated fibroblast & NK", "extracellular matrix & NK cell infiltration"])} AND {CANCER}',
        f'{NK_TITLE} AND {SOLID} AND {any_of(["microenvironment", "infiltration", "trafficking", "persistence", "resistance", "efficacy", "cytotoxicity", "adoptive transfer"])} AND {CANCER}',
    ],
    # -------------------------------------------------- clinical evidence
    "clinical_nk": [
        f'{NK_TITLE} AND {TRIAL} AND {CANCER}',
        f'{any_of(["adoptive NK cell therapy & patients", "NK cell infusion & patients", "haploidentical NK cell", "CAR-NK & clinical trial", "cord blood CAR-NK & patients", "FT500", "FT516", "FT576", "FT596", "NKX101", "NKX019", "SNK01", "AB-101", "QN-019a", "CYNK-001", "GDA-201", "GTB-3550", "NKG2D CAR-NK & trial", "memory-like NK & patients", "cytokine-induced memory-like NK & AML", "NK cell therapy & safety", "cytokine release syndrome & NK cell therapy", "graft-versus-host & NK cell infusion"])} AND {CANCER}',
    ],
    # -------------------------------------------------- manufacturing/regulatory framing
    "manufacturing_process": [
        f'{NK_TITLE} AND {MANUF} AND {CANCER}',
        f'{any_of(["NK cell manufacturing", "manufacturing of NK cells", "process development & NK cell therapy", "scalable manufacturing & NK", "cost of goods & cell therapy & NK", "supply chain & allogeneic NK", "regulatory & NK cell product", "CMC & NK cell", "master cell bank & NK", "iPSC master line & NK", "clonal iPSC line & NK cell product"])}',
    ],
    # -------------------------------------------------- high-impact sweep
    "sweep_high_impact": [
        f'{journal_any(["Nature", "Science", "Cell", "Cancer Cell", "Nat Med", "Nat Cancer", "Immunity", "Nat Immunol", "Cancer Discov", "Sci Transl Med", "J Clin Invest", "J Exp Med", "Cancer Immunol Res", "J Immunother Cancer", "Clin Cancer Res", "Cancer Res", "Nat Rev Cancer", "Nat Rev Clin Oncol", "Nat Rev Immunol", "Nat Rev Drug Discov", "Cell Rep Med", "Cell Stem Cell", "Sci Immunol", "Blood", "Leukemia", "N Engl J Med", "Mol Ther", "Cytotherapy", "Nat Biotechnol", "Blood Adv", "Signal Transduct Target Ther", "Neuro Oncol"])} AND {NK_TITLE} AND {CANCER}',
    ],
    # -------------------------------------------------- reviews / landscape
    "reviews_landscape": [
        f'{title_any(["NK cell therapy", "natural killer cell therapy", "NK cell-based immunotherapy", "NK cell based cancer immunotherapy", "harnessing NK cells", "NK cells in cancer", "natural killer cells in cancer", "next-generation NK", "engineering NK cells", "clinical translation of NK", "advances in NK cell", "challenges & NK cell therapy"])} AND {CANCER}',
    ],
}

PAGE = 100
SWEEPS = [
    ("modern", WINDOW, 3),
    ("recent", RECENT, 2),
    ("foundational", NODATE, 1),
]


def request_json(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lit-syn/1.0"})
            with urllib.request.urlopen(req, timeout=180) as resp:
                return json.load(resp)
        except Exception as exc:
            sys.stderr.write(f"  retry {attempt}: {exc}\n")
            time.sleep(4 + 4 * attempt)
    return None


def epmc_top_cited(query, pages):
    """Most-cited records first. Europe PMC ignores `page` alongside `sort`, so
    paging has to go through cursorMark."""
    out, hits, cursor = [], 0, "*"
    for _ in range(pages):
        params = urllib.parse.urlencode({
            "query": query, "format": "json", "pageSize": PAGE,
            "resultType": "core", "sort": "CITED desc", "cursorMark": cursor,
        })
        data = request_json(f"{EPMC}?{params}")
        if data is None:
            break
        hits = hits or data.get("hitCount", 0)
        results = data.get("resultList", {}).get("result", [])
        out.extend(results)
        nxt = data.get("nextCursorMark")
        if len(results) < PAGE or not nxt or nxt == cursor:
            break
        cursor = nxt
        time.sleep(0.34)
    return out, hits


def clean(text):
    if not text:
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def venue_of(rec):
    ji = rec.get("journalInfo", {}) or {}
    return (ji.get("journal", {}).get("title", "")
            or ji.get("journal", {}).get("medlineAbbreviation", "")
            or rec.get("journalTitle", "")
            or (rec.get("bookOrReportDetails", {}) or {}).get("publisher", ""))


def ingest(seen, results, domain, sweep):
    new = 0
    for rec in results:
        key = rec.get("pmid") or rec.get("doi") or rec.get("id")
        if not key:
            continue
        if key in seen:
            seen[key]["also_domains"].add(domain)
            continue
        new += 1
        seen[key] = {
            "domain": domain,
            "also_domains": set(),
            "sweep": sweep,
            "pmid": rec.get("pmid", ""),
            "pmcid": rec.get("pmcid", ""),
            "doi": rec.get("doi", ""),
            "title": clean(rec.get("title", "")).rstrip("."),
            "abstract": clean(rec.get("abstractText", "")),
            "authors": rec.get("authorString", ""),
            "venue": venue_of(rec),
            "year": rec.get("pubYear", ""),
            "date": rec.get("firstPublicationDate", ""),
            "isOA": rec.get("isOpenAccess", "N"),
            "inEPMC": rec.get("inEPMC", "N"),
            "cited": rec.get("citedByCount", 0),
            "pubType": (rec.get("pubTypeList", {}) or {}).get("pubType", []),
            "src": rec.get("source", ""),
        }
    return new


def main():
    seen = {}
    log = open(LOG, "a")
    for domain, queries in QUERIES.items():
        for i, q in enumerate(queries):
            for sweep, scope, pages in SWEEPS:
                results, hits = epmc_top_cited(f"({q}) AND {scope}", pages)
                new = ingest(seen, results, domain, sweep)
                msg = (f"{sweep:12s} {domain}[{i}]: hits={hits} "
                       f"fetched={len(results)} new={new} total={len(seen)}\n")
                sys.stderr.write(msg)
                log.write(msg)
                log.flush()
                time.sleep(0.34)

    out = []
    for v in seen.values():
        v["also_domains"] = "|".join(sorted(v["also_domains"]))
        v["pubType"] = "|".join(v["pubType"]) if isinstance(v["pubType"], list) else str(v["pubType"])
        out.append(v)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=0)
    print(f"total unique records: {len(out)}")
    log.write(f"total unique records: {len(out)}\n")
    log.close()


if __name__ == "__main__":
    main()
