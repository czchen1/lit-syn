# Cryopreservation, potency assays and product release

Off-the-shelf NK therapy requires cryopreserved product. The evidence says this is a **potency problem**, not a
logistics problem — and that the standard release assays hide it.

## Cryopreservation damages the functions that matter most

- **Mark et al. (2020, PMID 33067467)** is the pivotal result: standard degranulation and chromium-release assays
  confirmed that cryopreserved NK cells still kill, yet the same cells showed markedly impaired **3-D migration
  and cytotoxicity in tissue-like matrices** (earlier preprint of the same work at bioRxiv). A product that
  passes a 2-D potency assay can be functionally inert in tissue.
- Head-to-head comparison of fresh versus cryopreserved/thawed clinical-grade expanded NK cells confirms
  measurable functional loss (PMID 32536506).
- Mechanistic work in 2025–2026 localises the damage: lysosomal damage triggering programmed cell death, which
  induced stress granules can alleviate (PMID 42098076), and composition/temperature/granule-dependent
  post-thaw survival and function (PMID 42564981). A dedicated study of cryopreservation damage mechanisms in NK
  cells appeared in Cytotherapy (PMID 39918490).

## Reducing or replacing DMSO

DMSO is both the standard cryoprotectant and a source of dose-dependent infusion toxicity.

- Systematic evaluation of DMSO/Me₂SO, proline, trehalose and dextran-40 combinations for NK cells
  (PMID 41208818).
- DMSO-free formulations benchmarked against CryoStor 10 and FBS+DMSO for recovery and function
  (PMID 42098076; PMID 42564981).
- **Intracellular nanoparticle-mediated protection** avoids cryoinjury while retaining antitumour function
  (PMID 32382476) — a route that changes the cell rather than the buffer.
- Post-thaw **rescue** rather than prevention: brief co-culture with effector T cells or synthetic cells restores
  motility and killing after thaw (PMID 40966444).

## Cryopreservation of complex products

- Cord-blood-derived NK cells expanded from long-term cryopreserved units remain cytotoxic against primary breast
  cancer cells (PMID 29189387), and selective-thaw devices let a banked unit serve both transplant and NK
  manufacture (PMID 26432560).
- Cryopreserved NK cells retain activity against leukaemic targets, with IL-2 co-application affecting the result
  (PMID 27614454).
- **Engager-loaded cells can be frozen as a complex**: NK cells pre-complexed with innate cell engagers retain
  activity and specificity after cryopreservation (PMID 35225870) — the enabling result for off-the-shelf
  AFM13-NK logistics (PMID 40186077).
- Clinical NK-92 manufacturing has published expansion **and** cryopreservation conditions together
  (PMID 38394177), which is the right unit of process description.

## Potency assays and release testing

- Conventional readouts — chromium/calcein release, CD107a degranulation, IFN-γ — are 2-D, short-duration and
  single-round, and demonstrably fail to detect cryopreservation-induced defects (PMID 33067467).
- Better-correlating alternatives appearing in the literature:
  - **3-D spheroid microarrays** for high-throughput, high-content NK cytotoxicity (PMID 34290356), and 3-D
    colorectal spheroids where activated NK killing was independent of target PD-L1 (PMID 29632716).
  - **Serial-killing** assays, which reveal CD16-shedding-dependent limits invisible to single-round assays
    (PMID 41116262, PMID 39666369).
  - **Patient-derived organoid co-culture**, which shows hypoxia/TGF-β-driven, patient-specific diversification
    of NK activation programmes (PMID 41360426).
  - Sensitive metabolic viability readouts (resazurin-based) validated for NK-derived products
    (PMID 39022723).
- High-dimensional phenotyping and transcriptional profiling of the final product are now reported alongside
  clinical outcomes (PMID 39948608, PMID 38238616), which points toward phenotype-based release criteria
  (memory-like signature, CD16 expression, exhaustion markers) rather than purity and viability alone.

## Recommended release panel for a cryopreserved NK product

| Attribute | Assay |
|---|---|
| Identity/purity | CD56+CD3− frequency; residual T cells; residual feeder cells |
| Viability | post-thaw viability **and** recovery (both, not just viability) |
| Potency (primary) | 3-D or spheroid cytotoxicity post-thaw, at clinically plausible E:T |
| Potency (secondary) | serial-killing capacity; CD107a/IFN-γ after receptor restimulation |
| Fitness | post-thaw migration; metabolic readout |
| Phenotype | CD16 (and cleavage status), NKG2A/NKG2D/NCRs, memory-like and exhaustion markers |
| Genetic modification | vector copy number, transgene expression, editing efficiency, off-target/translocation assessment (PMID 41425600) |
| Safety | sterility, mycoplasma, endotoxin, residual feeder/irradiation controls |

## Open problems

- No consensus potency assay, which makes cross-product and cross-trial comparison of "NK activity" unreliable.
- Post-thaw functional loss is well documented but rarely reported in clinical papers, so its contribution to
  weak solid-tumour efficacy is unquantified.
- DMSO-free formulations are validated mostly for unmodified NK cells; edited and CAR-transduced products may
  behave differently.
