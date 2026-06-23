# DHG-H3G34 mutation-by-mutation literature synthesis: which pathways drive each alteration

## Scope and provenance

This note works through the alterations seen in a **CSF circulating-tumor-DNA (ctDNA) profile of a diffuse hemispheric glioma, H3 G34-mutant (DHG-H3G34)** case (Belay Diagnostics Summit + Ascent panel) and, for each gene, summarizes the literature on **what pathway the alteration drives or disables**. No patient-identifying information is included; only the gene-level variant set is used, which is the relevant unit for literature interpretation.

The variant set is interpreted in the context of the established DHG-H3G34 biology already covered in `h3g34_scrnaseq_analysis_report.md` (GSX2/DLX+ interneuron-progenitor origin, H3K36me3 loss, ALT, frequent TP53/ATRX co-mutation). The point of this note is to connect each individual call to a mechanism/pathway.

## Variant set at a glance

CSF ctDNA can read out multiple genetically distinct subclones at once, so VAF is only a rough proxy for clonality (and is diluted by wild-type cell-free DNA). Ordered roughly by pathway:

| Gene / alteration | Type | VAF | Pathway bucket | Driver role in this context |
|---|---|---|---|---|
| H3-3A p.G35R (legacy G34R), c.103G>A | missense (oncohistone) | 17.5% | Chromatin / H3K36 methylation | Defining epigenetic driver |
| TP53 p.R273C, c.817C>T | missense hotspot | 54.3% | p53 tumor suppressor | Clonal/truncal LOF (± GOF) |
| MDM4 (chr1q32.1) | arm/focal gain | — | p53 (negative regulator) | p53 pathway suppression |
| PPM1D p.R552* (Tier 3) | truncating | — | p53 (negative regulator, Wip1) | Gain-of-function dampening of p53/DDR |
| PDGFRA p.Y288C, c.863A>G | extracellular-domain missense | 3.1% | RTK → PI3K/MAPK/STAT3 | Neomorphic activating subclone |
| EGFR (chr7p11.2) | gain | — | RTK → PI3K/MAPK | RTK dosage; WHO GBM-defining criterion |
| MET (chr7q31) | gain | — | RTK (HGF/MET) → PI3K/MAPK/STAT | Invasion / therapy resistance |
| PIK3CA p.H1047R, c.3140A>G | kinase-domain hotspot | 2.7% | PI3K/AKT/mTOR | Activating subclone |
| PTPN11 p.S502P, c.1504T>C | PTP-domain missense | 0.8% | RAS/MAPK (SHP2) | Activating subclone |
| SMAD4 p.Q169*, c.505C>T | nonsense | 0.1% | TGF-β/BMP–SMAD | Tumor-suppressor loss (minor subclone) |
| RB1 (chr13q14.2) | loss | — | CDK4/6–RB–E2F cell cycle | Cell-cycle checkpoint loss |
| ATRX (previously reported; **not detected** here) | — | — | Chromatin / ALT | See note below |

Tier-3 VUS of mechanistic interest covered at the end: SETD2 C1533R, PTPRD V892I, NOTCH2/NOTCH4, BAP1, CBL, AXIN2, RET, ROS1, ALK splice, BBC3/PUMA, FOXO1, PREX2, SDHC, SH2B3.

---

## 1. Chromatin / H3K36-methylation axis — the defining driver

### H3-3A p.G35R (H3.3 G34R)
- **Mechanism / pathway.** The G34 (new nomenclature G35) substitution sits next to K36 on the H3.3 tail and acts *in cis* to block the H3K36 trimethyltransferase **SETD2** and the demethylase **KDM2A** from engaging the tail, depleting **H3K36me3**. This reprograms transcription toward a developing-forebrain program and drives prominent **MYCN** upregulation (Bjerke/Schwartzentruber et al., *Cancer Discovery* 2013, PMID 23539269). Loss of H3K36me3 also disinhibits **PRC2**, perturbing the H3K36me3/H3K27me3 balance and pushing cells toward a specialized neuronal rather than stem-like state (Juretic et al., *PNAS* 2020; Crowell et al., *npj Precis Oncol* 2025, DOI 10.1038/s41698-025-01070-w).
- **Lineage co-option.** G34R/V tumors arise in **GSX2/DLX+ interneuron progenitors** and co-opt **PDGFRA** through a chromatin loop linking PDGFRA to GSX2 regulatory elements; ~50% of G34R/V tumors carry activating PDGFRA mutations under selection at recurrence (Chen et al., *Cell* 2020). This is the direct mechanistic link between the H3-3A driver and the PDGFRA subclone seen here.
- **DNA repair / genome integrity.** G34R impairs H3K36me3–MutSα (mismatch-repair) interaction and causes replication stress and homologous-recombination defects (Fang et al., *PNAS* 2018; Jain et al., *eLife* 2017), feeding the chromosomal instability noted on this report.

