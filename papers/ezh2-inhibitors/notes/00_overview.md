# EZH2 inhibitors — literature synthesis (potency, BBB penetration, data)

Scope: small-molecule inhibitors of EZH2 (and dual EZH1/2 inhibitors, plus the
allosteric EED inhibitors that block the same PRC2 complex), spanning
first-disclosure medicinal chemistry, preclinical efficacy, and clinical data.
Organized **by compound**, with cross-cutting buckets for **CNS/blood-brain-barrier
(BBB) penetration**, **resistance/selectivity/SAR**, and **combinations/clinical**.
Emphasis, per request: **potency**, **BBB penetration**, and **the underlying data**
(preclinical + clinical).

## Why this matters for this repo
EZH2/PRC2 is the writer of H3K27me3. In the CNS tumors this repo tracks, PRC2 is a
central node: **H3K27M** diffuse midline glioma (DMG/DIPG) globally erases
H3K27me3 yet retains focal PRC2 dependence; **H3G34** hemispheric glioma perturbs
H3K36/K27 crosstalk; **SMARCB1/INI1-deleted ATRT** and rhabdoid tumors are the
archetypal EZH2-dependent CNS cancers. So for these indications the decisive
questions are not only "is the compound potent and selective" but **"does it cross
the blood-brain barrier at a free concentration sufficient to deplete H3K27me3 in
tumor?"** That BBB question is the weakest link for the approved agents and the
main differentiator among the newer ones.

## Corpus at a glance
- **148 curated papers** across **12 buckets** (`index.tsv`), years **2012–2026**.
- **104 open-access full texts** mirrored locally under `fulltext/` (`✓FT` in `REPORT.md`).
- **18** papers explicitly tagged CNS/BBB (glioma, DIPG/H3K27M, ATRT, brain
  metastasis); **20** reviews.
- Buckets: tazemetostat (34), valemetostat (22), GSK126/GSK343 (9), SHR2554 (9),
  UNC1999/EED226 (7), EPZ005687/EI1/EPZ011989 (4), DZNep (3),
  tulmimetostat/CPI-0209 (1) and mevrometostat/PF-06821497 (1) — thin because
  their drug names rarely appear in *titles*; both are discussed in the notes and
  captured in the combination/clinical bucket — plus CNS/BBB (12),
  resistance/SAR (20), combinations/clinical (26).

## The compound landscape (one-line each)
| Agent | Sponsor | Target | Status | Headline potency | Brain penetration |
|---|---|---|---|---|---|
| **Tazemetostat** (EPZ-6438) | Epizyme/Ipsen | EZH2 (SAM-competitive) | **FDA-approved** (epithelioid sarcoma 2020; FL EZH2-mut 2020) | Ki ≈ 2.5 nM; ~35× vs EZH1 | **Poor** — P-gp/BCRP substrate; low/variable CNS exposure |
| **Valemetostat** (DS-3201) | Daiichi Sankyo | **dual EZH1/2** | **Approved in Japan** (R/R ATL 2022; PTCL 2024) | low-nM vs both EZH1 & EZH2 | Reported **more brain-penetrant**; active in CNS-adjacent models |
| **Tulmimetostat** (CPI-0209) | Constellation/MorphoSys | EZH2 (2nd-gen, long residence) | Phase 1/2 | low-nM, extended target residence | limited public CNS PK |
| **Mevrometostat** (PF-06821497) | Pfizer | EZH2 | Phase 3 (mCRPC, +enzalutamide) | low-nM | designed for improved PK; CNS data limited |
| **SHR2554** | Jiangsu Hengrui | EZH2 | Phase 1/2 (China, lymphoma) | low-nM | not established as CNS-penetrant |
| **GSK126** (GSK2816126) | GSK | EZH2 (SAM-competitive) | Phase 1 (terminated — PK/exposure) | Ki ≈ 0.5–3 nM; ~150× vs EZH1 | poor solubility/exposure; not CNS-optimized |
| **GSK343 / GSK503 / GSK926** | GSK | EZH2 | tool compounds | low-nM (cellular) | tool use only |
| **EPZ005687 / EI1 / EPZ011989** | Epizyme/Novartis | EZH2 | tool / early | Ki ≈ 24 nM (EPZ005687); EPZ011989 orally active | EPZ011989 has **some brain exposure** in mice |
| **UNC1999** | SGC/UNC | **dual EZH1/2** | tool | IC50 <10 nM (EZH2), ~45 nM (EZH1) | oral tool; limited CNS data |
| **EED226 / MAK683 / A-395** | Novartis/SGC | **EED** (allosteric, H3K27me3-pocket) | MAK683 in trials | low-nM; overcomes some EZH2i resistance | designed to bypass SAM-site resistance |
| **DZNep** | (academic) | SAH-hydrolase → indirect PRC2 depletion | tool | non-specific | crosses BBB but non-selective/toxic |

