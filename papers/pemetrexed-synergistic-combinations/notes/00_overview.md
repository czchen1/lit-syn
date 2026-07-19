# Overview — Combinations synergistic with pemetrexed

## Why pemetrexed synergizes with so many partners

Pemetrexed is a multitargeted antifolate that inhibits **thymidylate synthase (TS)** (its principal target), dihydrofolate reductase, and GARFT, collapsing the thymidine and purine nucleotide pools required for DNA replication and repair. Its cytotoxicity is **S-phase dependent** and is amplified by intracellular polyglutamation (FPGS) and delivery through the **reduced folate carrier (RFC)** and **proton-coupled folate transporter (PCFT)**. This biochemistry defines four recurring synergy logics that organize this collection:

1. **Deplete nucleotides, then damage DNA (or block its repair).** Pemetrexed lowers dNTP pools; adding a DNA-damaging agent (platinum, radiation) or a repair/checkpoint inhibitor (WEE1, CHK1, ATR, PARP, base-excision-repair blockers) leaves cells unable to survive or repair — strongly synergistic, and often **schedule-dependent** (pemetrexed first to pre-deplete nucleotides).
2. **Raise pemetrexed activation or target expression.** Agents that increase TS turnover, PCFT/RFC transport, or polyglutamation, or that down-regulate TS (e.g. via MEK/ERK), sensitize to pemetrexed.
3. **Remove a survival buffer.** Blocking anti-apoptotic (BCL-XL/MCL-1), pro-survival signaling (PI3K/AKT/mTOR, SRC, STAT3, HSP90 clients), or metabolic escape (arginine, NAD, folate one-carbon flux) lowers the apoptotic threshold for pemetrexed-induced stress.
4. **Combine with orthogonal antitumor modalities.** Immunotherapy and antiangiogenics add non-overlapping mechanisms on the clinically validated pemetrexed/platinum backbone.

## Landscape (365 papers, 2001–2026)

- **286 preclinical synergy** studies + **79 clinical landmark** trials.
- Disease focus is dominated by **non-small cell lung cancer (nonsquamous)** and **malignant pleural mesothelioma** — the two indications where pemetrexed is standard of care.
- 148 papers have open-access full text in `fulltext/`.

| Partner class | n | Headline synergy |
|---|---|---|
| Immunotherapy (anti-PD-(L)1) | 70 | KEYNOTE-189: pembrolizumab + pemetrexed/platinum — practice-changing OS benefit |
| Chemo backbone (platinum, gemcitabine, taxane) | 59 | Cisplatin/pemetrexed is the reference doublet; schedule matters |
| Folate/TS modulation | 53 | TS down-regulation, PCFT/RFC transport, resistance reversal |
| EGFR-TKI | 52 | FLAURA2 (osimertinib + chemo); EGFR-TKI + pemetrexed intercalation |
| Targeted signaling / apoptosis | 47 | BCL-XL/MCL-1, mTOR/PI3K, HSP90, SRC, PLK1, NAMPT, arginine deprivation |
| Antiangiogenic | 27 | Bevacizumab/nintedanib/anlotinib maintenance and induction |
| DDR / cell-cycle checkpoint | 24 | WEE1, CHK1, ATR — abrogate G2/M checkpoint after nucleotide depletion |
| Radiosensitization | 18 | Pemetrexed is an intrinsic radiosensitizer; BER inhibition enhances it |
| ALK/ROS1/MET TKI | 9 | Continuing TKI with chemo at progression |
| Repurposed / natural | 6 | Metformin, ferroptosis induction, delivery-enabled combos |

## Cross-cutting themes

- **Schedule/sequence is decisive.** Pemetrexed-first pre-treatment (nucleotide depletion) sensitizes to subsequent radiation (Dorn 2016, PMID 27594806) and DNA-damaging agents; concurrent dosing with G1-arresting agents can antagonize S-phase kill. WEE1/CHK1 inhibitors work by abrogating the G2/M checkpoint cells rely on after chemotherapy damage.
- **Mesothelioma is a recurring testbed** for novel pemetrexed combinations because cisplatin/pemetrexed is its only standard doublet and resistance is near-universal: WEE1 (CRISPR-nominated, PMID 31694888), BCL-XL/MCL-1 (PMID 33298868), HSP90/ganetespib (MESO-02, PMID 32669375), arginine deprivation (ADI-PEG20, PMID 34589965), and capecitabine sequencing via CDA induction (PMID 39107509).
- **Transport and target biomarkers predict benefit** — PCFT/RFC expression, TS levels, and folate metabolism recur as determinants of sensitivity and as pharmacologic levers.
- **The clinical winners layer orthogonal modalities on the backbone** — IO (KEYNOTE-189) and antiangiogenics — rather than intensifying cytotoxicity.

## How to read this collection

Start with `01_chemotherapy_backbone.md` and `02_immunotherapy.md` for the clinically established synergies, then the mechanism-focused notes (`05`–`08`) for the preclinical synergy landscape that points to the next generation of combinations.