### SETD2 p.C1533R (Tier 3 VUS) — convergent on the same axis
- SETD2 is the **only** H3K36 trimethyltransferase in humans; loss-of-function SETD2 mutations occur specifically in **hemispheric high-grade gliomas of older children/young adults** and reduce H3K36me3, and are normally *mutually exclusive* with H3F3A mutations because they hit the same axis (Fontebasso et al., *Acta Neuropathol* 2013, DOI 10.1007/s00401-013-1095-8, PMID 23532809). C1533R lies near the catalytic SET domain. Its co-occurrence with H3-3A G35R here is notable: a second hit on the H3K36me3 axis would be expected to deepen the same epigenetic lesion, though as a VUS its functional impact is unproven.

---

## 2. Telomere maintenance / ALT — ATRX and KDM4B

- **ATRX (previously reported, NOT detected in this CSF specimen).** ATRX loss cooperates with H3G34R to activate **alternative lengthening of telomeres (ALT)**; essentially all DHG-H3G34R_ATRX tumors are ALT-positive, and this ALT state confers a basal DNA-damage burden exploited by **PARP-inhibitor + topoisomerase-I-inhibitor** combinations (Kfoury et al., *Neuro-Oncology* 2025, PMID/PMC11889718). Mechanistically, both **H3.3G34R and IDH1/2 mutations inactivate the demethylase KDM4B**, which acts in tandem with ATRX loss to trigger ALT (Voon/Wong et al., *Nat Commun* 2021, DOI 10.1038/s41467-021-22543-z).
- **Interpretation of the discordance.** The report explicitly states the previously reported ATRX variant was not detected in this specimen and that chromosomal instability increased. CSF ctDNA can miss a variant for sampling/sensitivity reasons or reflect genuine clonal evolution; either way, an ATRX-driven ALT phenotype established earlier would not necessarily be reversed by clonal turnover. This is the kind of finding to confirm against tissue/prior reports rather than over-interpret from a single ctDNA draw.

---

## 3. p53 pathway — hit at three levels simultaneously

This case disables p53 at the gene itself **and** through two negative regulators, a recurring theme in DHG-H3G34 (concurrent TP53 mutation in ~90%).

### TP53 p.R273C (VAF 54.3% — the most clonal call)
- R273 is a canonical **DNA-contact hotspot**: R273C abolishes sequence-specific DNA binding and transactivation while keeping the protein stable, so wild-type transcriptional output is lost and the wild-type allele is typically also lost (LOH) (Marker et al., *Neuro-Oncol Adv* 2022, DOI 10.1093/noajnl/vdab182, PMID 35047821). Beyond simple loss, hotspot mutants including R273C are widely proposed to have **gain-of-function** activities. The very high VAF is consistent with an early, truncal, biallelic event.

### MDM4 gain (chr1q32.1)
- MDM4 (and MDM2) are **negative regulators of p53**; 1q32.1 (MDM4) amplification is a recurrent way GBM suppresses p53 without mutating it, inactivating growth-arrest/apoptosis/senescence programs (Zhang Y et al., *Cancers* 2018, DOI 10.3390/cancers10090297; Riemenschneider et al., confirming MDM4 as the 1q32 amplicon target in malignant glioma). Here it layers on top of mutant TP53.

### PPM1D p.R552* (Tier 3, truncating)
- PPM1D encodes the phosphatase **Wip1**, a p53/DDR negative-feedback regulator. C-terminal **truncating** PPM1D mutations are recurrent **gain-of-function** events in pediatric gliomas (DIPG/DMG) that **oppose p53**, attenuate γH2AX/DNA-damage response, and suppress apoptosis and cell-cycle arrest after genotoxic stress; they are usually *mutually exclusive* with TP53 mutation (Zhang L et al., *Nat Genet* 2014, DOI 10.1038/ng.2995; *Nat Commun* 2022, DOI 10.1038/s41467-022-28198-8). The co-occurrence of PPM1D R552* with a strong TP53 R273C clone here is atypical (normally anti-correlated) and most likely indicates a **separate subclone**; PPM1D-mutant models are reported sensitive to **MDM2 inhibitors**.

**Net pathway read:** redundant, multi-node inactivation of p53 — relevant to the report's MDM4+TP53 trial matches (e.g., talazoparib combinations) and to the broader DDR/ALT vulnerability theme.

---

## 4. Receptor tyrosine kinase (RTK) signaling — PDGFRA, EGFR, MET

