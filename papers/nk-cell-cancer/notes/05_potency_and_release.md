# Potency and release: why standard testing misses the thing that matters

This is the most actionable gap in the field. If one change had to be made to how NK products are developed, it
would be here.

## The problem, stated precisely

Conventional NK potency readouts — chromium/calcein release, CD107a degranulation, IFN-γ secretion — are 2-D,
short-duration, single-round and run at high E:T ratios. Cryopreserved NK cells **pass** them while having lost
3-D migration and cytotoxicity in tissue-like matrices (Mark 2020, PMID 33067467). The assay's blind spot lines up
exactly with the conditions that matter in a patient: low E:T, tissue mechanics, repeated engagement.

Consequences visible in this corpus:

- Fresh-versus-thawed functional loss is measurable when investigators look for it (PMID 32536506) but is rarely
  reported in clinical papers, so its contribution to weak solid-tumour efficacy is unquantified.
- "NK activity" is not comparable across products or trials, which is a large part of why the manufacturing
  platform comparison in `02_manufacturing_advances.md` has never been run.

## Assays that track the right thing

- **3-D spheroid / matrix cytotoxicity.** High-throughput 3-D spheroid microarrays for NK cytotoxicity
  (PMID 34290356); 3-D colorectal spheroid killing that was independent of target PD-L1 (PMID 29632716) — i.e.
  3-D formats change conclusions, not just numbers.
- **Serial killing.** Reveals the CD16-shedding ceiling that single-round assays cannot see (PMID 41116262) and
  distinguishes CD16 variants (PMID 39666369).
- **Patient-derived organoid co-culture.** Shows hypoxia/TGF-β-driven, patient-specific diversification of NK
  activation programmes (PMID 41360426) — the closest available proxy for what the product will meet.
- **Post-thaw migration**, given that migration is the function cryopreservation destroys first (PMID 33067467).
- **Metabolic readouts.** Resazurin-based viability validated for NK-derived products (PMID 39022723); metabolic
  fitness is the attribute that predicted in vivo durability (PMID 37494448) and is raised or lowered by the
  expansion platform (PMID 31624330) and by freezing.
- **High-dimensional phenotyping of the final product.** Now reported alongside clinical outcomes
  (PMID 38238616, PMID 39948608), which is what makes phenotype-based release criteria (memory-like signature,
  CD16 level and cleavage status, exhaustion markers) credible rather than aspirational.

## A defensible release panel

| Attribute | Assay | Why it is here |
|---|---|---|
| Identity / purity | CD56+CD3− frequency; residual T cells; residual feeder cells | standard; feeder residuals are a real CMC risk (PMID 19383914-class processes) |
| Viability **and** recovery | post-thaw, both reported | viability alone hides cell loss |
| Potency (primary) | 3-D or spheroid cytotoxicity, post-thaw, at clinically plausible E:T | the 2-D assay's documented blind spot (PMID 33067467) |
| Potency (secondary) | serial-killing capacity; CD107a/IFN-γ on receptor restimulation | catches CD16 shedding (PMID 41116262) |
| Fitness | post-thaw migration; metabolic readout | tracks the failure mode that drove in vivo relapse (PMID 37494448) |
| Phenotype | CD16 (and cleavage status), NKG2A/NKG2D/NCRs, memory-like and exhaustion markers | ties release to the state you intended to manufacture (PMID 22983442, PMID 38941480) |
| Genetic modification | VCN, transgene expression, editing efficiency, off-target and translocation assessment | edit count is limited by this, not by editing efficiency (PMID 41425600) |
| Safety | sterility, mycoplasma, endotoxin, irradiation controls for feeders | standard |

## What would have to be true for this to become standard

A cross-lab qualified 3-D or serial-killing potency assay with defined acceptance criteria. Nothing in this corpus
suggests that exists yet, and its absence is the single largest obstacle to comparing products, comparing
manufacturing platforms, or interpreting a disappointing trial as a biology failure versus a product failure.
