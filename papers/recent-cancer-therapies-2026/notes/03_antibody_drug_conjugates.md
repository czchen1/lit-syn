# 03 — Antibody-drug conjugates

Bucket: `adc`. Small in absolute terms but the most trial-dense bucket per paper: the majority of `adc` rows are prospective clinical reports, and the phase-2 count exceeds phase-3, i.e. a wave of new targets is mid-pipeline while the first generation is being optimised.

## 1. New targets, mostly topoisomerase-I payloads

- **B7-H3** — ifinatamab deruxtecan pan-tumour dose-escalation (IDeate-PanTumor01, *Lancet Oncol*, PMID 41926962) and vobramitamab duocarmazine final phase-1 expansion (PMID 42487497). B7-H3 is simultaneously a CAR target (notes/01) and a radioconjugate target (notes/07).
- **SEZ6** — ABBV-706 in SCLC and solid tumours (*Nat Med*, PMID 42225988), a genuinely new SCLC surface antigen alongside DLL3 engagers.
- **Nectin-4 beyond urothelial** — SHR-A2102 in pretreated solid tumours (*Lancet Oncol*, PMID 42636836); nectin-4/Trop-2 expression in collecting-duct carcinoma (PMID 42526179).
- **EGFR and HER2 re-conjugated** — SYS6010 (EGFR-ADC) in NSCLC (*Cancer Cell*, PMID 42594871); SHR-A1811 global phase 1 (PMID 41856971); trastuzumab rezetecan vs pyrotinib+capecitabine in HER2+ MBC (HORIZON-Breast01, *Lancet Oncol*, PMID 42385760).
- **Lineage-restricted oddities** — anti-PMEL ADC with a Gq/11-inhibitor payload in GNAQ/GNA11-mutant melanoma (*Nat Med*, PMID 42443515) — payload chosen for the driver mutation, not for generic cytotoxicity; ADAM9-targeted glycan-linked exatecan ADC (MGC028, PMID 41166694); IL1RAP ADCs in oncofusion-driven cancers (*Cancer Discov*, PMID 41973074).

## 2. First-generation ADCs: combination and sequencing

Datopotamab deruxtecan (ICARUS-LUNG01 biomarker-rich phase 2, *Cancer Cell*, PMID 41999747; HR+/HER2− safety analysis, PMID 42497483), T-DXd with durvalumab first-line in HR−/HER2-low disease (*Nat Cancer*, PMID 42259988), enfortumab vedotin + pembrolizumab 5-year follow-up (EV-103 cohort A, PMID 42155320), tisotumab vedotin 5-year cervical data (PMID 42000372), mirvetuximab + pembrolizumab in FRα+ uterine serous carcinoma (PMID 41888141), and hematologic combinations (mosunetuzumab + polatuzumab in post-BTKi MCL, PMID 42013019; brentuximab + nivolumab + chemotherapy in early-stage cHL, PMID 41460964; inotuzumab in pediatric high-risk B-ALL relapse, ITCC-059, PMID 42296977; inotuzumab for MRD in adult ALL, PMID 42365008; belantamab mafodotin in intermediate-fit/frail newly diagnosed myeloma, PMID 41346230).

## 3. Resistance mechanism is the preclinical theme

Three complementary mechanisms were published in the window:

- **Endocytic evasion** as an ADC-resistance mode (*Cancer Cell*, PMID 42167230) — resistance without antigen loss.
- **Antigen heterogeneity and subclonal dynamics** in HER2-heterogeneous models (*Cancer Discov*, PMID 41925564).
- **Delivery/linker workarounds** — modular *in vivo* antibody–ADC "click" to reverse resistance (*Nature*, PMID 42457957) and a binding-to-release strategy for targeted delivery (*Nature*, PMID 42649302).

## 4. Practical pharmacology

The `clinical_other` rows are unusually useful here: quantitative HER2 tissue/plasma profiling predicting T-DXd activity (PMID 41826432); UGT1A1 germline variants and T-DXd toxicity (PMID 42114485); pooled sacituzumab govitecan safety across three regions (PMID 41861751); sex-based differences in developmental-ADC tolerability in NSCLC (PMID 42330841); CTC-based dynamic monitoring of TROP2/HER2 ADCs (PMID 42308036).

**Takeaway:** the class-defining question has shifted from "can we conjugate a topoisomerase-I payload to a new antigen" (evidently yes, repeatedly) to **target-expression thresholds, payload diversification, and mechanism-specific resistance**.