All three converge on **PI3K/AKT and RAS/MAPK** (≈86% of GBM carry ≥1 core RTK/PI3K event; Cheng & Guo, *J Exp Clin Cancer Res* 2019, DOI 10.1186/s13046-019-1269-x).

### PDGFRA p.Y288C — the most mechanistically specific RTK call
- Y288C is an **extracellular Ig-domain neomorphic activating mutation**: the receptor is high-mannose glycosylated and **ER-trapped**, yet **constitutively dimerized and phosphorylated without ligand**, driving constitutive **AKT, ERK1/2, and STAT3** activation. Critically, Y288C is **resistant to PDGFR kinase inhibitors but sensitive to PI3K/mTOR and MEK inhibitors** (Ip CKM et al., *Nat Commun* 2018;9:4583, DOI 10.1038/s41467-018-06949-w). This has direct therapeutic-selection implications and connects to the H3G34→GSX2→PDGFRA co-option model (Chen et al., *Cell* 2020).

### EGFR gain (chr7p11.2)
- EGFR is the single largest RTK subgroup in IDH-wildtype GBM and signals through **PI3K/AKT and RAS/MAPK**; EGFR amplification is a WHO diagnostic criterion for GBM, IDH-wildtype (report cites PMID 24120142). Copy gain here contributes RTK dosage rather than a defined activating mutation.

