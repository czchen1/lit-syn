# 00 — Overview: LNP delivery of novel cancer payloads

## What this collection is about

The clinical success of LNP-mRNA (Onpattro siRNA-LNP, then the COVID-19 vaccines) established the lipid nanoparticle as a manufacturable, re-dosable, non-integrating delivery vehicle for nucleic acids. This collection tracks the wave of work that followed, in which LNPs are used **not to vaccinate against a tumour antigen, but to deliver a functional genetic payload that does therapeutic work inside the patient** — generating CAR cells in situ, expressing toxic cytokines only where they are needed, secreting bispecific engagers from the liver, restoring lost tumour suppressors, or carrying genome-editing machinery to a tumour. The 157 curated papers (2008–2026) span twelve payload buckets and are dominated (>80 papers) by 2024–2026 work, reflecting how recently this field has exploded.

## Payload taxonomy and counts

Topic tags are multi-label (a single paper can co-encode a cytokine and a suicide gene); counts below are tag occurrences across the 157 papers. The `category` column in `index.tsv` records the single primary bucket.

| Payload bucket | Papers (tagged) | Representative encoded payload |
|---|---|---|
| LNP engineering / targeting | 72 | ionizable-lipid libraries, organ- & cell-targeting (payload-agnostic) |
| Cytokine / immunomodulator | 55 | IL-12, IL-15, IL-18, IFN-α/γ, OX40L+IL-23+IL-36γ |
| Gene editing | 46 | Cas9 mRNA+sgRNA, base/prime/RNA editors, RNP |
| TF / reprogramming | 30 | BATF, IRF8, NIK, β-catenin, M2→M1 macrophage |
| Tumour-suppressor restoration | 25 | p53, PTEN, p21, LATS1, NDRG2 mRNA |
| Antibody / engager | 23 | BiTE, macrophage engager, nanobody-BiTE |
| In vivo / in situ CAR | 19 | CAR-T, CAR-macrophage, CAR-NK mRNA |
| Circular RNA / cssDNA | 9 | circ-IL-12, circ-CD-UPRT, cEMSY, cssDNA |
| Self-amplifying / replicon / saRNA | 9 | srRNA-IL-12, alphavirus VLV, RNAa p21/NKX3-1 |
| Suicide gene / prodrug enzyme / toxin | 8 | cytosine deaminase-UPRT, gasdermin |
| Clinical-stage tags | 7 | mRNA-2752, MTS105 (GPC3 TCE), NTLA-class |
| Review / perspective | 9 | in vivo CAR landscape, circRNA immunology |

## Eras

- **2008–2013 (5 papers): RNA-activation prehistory.** The earliest LNP "novel payload" cancer work is small-activating RNA (RNAa): lipidoid-formulated dsRNA inducing endogenous *p21* (Place 2012, PMID 23343884) and *NKX3-1* (Ren 2013, PMID 23836514) in prostate xenografts, plus an intravesical bladder-tumour saRNA model (Kang 2012, PMID 22872227). These established intratumoural/intravesical lipid delivery of gene-*activating* nucleic acids years before mRNA therapeutics matured.
- **2018–2022 (15 papers): replicon and proof-of-concept mRNA payloads.** Self-replicating RNA-LNP encoding IL-12 for intratumoural and then systemic dosing (Li 2020 *Nat Cancer* PMID 34447945; Wang 2024 PMID 38548896), and the first in situ CAR-T LNP demonstrations.
- **2023–2026 (137 papers): the explosion.** In vivo CAR (T and macrophage), organ-targeted engagers, tumour-suppressor mRNA replacement, CRISPR-LNP against solid-tumour drivers, saRNA/circRNA cytokine platforms, and ML-designed extrahepatic lipids. 102 of 157 papers are from 2025–2026.

## Recurring design themes

1. **Transient, re-dosable, non-integrating expression is a feature, not a bug.** Across in vivo CAR (notes/01) and cytokine work (notes/02), authors repeatedly frame transient mRNA expression as a safety advantage — limiting cytokine-release syndrome and on-target/off-tumour toxicity relative to durable engineered cells. A minority deliberately move to integration (minicircle DNA + SB100x transposase, Bimbo 2025, PMID 40659448) when durability is needed.
2. **Localising a toxic payload is the central problem.** IL-12 and IL-12-class cytokines recur because they are potent but historically too toxic systemically; nearly every cytokine paper is really a *delivery/localisation* paper — intratumoural injection, liver-restricted secretion, β-glucan/macrophage "Trojan-horse" homing, prodrug-tethered lipids, or replicon amplification to lower the dose.
3. **Cell- and organ-targeting via surface ligands.** Antibody/nanobody-decorated LNPs (anti-CD5, anti-CD3, anti-CD7, anti-CD8, VHH) for T-cell or macrophage tropism (notes/01, notes/08), and SORT-style / chemistry-driven organ selection (lung "tripod" lipids, spleen-tropic, fluorinated lipids, GLUT1/mannose brain targeting) appear in the majority of 2025–2026 papers.
4. **Co-delivery and combination.** Single-particle co-encapsulation of two mRNAs (engager + cytokine), mRNA+siRNA (PTEN mRNA + PARP1 siRNA), Cas9 mRNA + multiple sgRNAs, and pairing with checkpoint blockade (anti-PD-1/PD-L1) or chemotherapy is now standard.
5. **Beyond linear mRNA.** Self-amplifying RNA, circular RNA, and circular ssDNA are pursued for higher/longer expression at lower dose and lower innate immunogenicity (notes/06).

## Translational status

Most of the corpus is preclinical (mouse, with some NHP PK/tox). The clearest clinical anchors are **mRNA-2752** (LNP-mRNA encoding OX40L+IL-23+IL-36γ, intratumoural ± durvalumab; phase 1 NCT03739931, 134 patients, 17.9% ORR in CPI-resistant melanoma; Sweis 2026, PMID 42149124) and **MTS105** (LNP-delivered, liver-targeted GPC3 T-cell-engager mRNA with NHP PK and a first-in-human study underway; Huang 2025, PMID 41397962). In vivo CAR-T is the most active translational frontier, with multiple 2025 ASH-meeting reviews (notes/01) cataloguing LNP, VLP, and non-viral-DNA programs moving toward the clinic, building on the NTLA-class CRISPR-LNP precedent.

## Conventions

Papers are cited as *First-Author Year (PMID)*. `index.tsv` is the canonical metadata table; `status` indicates whether an OA PDF (`pdfs/`), Europe PMC XML (`fulltext/`), or metadata-only record backs each entry. See `09_per_paper_extractions.md` for one capsule per paper.
