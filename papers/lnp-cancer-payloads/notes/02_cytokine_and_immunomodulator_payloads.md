# 02 — Cytokine and immunomodulator payloads

The most-tagged *encoded* payload class (55 papers) is immunostimulatory cytokines and innate-immune agonists. The recurring rationale is that the most potent anti-tumour cytokines (IL-12 above all) are too toxic to give systemically as protein, so the work is fundamentally about **using the LNP to confine high cytokine expression to the tumour or a tolerant organ**, transiently and re-dosably.

## IL-12 and IL-12-centred constructs

IL-12 is the dominant payload. Strategies to tame its toxicity:
- **Replicon amplification at low dose.** Self-replicating RNA-LNP encoding IL-12 (Li 2020 *Nat Cancer*, PMID 34447945, intratumoural; Wang 2024 *Sci Rep*, PMID 38548896, "JCXH-211" given IV and intratumourally) drives high intratumoural IL-12, type-I-IFN, and immunogenic cell death, eradicating established tumours and protecting against rechallenge, with tolerability shown in mice and non-human primates.
- **Cascade amplification.** Li 2025 (*Commun Biol*, PMID 40851032) co-delivers self-amplifying mRNA + modified mRNA encoding alphavirus capsid/envelope so transfected cells package and spread the payload to neighbours — a 525-fold intratumoural IL-12 increase in B16F10 with single-cycle, safety-limited spread.
- **Low-toxicity coding scaffolds.** Hu 2026 (PMID 41896926) encodes IL-12 on circular single-stranded DNA (cssDNA)-LNP, uncoupling high hepatic expression from the inflammation/toxicity of plasmid DNA; 100% protection against rechallenge in c-MYC/p53 HCC.
- **Prodrug-tethered combination.** Shi 2026 (*Nat Nanotechnol*, PMID 41851499) builds prodrug ionizable lipids that release an IDO inhibitor intracellularly while delivering IL-12 mRNA — co-stimulating effector T cells while suppressing exhaustion; complete primary-tumour regression and abscopal effect in colon cancer.

## Cytokine cocktails and combinations

- Lee 2026 (PMID 42116169) co-delivers single-chain IL-12 + IL-15 + pro-IL-18 + Caspase-1 mRNAs intraperitoneally for ovarian cancer, finding the IL-15/IL-18/Caspase-1 combination superior to IL-12 monotherapy, and a reduced-dose regimen needed to manage hepatotoxicity.
- Niu 2026 (PMID 41027739) pairs a suicide-gene circRNA (CD-UPRT, see notes/07) with an IL-15-expressing circRNA to expand CD8 T and NK cells.

## Interferons

- Pan 2026 (PMID 40908442) encodes an IFN-α/anti-GPC3 fusion (GPA01) for liver-restricted in situ expression in HCC, with a >40-fold therapeutic window and PD-1 synergy.
- Fick 2025 (*JITC*, PMID 40750105) delivers IFNα2 mRNA in DOTAP-cholesterol LNP that accumulates in tumour-bearing lung, activating Cxcl9 to recruit CTLs and suppress lung metastasis without liver toxicity.
- Luo 2026 (PMID 40803233) reprograms tumour macrophages with IFN-γ mRNA via β-glucan-conjugated LNPs taken up by Peyer's-patch M cells after *oral* dosing — a "Trojan-horse" route exploiting endogenous macrophage tumour-homing.

## Innate-immune / co-stimulatory agonists

- **mRNA-2752 (clinical).** Sweis 2026 (*Clin Cancer Res*, PMID 42149124) reports the phase 1 of intratumoural LNP-mRNA encoding OX40L + IL-23 + IL-36γ ± durvalumab; 134 patients, manageable safety (two grade-2 CRS events), 17.9% confirmed ORR in CPI-resistant melanoma, with sustained intratumoural inflammation — the clearest clinical validation of a multi-payload LNP-mRNA in this collection.
- **STING/innate mimics.** Kaskow 2026 (PMID 41928973) uses an LNP-delivered multivalent peptide-polymer that mimics the STING C-terminal tail to activate TBK1/IRF3 even in STING-silenced tumours, driving type-I IFN and myeloid repolarisation in ovarian cancer.

## Cross-cutting localisation tactics

Across this bucket the levers used to make a toxic cytokine usable are: intratumoural/intraperitoneal/intravesical route; organ-restricted lipid tropism (liver for fusion proteins, lung for IFN); cell-homing ligands (β-glucan→macrophage); replicon/circRNA amplification to lower dose; and prodrug-lipid co-delivery. Hepatotoxicity and weight loss at high dose are the most frequently reported dose-limiting toxicities, repeatedly resolved by dose reduction rather than payload redesign.

See notes/06 for the saRNA/circRNA chemistry behind the amplified cytokine constructs and notes/08 for the organ-targeting lipids.