### MET gain (chr7q31)
- HGF/**MET** drives **PI3K/AKT, RAS/MAPK, JAK/STAT, SRC and Wnt** signaling and is strongly tied to **invasion/EMT, stem-like maintenance, and resistance to EGFR/VEGF-targeted therapy** in glioma (Cheng & Guo, *J Exp Clin Cancer Res* 2019). On 7q, it co-rides with the broader chr7 gain.

---

## 5. PI3K/AKT/mTOR — PIK3CA p.H1047R

- H1047R is one of the two dominant **PIK3CA hotspots** (kinase domain); it alters the membrane-binding surface of p110α and locks in an active-like conformation, **increasing membrane recruitment and lipid-kinase output** independent of upstream input, and is transforming in classic assays (Kang S, Bader AG, Vogt PK, *PNAS* 2005, DOI 10.1073/pnas.0408864102; structural work in *Nat Commun* 2023, PMC9837058). In GBM, PI3K-pathway genes (PIK3CA/PIK3R1/PTEN) are altered in ~25–30% of cases (report cites PMID 24120142). With PDGFRA-Y288C and EGFR/MET on the same axis, PI3K/AKT/mTOR is multiply reinforced — relevant to the report's PI3K-pathway trials (e.g., STX-478/RLY-2608/OKI-219).

---

## 6. RAS/MAPK — PTPN11 p.S502P (SHP2)

- PTPN11 encodes **SHP2**, a positive transducer of RAS/MAPK (and PI3K/JAK-STAT) downstream of RTKs; activating mutations relieve SHP2 autoinhibition. In glioma specifically, **SHP2/PTPN11 mediates PDGFRA + INK4A/ARF-driven gliomagenesis** by coupling PDGFRα to PI3K/AKT/mTOR (Liu KW et al., *JCI* 2011, DOI 10.1172/JCI43690). S502 lies in the PTP domain region implicated in the autoinhibitory N-SH2/PTP interface; activating PTPN11 events confer **MAPK-pathway dependence**, and gain-of-function PTPN11 in glioma has supported MEK-inhibitor (trametinib) response in case reports (PMC12994696). PTPN11 mutations are individually uncommon in solid tumors, consistent with the low VAF/subclonal status here.

---

## 7. TGF-β/BMP–SMAD — SMAD4 p.Q169* (loss)

- SMAD4 is the central co-SMAD effector of **TGF-β/BMP** signaling; Q169* is a **truncating loss-of-function** allele. Reduced SMAD4 expression correlates with higher glioma grade and worse survival, consistent with a tumor-suppressor role whose loss relieves growth inhibition / G1 arrest (He SM et al., *J Exp Clin Cancer Res* 2011, DOI 10.1186/1756-9966-30-70, PMID 21791112 — the citation used in the report). At VAF 0.1% this is a very minor subclone; mechanistically informative but unlikely to be a dominant driver.

---

## 8. Cell cycle — RB1 loss (chr13q14.2)

- RB1 is the gatekeeper of the **CDK4/6–RB–E2F** G1/S transition; the CDKN2A–CDK4/6–RB axis is altered in ~80% of primary GBM. **RB1 loss sits downstream of CDK4/6**, so RB1-deficient tumors are predicted *not* to respond to CDK4/6 inhibitors (sensitivity tracks with CDKN2A/CDKN2C codeletion and intact RB) (Wiedemeyer WR et al., *PNAS* 2010, PMID 20534551). This is an important caveat against CDK4/6-inhibitor strategies for this specimen, and contrasts with the CDK6 vulnerability described in RB-intact DHG-H3G34 (Liu et al., *Cancer Cell* 2024).

---

## 9. Other Tier-3 VUS — mechanistic context (lower confidence)

- **PTPRD p.V892I.** PTPRD is a frequently inactivated 9p receptor phosphatase tumor suppressor that **dephosphorylates STAT3**; its loss drives aberrant STAT3 activation and cooperates with CDKN2A loss in gliomagenesis (Ortiz B et al., *PNAS* 2014, DOI 10.1073/pnas.1401952111; Veeriah S et al., *PNAS* 2009). A missense VUS here is of uncertain effect but plausibly relevant to STAT3 tone (which PDGFRA-Y288C also elevates).
- **NOTCH2 (L1220P), NOTCH4 (G583E, R234Q).** NOTCH is **context-dependent (oncogene vs tumor suppressor) in glioma**; inactivating NOTCH mutations occur in some gliomas (Parmigiani E, Taylor V, Giachino C, *Cells* 2020, DOI 10.3390/cells9102304). Direction of effect for these specific VUS is unknown.
- **BAP1 (R56H), CBL (S407P), AXIN2 (Y550D), FOXO1 (A511V), PREX2 (V678L), BBC3/PUMA (G193R), SH2B3 (P242S), RET (V292M), ROS1 (Y761*), ALK (c.2487+1G>A splice), SDHC (C70R), KAT6A, LRP1B, SETBP1-adjacent, etc.** These touch deubiquitination/PR-DUB (BAP1), RTK ubiquitination (CBL), Wnt/β-catenin (AXIN2), PI3K-FOXO (FOXO1), apoptosis (BBC3/PUMA), and JAK/STAT (SH2B3) — but all are Tier-3 VUS at unknown functional significance and should be treated as hypotheses, not drivers. Several (RET V292M, SDHC C70R) are common germline polymorphisms in population databases and most likely incidental.

---

## 10. Cross-cutting themes

1. **One epigenetic driver, many signaling subclones.** A single truncal H3-3A G35R + biallelic TP53 R273C backbone, with **branching RTK/PI3K/MAPK subclones** (PDGFRA Y288C, PIK3CA H1047R, PTPN11 S502P) at low VAF and broad copy-number RTK gains (EGFR, MET). This matches the DHG-H3G34 model where G34 stalls differentiation and downstream RTK/PI3K events are co-opted and selected.
2. **p53 redundantly disabled** (TP53 mutation + MDM4 gain + PPM1D truncation) — supports p53-axis/DDR therapeutic framing and MDM2-inhibitor rationale for PPM1D-mutant subclones.
3. **Convergence on PI3K/AKT/mTOR and RAS/MAPK** from at least four independent nodes — the PI3K/mTOR and MEK inhibitor sensitivities reported for PDGFRA-Y288C are the most mechanistically grounded targeted angle.
4. **Genome instability program** (H3K36me3 loss → MMR/HR defects, ALT history, high arm-level CNV burden, RB1 loss) — coherent with the report's emphasis on chromosomal instability and with PARP/DDR vulnerabilities described for ALT+ DHG-H3G34.
5. **Caveats:** RB1 loss argues against CDK4/6 inhibitors; PDGFRA-Y288C is intrinsically resistant to PDGFR TKIs; low-VAF calls are subclonal and ctDNA-sensitivity-limited.

## References (new, added to index.tsv)

Key newly indexed mechanism papers: Ip et al. *Nat Commun* 2018 (PDGFRA Y288C); Liu KW et al. *JCI* 2011 (PTPN11/SHP2 glioma); Marker et al. *Neuro-Oncol Adv* 2022 (TP53 R273C); Kang/Bader/Vogt *PNAS* 2005 (PIK3CA oncogenicity); He et al. *J Exp Clin Cancer Res* 2011 (SMAD4 glioma); Zhang Y et al. *Cancers* 2018 (p53/MDM4 in GBM); Cheng & Guo *J Exp Clin Cancer Res* 2019 (MET/RTK glioma); Wiedemeyer et al. *PNAS* 2010 (RB1/CDK4-6); Zhang L et al. *Nat Genet* 2014 and *Nat Commun* 2022 (PPM1D); Voon/Wong et al. *Nat Commun* 2021 (KDM4B/ALT); Ortiz et al. *PNAS* 2014 and Veeriah et al. *PNAS* 2009 (PTPRD/STAT3); Fontebasso et al. *Acta Neuropathol* 2013 (SETD2); Parmigiani et al. *Cells* 2020 (NOTCH in glioma).
