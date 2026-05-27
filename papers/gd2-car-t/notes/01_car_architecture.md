# CAR architecture for GD2: scFv, spacer, transmembrane, costim, signaling

This note compiles construct-level commentary from the 204 papers in the collection. Each subsection summarises what has been tried, what works, and where there is unresolved debate, with citations to the underlying papers (PMID).

## 1. scFv (antigen-binding domain)

### 1.1 14g2a / 14G2a (murine IgG2a, the field standard)

- Originating antibody: 14G2a is a class-switched murine IgG2a derivative of the murine IgG3 14.18 antibody. It is the parent of clinically used dinutuximab (ch14.18). Its scFv (VH-linker-VL or VL-linker-VH) is the single most common GD2 binder in published CARs.
- The Brenner lab "1G GD2 CAR" used by Pule 2008 (Nat Med, PMID 18978797) joins a 14g2a scFv to a CD3ζ-only endodomain in the SFG retroviral vector (PMID 18978797 supplementary methods). The 14g2a is detected with anti-idiotype antibody 1A7 (also from Mike Brenner's group), which is the de facto staining reagent throughout the field.
- 14g2a "extended-linker" (XL): Long 2015 (Nat Med, PMID 25939063) replaces the typical (G4S)3 inter-domain linker with (G4S)4 and reports modest changes in clustering/tonic signaling.
- 14g2a "E101K" CDR3 affinity-matured variant: Richman 2018 (Cancer Immunol Res, PMID 29180536) introduces a single VH-CDR3 E→K substitution that increases GD2-binding affinity ~10-fold. In a CD28-CD3ζ CAR T cell this variant induces lethal encephalitis in mice; in a 4-1BB-CD3ζ CAR it is potent without lethality (PMID 29180536; debated in PMID 29610423 / 29610424 letters).
- Humanized 14g2a (hu14.18) scFv: appears in a minority of constructs (e.g. recent 2024–2025 preclinical work) and in clinical 14.18-IL2 immunocytokine work; not yet the dominant clinical CAR scFv.

### 1.2 3F8 / hu3F8

- Murine 3F8 is the second canonical anti-GD2 antibody (Cheung lab; humanized as naxitamab). Richman 2018 (PMID 29180536) constructs an m3F8 scFv in both VH-linker-VL and VL-linker-VH orientations and reports that **only the VL-linker-VH orientation yields a functional CAR**.
- Hu3F8 scFv CARs appear in several MSK-led preclinical papers (Hoseini 2017 PMID 28680755; later 2022–2024 papers in the collection).

### 1.3 Other GD2 binders explored in the collection

- **8B6 / O-acetyl-GD2 (OAcGD2)** binders, which spare healthy peripheral nerves (PMID 26298772, recent OAcGD2 papers): a strategy to retain tumor expression while reducing on-target/off-tumor neurotoxicity.
- **M3H7-based GD2 scFvs**: appear in a small number of preclinical Italian and Chinese papers (Prapa 2015 PMID 26298772; Chen 2023 PMID 36882513).
- **Non-scFv binders**: at least one paper in the collection uses a designed ankyrin repeat protein (DARPin) format rather than an scFv; logic-gate constructs (synNotch in Moghimi 2021) use anti-B7-H3 binder as the first gate and the standard 14g2a scFv as the second.

### 1.4 Empirical conclusions

- Across multiple direct comparisons (Mount 2018 PMID 29662203 vs Richman 2018 PMID 29180536; Quintarelli 2018 PMID 29872565 between 2G and 3G), unmodified 14g2a affinity with 4-1BB costimulation gives the best balance of potency vs neurotoxicity in CNS targets. Affinity boosting (E101K) is **not** advised with CD28-CD3ζ.
- The 14g2a framework drives substantial antigen-independent tonic CAR clustering (Long 2015 PMID 25939063), which differentially affects CD28 vs 4-1BB CARs (see costim section).

## 2. Hinge and transmembrane

- **CD8α hinge + CD8α TM**: dominant in 4-1BB-based GD2 CARs (Long 2015 PMID 25939063 GD2.BBz; Mount 2018 PMID 29662203 GD2-4-1BBz; Richman 2018 PMID 29180536; Majzner 2022 PMID 35130560).
- **CD28 hinge + CD28 TM**: paired with CD28 costimulation in early second-generation GD2 CARs.
- **IgG1 CH2CH3 spacer (long)**: used in the original Long 2015 GD2.28z construct (`MSGV-14g2a-28z` with a CH2CH3 hinge derived from human IgG1). Some IgG-spacered CARs interact with Fcγ receptors on myeloid cells and accelerate exhaustion; this motivated the move to CD8α-only spacers in modern constructs.
- **IgD hinge / "long" hinges**: examined in a few preclinical papers as a trade-off for very-low-density antigen.
- **Hinge length and tonic signaling**: shorter hinges (CD8α) reduce CAR clustering at the cell surface and lower constitutive CD3ζ phosphorylation; this is a consistent argument across the recent (2023–2026) optimization papers in the collection.

## 3. Costimulatory domains

The single most-discussed design axis in this collection. Direct comparisons appear in Quintarelli 2018 (PMID 29872565), Heczey 2014 (PMID 25049283), Heczey 2017 (PMID 28602436), Long 2015 (PMID 25939063), Zhong 2018 (PMID 30253384), Omer 2018 (PMID 30619856), Fisher 2017 (PMID 28341563), and Caforio 2021 (PMID 33737337).

### 3.1 CD3ζ only (1G)

- Pule 2008 / Louis 2011 used a strictly first-generation 14g2a-CD3ζ CAR in EBV-CTLs and ATCs. Persistence was short (peak signal by week 6), confirming clinically the need for added costimulation in T cells without native antigen support.

### 3.2 CD28-CD3ζ (2G, "GD2.28z")

- Drives the strongest immediate effector function but the worst tonic-signaling exhaustion in 14g2a CARs (Long 2015 PMID 25939063): GD2.28z CAR T cells fail to expand, accumulate apoptotic cells, and upregulate PD-1/TIM-3/LAG-3, T-bet, Blimp-1 within 5–9 days of activation. Cytokine production drops >100-fold versus CD19.28z controls.
- In NKT cells the same CD28-only configuration gives a Th2-leaning cytokine profile with reduced in-vivo persistence compared to 4-1BB (Heczey 2014 PMID 25049283).
- Quintarelli 2018 PMID 29872565 reports that CD28-only 2G CAR T cells produce strong cytotoxicity but rapidly become exhausted; this is the rationale for moving Bambino Gesù's clinical product to 3G.

### 3.3 4-1BB-CD3ζ (2G "BBz")

- Reduces tonic-signaling exhaustion and rescues expansion of 14g2a CAR T cells (Long 2015 PMID 25939063, Fig. 4). This is the dominant 2G configuration in CNS-directed GD2 CARs (Mount 2018 PMID 29662203; Majzner 2022 PMID 35130560; Monje 2025 PMID 39537919).
- Glienke 2022 (PMID 35401506) IL-18 TRUCK uses a 14g2a-4-1BB-CD3ζ backbone.
- In NKT cells, 4-1BB drives a Th1-polarized cytokine profile (Heczey 2014 PMID 25049283).

### 3.4 OX40-CD3ζ (2G)

- Used in some preclinical NB models; in NKT cells (Heczey 2014) does not match the persistence advantage of CD28+4-1BB combinations.

### 3.5 CD28-4-1BB-CD3ζ (3G)

- Quintarelli 2018 (PMID 29872565) directly compared CD28-OX40-CD3ζ vs CD28-4-1BB-CD3ζ third-generation CARs from a 14.G2a scFv. CD28-OX40-CD3ζ T cells plateaued in expansion; CD28-4-1BB-CD3ζ matched non-transduced T-cell expansion kinetics. CD28+4-1BB produced the most homogeneous, longer-lived stem-cell-memory-enriched product in vitro and the strongest tumor control in NB-xenograft mice. This 3G CD28-4-1BB-CD3ζ + iCasp9 became the clinical **GD2-CART01** product later used by Del Bufalo 2023 and Locatelli 2025 in NB.
- Caforio 2021 (PMID 33737337) extended the same CART01 design to medulloblastoma preclinical models with similar findings.

### 3.6 CD28-OX40-CD3ζ (3G, "GD2.CAR3")

- Heczey 2017 (Mol Ther, PMID 28602436) is the canonical example: 14g2a-CD28-OX40-CD3ζ + iC9 in the SFG retroviral backbone, manufactured at Texas Children's. The clinical trial showed that without lymphodepletion the cells expanded poorly, whereas Cy/Flu plus IL-7/IL-15-cultured cells expanded up to three logs.

### 3.7 Co-stimulation-only "1G" CARs

- Fisher 2017 (PMID 28341563) explored a costimulation-only CAR (no CD3ζ ITAMs) to avoid on-target / off-tumor activation; intended to be paired with a second activating signal.

### 3.8 Empirical conclusions

- For autologous T cells: CD28-4-1BB-CD3ζ (3G) is the dominant clinical choice (Bambino Gesù lineage). 4-1BB alone is preferred for CNS-directed CARs (Stanford lineage).
- For NKT cells: CD28+4-1BB combinations or 4-1BB alone outperform CD28 alone; CD28+OX40 may favor early effector function but with reduced persistence.

## 4. Signaling domain

Universally CD3ζ ITAM1-3 (full-length cytoplasmic tail of CD247). Variants tried:

- **ITAM mutants**: a small number of recent preclinical papers explore ITAM1-only or ITAM-mutant CD3ζ to tune signal strength and reduce tonic activation.
- **CD3ε ITAMs / Fas-fusion / DAP12**: appear in a handful of 2024–2026 optimization papers; not yet in the clinic for GD2.

## 5. Promoter and cassette layout

- **MoMLV LTR (SFG)**: Pule 2008 / Louis 2011, Heczey 2014, Heczey 2017 (PMID 18978797, 21984804, 25049283, 28602436). Spliced retroviral cassette with cryptic splice donor in 5'LTR; expression is tonic but moderate.
- **MSGV-1 / MSCV LTR**: Long 2015 GD2.28z, Mount 2018 GD2-4-1BBz, Majzner 2022 / Monje 2025 (PMID 25939063, 29662203, 35130560, 39537919). Higher and more stable expression than SFG; widely used in the NCI / Stanford lineage.
- **EF1α promoter, lentiviral**: Richman 2018 (PMID 29180536), Glienke 2022 (PMID 35401506), Chen 2019 (PMID 30617136). Increasingly the default for new clinical products because of better safety profile and capacity for larger payloads.
- **PGK / CAG promoters**: rare; used in some non-viral CAR knock-in studies that need to drive payloads outside the TRAC locus.
- **TRAC promoter (endogenous)**: Mueller 2022 (PMID 36382633), Balke-Want 2023 (PMID 37365642), Cappabianca 2024 (PMID 38699288), Foster 2025 — when the CAR is knocked into the TRAC locus, expression is driven by the TRAC promoter, giving more physiological CAR levels and TCR knockout simultaneously.

## 6. Multi-cistronic and armored cassettes

The collection includes many 2A-linked multi-gene cassettes:

- **CAR-P2A-iC9** (Quintarelli 2018; Del Bufalo 2023; Locatelli 2025; Majzner 2022; Monje 2025).
- **CAR-P2A-IL15** (Heczey 2020 Nat Med supplement PMID 33046868; Tian 2025 PMID 40044579).
- **CAR-T2A-C7R** (Heczey 2017 era and later; constitutively active IL-7Rα).
- **CAR-P2A-IL18** (Glienke 2022 PMID 35401506; transgene under NFAT-inducible promoter — "TRUCK 4th-generation" design).
- **CAR-P2A-RQR8** (Vandenberghe; appears in some safety-switch papers in the collection).
- **CAR + non-coding "barcode" oligo** for vector tracking (Pule 2008 "Zeta-5" / "Zeta-6" 12-bp tag for distinguishing CTL vs ATC integrations).

Constructs that combine more than two transgenes typically use a mix of 2A peptides (P2A, T2A) to avoid ribosomal skipping bias.
