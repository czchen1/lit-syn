# CDK4/6 inhibitors + chemotherapy in NSCLC and pleural mesothelioma

These are the disease settings where pemetrexed is the standard chemotherapy backbone (nonsquamous NSCLC; pleural mesothelioma with cisplatin/pemetrexed). Papers here establish the combination biology and clinical rationale even when the specific partner is a taxane, platinum, or immunotherapy rather than pemetrexed itself.

## Non-small cell lung cancer

### Single-agent CDK4/6i underperforms — the reason combinations are pursued
- **Goldman et al. 2020 — JUNIPER Phase III (PMID 33194700):** abemaciclib vs. erlotinib in KRAS-mutant stage IV NSCLC after platinum. Abemaciclib improved PFS (3.6 vs 1.9 mo) and ORR (8.9% vs 2.7%) but **not OS** (7.4 vs 7.8 mo). Confirms single-agent CDK4/6i is insufficient in NSCLC — motivating chemo/other combinations.
- **Liu et al. 2025 — JUNIPER biomarker reanalysis (PMID 40231258):** retrospective KRAS co-mutation expression subtyping found an **OS benefit in the KL subtype** (13.05 vs 5.65 mo; HR 0.25) — evidence that biomarker-selected NSCLC subsets may benefit and that combination trials should be enriched.

### Chemotherapy combinations enhance CDK4/6i activity (preclinical)
- **Cao et al. 2019 (PMID 30700828):** palbociclib + taxanes in squamous cell lung cancer — enhanced cytotoxicity via sustained pRB-E2F disruption, abrogation of the G2/M and spindle-assembly checkpoints, and reduced HIF-1α/angiogenesis; relevant because squamous NSCLC receives platinum-taxane rather than pemetrexed.
- **Son et al. 2021 (PMID 34593430):** docetaxel/paclitaxel + abemaciclib (LY2835219) in KRAS-mutant lung cancer — **sequence-dependent synergy** (DTX→LY and PTX→LY superior to concurrent), a direct illustration of the schedule dependence that also governs pemetrexed combinations.

### Immunotherapy combinations
- **Pujol et al. 2021 (PMID 34746886):** abemaciclib + pembrolizumab, Phase Ib, KRAS-mutant/squamous NSCLC — higher-grade toxicity (notably pneumonitis/transaminitis) tempered enthusiasm for CDK4/6i + IO in lung.

## Pleural mesothelioma

Mesothelioma is arguably the most rational setting for pemetrexed + CDK4/6i: cisplatin/pemetrexed is the chemotherapy standard and CDKN2A/p16 loss (≈70%) predicts CDK4/6 dependence.

- **Costa et al. 2024 (PMID 39011477):** abemaciclib, palbociclib, and ribociclib across a DPM cell-line panel — **abemaciclib most potent**, reducing viability, clonogenicity, and 3D spheroid growth, inducing G0/G1 arrest and apoptosis, and **retaining activity in cisplatin-resistant cells** (a key point for pemetrexed/cisplatin-refractory disease). RB-family single silencing did not abolish response.
- **Sreeram et al. 2026 (PMID 41963314):** palbociclib induces a reversible **pseudo-senescence** (SASP: IL-6/IL-8) in PM cells that regrow after drug removal; senolytics/BH3 mimetics did not convert this to cell death, but **cisplatin induced permanent arrest and complete senescence** — arguing that cytotoxic chemotherapy (the pemetrexed/cisplatin backbone), not senolytics, is the productive partner for CDK4/6i in mesothelioma.
- See also Terenziani 2022 (in `01_direct_pemetrexed_cdk46.md`) — abemaciclib + cisplatin/pemetrexed, the direct mesothelioma triplet.

## Takeaways for a pemetrexed + CDK4/6i strategy

1. **Single-agent CDK4/6i is inadequate in NSCLC/MPM** — combinations are necessary, and biomarker selection (KRAS subtype, CDKN2A loss, RB proficiency) matters.
2. **Mesothelioma is the highest-value setting** — CDKN2A-null biology + pemetrexed/cisplatin standard of care + preclinical triplet data + the MiST2 abemaciclib signal.
3. **Sequencing is decisive** — chemo→CDK4/6i schedules repeatedly outperform naive concurrent dosing in lung models.
4. **CDK4/6i can re-sensitize chemo-resistant cells** (cisplatin-resistant DPM), suggesting a role at progression on a pemetrexed/platinum backbone.
