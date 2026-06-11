# GD2 CAR-T literature synthesis

Curated collection of published literature on **GD2-targeted CAR-T cell therapies**, with an explicit focus on **CAR design, genetic construction, and manufacturing** (rather than clinical outcomes alone). Includes commentary extracted from main texts and from supplementary materials wherever available.

## Scope

This collection is restricted to studies in which GD2 (disialoganglioside, or its O-acetyl variant OAcGD2) is targeted by an engineered cellular product carrying a chimeric antigen receptor — i.e. CAR-T, CAR-NKT, CAR-NK, CAR-γδT, CAR-macrophage, CAR-microglia, CAR-MSC, CAR-iPSC-derived effectors. Studies of the unconjugated ch14.18 / dinutuximab / naxitamab antibodies (without engineered cells) are excluded.

## Directory structure

- `index.tsv` — curated paper metadata for all 204 papers identified, with topic tags, download status, and DOI/PMID/PMCID links.
- `index_by_lab.tsv` — the GD2 CAR-effector **clinical trials indexed by originating lab/group** (product, construct, cell type, safety switch, registration ID, disease, route, key papers, local supplements).
- `protocols/clinicaltrials_gov/` — archived ClinicalTrials.gov protocol records (JSON) for the registered trials (eligibility, arms/interventions, lymphodepletion, dose levels, outcome measures).
- `pdfs/` — open-access PDFs of main texts (151 papers).
- `supplements/` — extracted PDF/DOCX supplementary materials (122 files across 97 papers), trimmed to text/protocol-relevant content (≤30 MB per paper). The full original Europe PMC supplementary zips were unpacked and pruned of large raw data files (videos, sequencing data, multi-GB image stacks) so the repository remains tractable.
- `notes/` — synthesis reports extracting design, construction, and manufacturing commentary, organized by topic.

## Notes index