(Values are canonical medicinal-chemistry/first-disclosure figures; see
`01_potency_selectivity.md` for sources and caveats.)

## Five takeaways
1. **Potency is largely solved; selectivity and mechanism differ.** All modern
   agents are SAM-competitive and low-nanomolar on PRC2. The meaningful axes are
   **EZH2-selective (tazemetostat, GSK126, mevrometostat) vs dual EZH1/2
   (valemetostat, UNC1999)** and **catalytic-site vs allosteric-EED (EED226,
   MAK683)**. Dual EZH1/2 inhibition matters where EZH1 compensates
   (e.g., quiescent/stem-like and some CNS contexts).
2. **BBB penetration is the real bottleneck for brain tumors.** Tazemetostat is a
   **P-gp/BCRP efflux substrate with poor, variable CNS exposure** — a recurring
   caveat in the DIPG/ATRT literature and the reason single-agent CNS activity has
   been modest. Valemetostat and several next-generation/tool compounds
   (EPZ011989) report better brain exposure; **verified free-brain PK in humans
   remains sparse** for every agent.
3. **The clinical wins are extracranial.** Approvals/robust responses are in
   **EZH2-mutant follicular lymphoma**, **INI1/SMARCB1-deficient epithelioid
   sarcoma** (tazemetostat), and **ATL/PTCL** (valemetostat). CNS tumor activity
   is still largely **preclinical or early-phase**.
4. **Synthetic lethality drives target selection.** The strongest preclinical
   rationale is **SWI/SNF loss** (SMARCB1/INI1 in ATRT & epithelioid sarcoma;
   ARID1A, PBRM1, SMARCA4) and **gain-of-function EZH2 mutations** (Y641, A677,
   A687) in lymphoma. In DMG/DIPG the dependency is more context-specific and often
   requires **combinations** (HDACi, ONC201/DR5, glutamine metabolism).
5. **Resistance is a live problem.** Acquired **secondary EZH2 SET-domain
   mutations** and PRC2-independent escape drive interest in **EED allosteric
   inhibitors** and **EZH2 degraders/PROTACs**, well represented in the
   resistance/SAR bucket.

## How it was built
`harvest.py` queries Europe PMC per compound (and per theme), `curate.py` keeps
only EZH2/PRC2-inhibitor records and assigns each to one bucket (named agent >
theme), `fetch_fulltext.py` mirrors OA XML, and `gen_report.py` writes
`REPORT.md`. Bucket assignment is a title/abstract heuristic — thin drug buckets
(CPI-0209, PF-06821497) reflect naming in titles, not clinical importance.
Re-run in order: `harvest` → `curate` → `fetch_fulltext` → `gen_report`.

See:
- `01_potency_selectivity.md` — biochemical/cellular potency, PRC2 mechanism, selectivity.
- `02_bbb_penetration.md` — BBB/CNS exposure per agent, efflux, intracranial efficacy.
- `03_clinical_data.md` — trials, approvals, response rates, safety.
- `04_preclinical_efficacy_and_combinations.md` — models, synthetic lethality, combos, resistance.
