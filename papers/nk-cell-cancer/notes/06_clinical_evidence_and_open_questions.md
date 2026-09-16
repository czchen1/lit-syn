# Clinical evidence, and what would change the argument

## What patients have actually shown

**Safety is the settled claim.** No GvHD and little or no CRS/ICANS across allogeneic, cord-blood, iPSC-derived,
engineered and cell-line products, including CD19 CAR-NK (PMID 32023374, PMID 38238616), iPSC-derived FT596
(PMID 39798981), 4-1BB-costimulated CD19 CAR-NK (PMID 40251398) and intracranial HER2 CAR-NK-92
(PMID 37148198); the 2025 landscape review catalogues 120+ CAR-NK trials (PMID 40149002).

**Efficacy signals cluster where three things coincide:** a haematological target, an armoured or
memory-like-programmed product, and real lymphodepletion.

| Product | Setting | What it establishes |
|---|---|---|
| Haploidentical PB-NK + IL-2 | AML, non-transplant | in vivo expansion and remissions require lymphodepletion (PMID 15632206); Treg depletion raised expansion 10%→27% with better clearance (PMID 24719405) |
| KIR-ligand-mismatched NK | elderly high-risk AML | feasible, no GvHD, CR in active disease (PMID 21791425) |
| CB-derived CAR19/IL-15 NK | r/r CD19+ B-cell malignancies | phase 1/2 (PMID 32023374), then 37 patients with determinants of response (PMID 38238616) — the reference dataset for armoured CAR-NK |
| CD19-BBz CAR-NK (BaEV-transduced CB) | r/r large B-cell lymphoma | repeat dosing is feasible and tolerable (PMID 40251398) |
| FT596 (iPSC; CD19 CAR + hnCD16 + IL-15/IL-15Rα) | B-cell lymphoma | a multiplex-engineered iPSC product can be dosed in humans (PMID 39798981) |
| Donor CIML NK | post-transplant relapse | memory-like programming expands and persists in patients (PMID 35349491; original AML trial PMID 27655849) |
| CIML NK + N-803 ± ipilimumab | r/r head and neck cancer | the most credible solid-tumour attempt: state programming + cytokine support + checkpoint blockade (PMID 39948608) |
| AFM13-precomplexed CB-NK | CD30+ lymphoma refractory to brentuximab **and** checkpoint inhibitors | engager-loaded cells can work without any gene transfer (PMID 40186077) |
| TRACK NK (CB, sIL-15, PD-L1+) | checkpoint-refractory NSCLC | interim engineered-NK solid-tumour data (PMID 39903538, PMID 38572955) |
| NK-92 / CAR-NK-92 | RCC, melanoma, recurrent GBM | safe at high doses; locoregional delivery is viable (PMID 18836917, PMID 24094496, PMID 37148198) |
| Autologous SNK01 + chemo/cetuximab | NSCLC after TKI failure | autologous route is feasible but starts from impaired cells (PMID 38538093) |

**Solid tumours remain largely unsolved**, and the two least-negative examples both added something beyond "more
NK cells": intracranial delivery that bypasses trafficking (PMID 37148198), and combined state programming plus
cytokine support plus checkpoint blockade (PMID 39948608).

## Ranked by strength of *clinical* evidence

1. IL-15 armouring or IL-15-containing engagers — in essentially every product with a clear response signal.
2. Lymphodepletion plus Treg control — oldest, best-quantified, and free (PMID 24719405).
3. Memory-like programming — clinical expansion/persistence in two settings.
4. Donor/education selection — outcome associations in transplant cohorts (PMID 20581313, PMID 30647027).
5. Protected/high-affinity CD16 plus an antibody or engager — mechanistically strong, now inside clinical products.
6. Brake knockouts — compelling preclinically, clinical readouts immature.
7. Route of administration for solid tumours — one positive locoregional trial.

## What is genuinely unresolved

- **No qualified potency assay**, so "the product met specification" does not imply potency, and cross-trial
  comparison of NK activity is unsound (`05_potency_and_release.md`).
- **Persistence still measured in weeks.** Cell-intrinsic IL-15 helps; nothing approaches CAR-T-like durability,
  and repeat dosing is the current pragmatic answer (PMID 40251398).
- **No head-to-head manufacturing comparison** on shared donors with one potency readout: feeder vs PM21 vs
  feeder-free, static vs bioreactor, DMSO vs DMSO-free.
- **Multi-edit safety science lags the edit lists** that screens are now generating (PMID 41425600 vs
  PMID 40845844, PMID 38918616).
- **Solid-tumour TME resistance** — hypoxia, TGF-β, lactylation, nutrient competition, CAF decoys, and functional
  impairment within hours of tumour entry (PMID 38267402) — is the bottleneck, and no clinical product yet
  carries the full resistance package.
- **Cost of goods is essentially unreported**, despite being the main argument for allogeneic and iPSC platforms.

## What would change the argument in these notes

- A trial in which an unarmoured product matched an armoured one → IL-15 is not the dominant lever, and the
  ranking above collapses.
- A cryopreserved product showing preserved 3-D function with standard DMSO → failure mode #2 downgrades to a
  formulation detail.
- A solid-tumour response driven by a novel CAR target alone → antigen choice deserves more investment than
  argued in `00_thesis_and_decision_frame.md`.
- Multi-month persistence from a cell-intrinsic circuit → the "repeat dosing" default is wrong, and edit-count
  economics change with it.
- A head-to-head platform comparison showing feeder-free yield parity → the feeder CMC burden becomes
  indefensible.

## Honest limits of this collection

Axis, evidence class, disease tag and manufacturing/engineering flags are title/abstract-level heuristics, useful
for navigation and not a substitute for reading. Citation counts are Europe PMC's and are time-biased against
2025–2026 records. Per-axis quotas mean the corpus is deliberately balanced across topics rather than
proportional to publication volume — clinical and process evidence are over-weighted relative to the raw
literature on purpose. Anything not resolvable from an abstract was checked against the 153 mirrored open-access
full texts where available; the remaining records are catalogued from metadata only.