- `notes/00_overview.md` — landscape, paper counts, eras, and conventions used in this collection.
- `notes/01_car_architecture.md` — scFv (14g2a, hu14.18, 3F8, K666, 8B6 etc.), extracellular spacer/hinge, transmembrane, costimulatory and signaling endodomains, generations, and the trade-offs reported across papers.
- `notes/02_gene_delivery.md` — gamma-retroviral (SFG/MSGV), lentiviral, and non-viral platforms (mRNA electroporation, sleeping-beauty / piggyBac transposon, CRISPR-Cas9 HDR/HITI knock-in to TRAC, mRNA-LNP in situ).
- `notes/03_cell_sources.md` — autologous PBMC bulk T cells, CD4/CD8-selected products, naive/TSCM enrichment, virus-specific T cells, Vα24-invariant NKT cells, γδT cells, NK cells, iPSC-derived effectors, allogeneic and donor-derived products, MSCs, macrophages, and microglia.
- `notes/04_manufacturing.md` — apheresis and selection, T-cell activation reagents (OKT3, anti-CD3/CD28 beads, TransAct, K562-based aAPCs, αGalCer-LCLs), expansion cytokines (IL-2 vs IL-7+IL-15 vs IL-21), exhaustion-mitigating additives (dasatinib, AKT inhibitor), closed-system platforms (CliniMACS Prodigy, Lonza Cocoon, G-Rex), GMP reagents and release testing, manufacturing timelines and yields.
- `notes/05_safety_engineering.md` — inducible-caspase 9 / rimiducid, RQR8, EGFRt, HSV-TK, and CD20-epitope safety switches; affinity-tuning to spare healthy tissue; constrained costimulation-only "1G" CARs; SUPRA / antibody-coupled CARs.
- `notes/06_cytokine_armoring.md` — TRUCKs and armored CARs: constitutive or inducible IL-15, IL-18 (Glienke), IL-7Rα C7R (Heczey 2017+), IL-21, CCL19/IL-7 (Cytomicrocosm), CCR2b/CXCR2 chemokine-receptor co-arming.
- `notes/07_logic_and_switchable.md` — synNotch AND-gates (B7-H3 → GD2), SUPRA / DARPin switches, bispecific tandem CARs, antigen-density-gated CARs, KIR-based NOT gates, dual-CAR designs.
- `notes/08_clinical_formulation.md` — lymphodepletion regimens (Cy/Flu doses), routes (IV vs ICV vs intratumoral), dose levels, fractionated dosing, redosing, and bridging therapy across the 14 GD2 CAR-T clinical trials catalogued.
- `notes/09_per_paper_extractions.md` — capsule entries per primary paper summarizing the construct, vector, cell source, activation/transduction/expansion protocol, safety engineering, and notable manufacturing observations.
- `notes/10_trial_index_by_lab.md` — narrative index of every published GD2 CAR-effector clinical trial grouped by lab/group (Baylor CAGT, Bambino Gesù, Stanford, UCL/GOSH, Chang/4SCAR, Adelaide CARPETS, Children's Mercy), with registration IDs and key papers; human-readable companion to `index_by_lab.tsv`.
- `notes/11_clinical_management_plan.md` — comprehensive clinical-management plan with a **per-section comparison table across trials**: patient selection, bridging, lymphodepletion, dose/route/DLT, CRS, ICANS vs TIAN, the TIAN algorithm, on-target neuropathic pain, IL-15 hyperleukocytosis, safety-switch activation, premedication, hematologic toxicity, ICV/device management, redosing, and long-term follow-up; ends with a distilled cross-trial best-practice protocol.

## Identification strategy

Five complementary PubMed E-utils queries were combined and deduplicated:

1. `("GD2" OR "disialoganglioside") AND ("CAR-T" OR "CAR T" OR "chimeric antigen receptor")`
2. `"anti-GD2" AND ("CAR" OR "chimeric")`
3. `"GD2.CAR" OR "GD2-CAR"`
4. `"GD2"[Title] AND ("CAR" OR "CAR-T" OR "chimeric"[Title])`
5. `("GD2") AND ("CAR-NKT" OR "CAR-T" OR "CAR T cell")`

371 candidate records were retrieved (June 2008–February 2026). Manual filtering removed papers about the ch14.18 / dinutuximab antibody used without engineered cells, leaving 204 GD2-CAR effector papers. PMC IDs were resolved via NCBI E-utils and the PMC ID converter; PDFs were retrieved from Europe PMC OA, NCBI PMC (with a real browser to bypass the JavaScript proof-of-work challenge on author-manuscript PDFs), and Unpaywall. Publisher-direct attempts were made for major paywalled papers (Nature, Nature Medicine, NEJM, Science Translational Medicine, Cancer Cell, Cell, AACR). Three Nature Medicine papers (Heczey 2020, Heczey 2023, Quintarelli 2025) yielded peer-reviewed supplementary PDFs only (`supplements/*_supp.pdf`) because the typeset article is paywalled.

## Coverage summary

- 204 unique papers in `index.tsv` (14 clinical trials, 125 primary research, 10 preprints, 43 reviews, 12 editorials/letters/errata).
- 151 main-text PDFs in `pdfs/` (~ 560 MB).
- 122 supplementary files extracted across 97 papers in `supplements/` (~ 126 MB after pruning).
- ≈53 paywalled / non-OA papers are listed in `index.tsv` with DOIs/PubMed links but no local PDF; design/construction/manufacturing details for these are captured from their abstracts and from preprints, conference reports, related supplements, and authoritative reviews where possible.

The downloaded set covers every major preclinical lineage paper and every published GD2 CAR-T clinical trial (Pule 2008/Louis 2011, Yu 2012, Heczey 2017, Straathof 2020 STM, Heczey 2020 NM CAR-NKT, Heczey 2023 NM CAR-NKT-15, Del Bufalo 2023 NEJM GD2-CART01, Majzner 2022 / Monje 2025 H3K27M-DMG, Locatelli 2025 NB phase 1/2, Li 2025 long-term follow-up, Gargett 2024 melanoma, Tian 2025 CAR-NKT IL-15, Quintarelli 2025 donor-derived allogeneic). The four trial papers that exist only as paywalled main texts (Straathof 2020, Del Bufalo 2023, Heczey 2020/2023) are captured via their construct lineage papers, supplementary methods, and trial-companion preclinical articles already included in the collection.
