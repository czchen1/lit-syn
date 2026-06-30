# 05 — Gene-editing payloads

46 papers carry a genome- or transcriptome-editing payload. The core delivery problem differs from single-mRNA payloads: editors require **co-delivery of multiple species** (Cas mRNA + sgRNA, or RNP, sometimes + donor DNA) and, for cancer, **extrahepatic and frequently cell-type-specific** editing — the opposite of the LNP's default liver tropism.

## Cargo formats

- **Cas9 mRNA + sgRNA** (most common): transient nuclease expression, attractive for safety.
- **RNP (protein + gRNA)**: Xu 2026 (PMID 41825677) uses aptamer (AS1411/nucleolin)-modified polymer-lipid hybrids for nuclear-directed RNP delivery.
- **pDNA-encoded CRISPR**: Mashreghi 2026 (PMID 41606801) delivers a CRISPR-Cas9 plasmid in LNP to knock out CDK4/6.
- **RNA / 3′UTR editing (no DNA cut).** Huang 2026 (*Nat Biomed Eng*, PMID 42303814) delivers a dCas13-based "3′UTR CRISPR engineering system" (3′UTRCES) to reverse tumour-specific 3′UTR shortening of SPSB1, restoring MHC-I and sensitising immune-cold prostate cancer to checkpoint therapy — editing the transcriptome rather than the genome.

## Targets edited in tumours

- **SOX2** (cancer-specific): Masarwy 2025 (*Adv Sci*, PMID 39736115) — intratumoural EGFR-targeted CRISPR-LNP knocks out SOX2 in HNSCC, 90% tumour-growth inhibition and tumour disappearance in 50% of mice.
- **PLK1**: Zeng 2026 (PMID 41494604) — CD44-peptide LNPs deliver Cas9 mRNA + sgPLK1 to melanoma, including brain metastases.
- **KRAS-G12S**: Marschhofer 2026 (PMID 41506374) — pulmonary-optimised LNPs deliver Cas9 mRNA + KRAS-G12S sgRNA intratracheally to NSCLC, ~90% in vitro editing, mucus-penetrating.
- **CDK4/6**: Mashreghi 2026 (PMID 41606801).
- **Lcn2**: Xu 2026 (PMID 41825677).
- **PD-1 / TRAC / B2M (engineering CAR-T)**: Wang 2026 (PMID 40879055) co-delivers CD19-CAR mRNA + Cas9 mRNA + sgRNAs to *make and edit* CAR-T in one LNP step — triple knockout (76% PD-1, 86% TRAC, 80% B2M) with higher viability than electroporation (bridges to notes/01).
- **TP53 (ex vivo HSC)**: Hiraki 2026 (PMID 41887390) — Bayesian-optimised HSC-targeted LNPs for cord-blood CD34⁺ TP53 editing (~40%).

## Solving extrahepatic / cell-specific editing

This is the dominant engineering motif:
- **Cell-targeting ligands**: EGFR (Masarwy), CD44 (Zeng), aptamer/nucleolin (Xu).
- **Organ-selective lipids**: pulmonary LNPs (Marschhofer 2026; Tian 2026 "tripod" LuT lipids, PMID 41845088, 9.2× CRISPR editing vs DOTAP-SORT and >90% lung selectivity); organic-solvent-free, PEG/ethanol-free water-based LNPs with extrahepatic preference (Streiber 2026, PMID 41913646).
- **Format/biocompatibility upgrades**: CRISPR LNP-spherical-nucleic-acids (Han 2025 PNAS, PMID 40906807) add a DNA shell for 2–3× uptake/indels and 21% HDR with donor; lipopolyplex core-shell systems for co-delivering two nucleotides (Gabelmann 2025, PMID 40412659).

## Combination editing

- Lee 2025 (*Cancer Res*, PMID 40327605) pairs multiplexed Cas9-nickase editing with PARP inhibition for precise cancer-cell targeting.
- The pulmonary KRAS-G12S editor (Marschhofer 2026) reads out via downstream apoptosis, linking editing to a therapeutic phenotype.

## Clinical framing

NTLA-2001 (in vivo CRISPR-LNP, hepatic) is the repeatedly-cited precedent for LNP-CRISPR feasibility; the cancer field's challenge, per these papers, is replicating that outside the liver and in a cell-specific way. Reviews: Khizar 2026 (PMID 41496934) and Sivamaruthi 2025 (PMID 41088907).
