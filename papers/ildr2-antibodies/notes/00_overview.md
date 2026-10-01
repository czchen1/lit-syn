# ILDR2 antibodies: overview

## What ILDR2 is, and why it is an antibody target

**ILDR2** (immunoglobulin-like domain containing receptor 2) is a type I transmembrane protein encoded by `ILDR2` / `C1orf32` on human chromosome 1q23–25. It carries an N-terminal signal peptide, a single extracellular **Ig V-set (IgV) domain** (~167 aa), a 20-aa transmembrane segment, and a long (~433-aa) intracellular tail (full length 639 aa) (PMID 34639059). Its paralogs are **ILDR1** and **LSR** (lipolysis-stimulated lipoprotein receptor, also called ILDR3 / angulin-1); together the three are the **"angulin" family** of tricellular-tight-junction proteins (PMID 23239027, 28785060).

ILDR2 sits at the intersection of two literatures, and the gene's tangle of aliases is the main source of confusion:

| Alias | Origin | Note |
| --- | --- | --- |
| **ILDR2** | HGNC symbol | current standard |
| **C1orf32** | chromosome-1 ORF | seen in genomics tables |
| **LISCH-like** | "LISCH7-like" | named for sequence similarity to LISCH7/LSR; this is the mouse diabetes-modifier name (PMID 18654634) |
| **angulin-3** | tricellular-junction nomenclature | used in the tight-junction / kidney literature (PMID 38311119, 39640577) |

> **Caution — LISCH7 ≠ ILDR2.** `LISCH7` is the older name for **LSR** (angulin-1), a *different* gene. PubMed queries for "LISCH7" return LSR/colon-cancer/TNBC papers that are **not** about ILDR2; these are excluded here (see below).

Two discoveries made ILDR2 an antibody target:

1. **ILDR2 is a B7-family immune checkpoint.** In 2018 ILDR2 was independently described as a novel **B7-like protein with robust T-cell inhibitory activity** (PMID 29431694). Its extracellular IgV domain shares ~24–36% sequence homology with other B7 members and binds a (still incompletely defined) counter-receptor on activated T cells. This is what makes ILDR2 druggable with antibodies in the same conceptual class as PD-1/PD-L1, CTLA-4, B7-H3, etc.
2. **The axis is bidirectionally drug-able.** Because ILDR2 *delivers an inhibitory signal*, you can either **mimic/engage** it (an ILDR2-Fc decoy → immune suppression / tolerance for autoimmunity) or **block** it (an antagonist anti-ILDR2 mAb → relief of T-cell suppression for oncology).

## The corpus at a glance

- **21 included papers** (2008–2026): **7 `core`** (antibodies / Fc biologics / checkpoint biology) + **14 `context`** (target biology).
- **3 distinct antibody/biologic programs** appear in the corpus:
  - **ILDR2-Fc fusion protein** (Compugen): discovery + tolerance papers, PMID 29431694, 29431690.
  - **BAY 1905254** antagonist anti-ILDR2 hIgG2 mAb (Bayer): PMID 32312711.
  - **Research/tool monoclonal antibodies** against mouse ILDR2 and against angulin-3/ILDR2 used for tissue detection: PMID 39626366 (anti-mouse-ILDR2 mAb), PMID 38311119 (anti-angulin-3 mAb).
- **12/21 PDFs** archived locally; the remainder are paywalled or reCAPTCHA-blocked (see `README.md` download note).

### Era timeline

- **2008** — `ILDR2` is positionally cloned as **"Lisch-Like"**, a candidate type-2-diabetes modifier on distal mouse Chr1 affecting β-cell mass (PMID 18654634). The earliest functional frame is metabolic, not immune.
- **2013–2017** — ILDR2 is characterized as an ER-resident regulator of hepatic lipid homeostasis (PMID 23826244) and, separately, as an **angulin** tricellular-tight-junction protein (PMID 23239027, 28785060). Interactome work identifies ZNF70 (PMID 27353377).
- **2018 — the immune-checkpoint inflection.** Two back-to-back `J Immunol` papers define ILDR2 as a B7-like T-cell inhibitor (PMID 29431694) and show that **ILDR2-Fc** induces durable antigen-specific tolerance in EAE, NOD type-1 diabetes, and a minor-mismatch bone-marrow-transplant model (PMID 29431690). A negative-control metabolism paper (PMID 29847571) walks back the earlier hepatic-steatosis claim.
- **2020 — the oncology antibody.** Bayer reports **BAY 1905254**, a human/mouse/monkey cross-reactive anti-ILDR2 hIgG2 antagonist that blocks ILDR2's immunosuppression and shows efficacy across syngeneic tumor models, correlating with mutational load and synergizing with anti-PD-L1 and chemo (PMID 32312711).
- **2021–2025** — ILDR2 is folded into B7-family reviews (PMID 33800752, 34639059), profiled in disease tissue (PMID 37665469), tied to protein-stability chaperones GRP78/PDIA1 (PMID 33863978), and shown to mark a tolerogenic CD206hi macrophage subset in sublingual mucosa via a new anti-mouse-ILDR2 mAb (PMID 39626366). In parallel the angulin-3 / kidney-podocyte thread matures (PMID 38311119, 39640577) along with tight-junction structure work (PMID 40928054).

## Inclusion / exclusion decisions

**Included (21):** any paper in which ILDR2 itself is a subject of study — the checkpoint/antibody papers, plus the angulin-3 tight-junction, interactome, structure, and diabetes/metabolism papers that define the target.

**Excluded (21):** the PubMed union also returned papers that are *not* about ILDR2:

- **LISCH7 / LSR (a different gene; 6 papers):** PMID 11402317, 15731461, 17975147, 18456845, 32048750, 34238140 — these concern LSR/angulin-1 ("LISCH7") in p53 signaling, hypertension, and colon/triple-negative-breast cancer.
- **Incidental gene-list / omics mentions (15 papers):** PMID 24212375, 27034888, 28709640, 29494550, 32661289, 36147669, 36557314, 36530149, 37325559, 38437001, 40003915, 41285811, 41518986, 41865132, 42137783 — `ILDR2`/`C1orf32` appears only inside a differential-expression table, GWAS region, proteomics hit list, or methods dataset, without being studied.

The full excluded list with one-line reasons is reproduced in `REPORT.md`.

## Conventions used in this collection

- Each `index.tsv` row's `relevance` is `core` or `context`; `category` is `primary_research`, `review`, or `methods`.
- PDF filenames are `{firstauthor}_{year}_pmid{PMID}.pdf`.
- `status` records provenance: `downloaded_<source>` for archived PDFs; `not_available_oa …` or `free_at_publisher_pmc; blocked_recaptcha` for the rest.
