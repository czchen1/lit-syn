# Clinical translation, delivery, and reviews

## The first-in-human GBM DNA vaccine: GNOS-PV01 (GT-20)

- **Garfinkle et al. 2026 (PMID 42120910, *Nature Cancer*, full text in `pdfs/`)** with a lay **news feature in *Nature* (PMID 42151541)**. Senior author Tanner Johanns (WashU); ClinicalTrials.gov NCT04015700.
- **Product**: **GNOS-PV01** is a personalized DNA **plasmid (pGX0001 backbone, GenScript)** encoding **up to 40 patient-specific neoantigens** (range 17–40), GMP-manufactured. Neoantigens were selected from **3–4 geographically distinct tumor regions** (multiregion WES) to capture clonal and subclonal heterogeneity (21–58% of variants were region-restricted/subclonal).
- **Delivery**: **1 mg GNOS-PV01 + 1 mg INO-9012 (a DNA plasmid encoding IL-12, molecular adjuvant)**, injected **intramuscularly followed by in vivo electroporation with the CELLECTRA 2000 device (Inovio)**. This trial is **vaccine monotherapy** — no checkpoint inhibitor (a separate combination-with-PD-1 trial is NCT05743595).
- **Setting/schedule**: **adjuvant** after resection + radiation; priming doses every 3 weeks for 9 weeks, then boosters every 9 weeks until progression. **Median 4 doses** (range 2–18).
- **GT-20 trial**: open-label, single-arm **phase 1**; primary endpoints safety/feasibility, secondary endpoints immunogenicity and preliminary activity. 34 screened → 13 eligible → **9 vaccinated**.
- **Safety (met)**: no DLTs, no unexpected toxicities, **no GNOS-PV01-related serious AEs (≥grade 3, CTCAE v4.0)**; most AEs grade-1 injection-site reactions. One post-DLT-window grade-3 cerebral edema resolved with low-dose bevacizumab; vaccination continued. Including >20 neoantigens did not worsen safety.
- **Feasibility**: median **10 weeks** radiotherapy→first dose (range 5–18) and **22 weeks** surgery→first dose (range 17–30) — feasible but slower than the 4-week goal; pipeline speed flagged for future trials.
- **Immunogenicity**: ex vivo neoantigen restimulation of post-vaccine PBMCs gave a **significant increase in CD8⁺/CD4⁺ T cells expressing CD69, CD137, PD-1 and Ki67** vs unstimulated controls. T-cell activation **correlated with OS** — CD8⁺CD69⁺ (R=0.84, P=0.018) and CD8⁺IFNγ⁺ (R=0.78, P=0.04); not the CD4⁺ equivalents. Responses seen in all evaluated patients **except one on dexamethasone**. Monitoring: bulk **TCR-seq**, **IFNγ ELISpot**, **flow ICS**, **CIBERSORTx**.
- **Clinical activity**: **6-month PFS 66.7%; 12-month OS 66.7%; median PFS 8.5 mo; median OS 16.3 mo; 24-month survival 33%**, including **one patient alive and disease-free >4 years** (patient 8). Expected 24-month OS in this population is ~10–15%; against small contemporaneous institutional controls the cohort fared better, but **differences were not statistically significant**.
- **Significance**: first-in-human DNA-vaccine readout here; marks the field's shift from **single shared self/differentiation antigens** (TRP-2, VEGFR2) toward **personalized neoantigen** repertoires, and validates **in vivo electroporation + IL-12 plasmid adjuvant** as the human delivery strategy that overcomes the naked-plasmid immunogenicity limits seen preclinically.
- **Caveats**: n=9, single-arm, non-randomized; small institutional controls; corticosteroids suppress responses; feasibility timelines exceed target. Efficacy figures are hypothesis-generating.

## Antibody-framework DNA vaccine toward the clinic

- **SCIB1 / ImmunoBody® (Pearson et al. 2024; PMID 38954031, OA; see `01`)**: a clinical-stage DNA-vaccine modality (the ImmunoBody platform has prior melanoma clinical experience) here repositioned for intracranial TRP-2/gp100⁺ tumors in combination with PD-1 blockade. Represents the "engineered-antibody-as-antigen-vehicle" route to better APC targeting.

## Delivery methods seen across the corpus

| Method | Rationale | Papers |
| --- | --- | --- |
| **In vivo electroporation** of plasmid | Dramatically increases uptake/expression and immunogenicity of naked DNA; the human-validated route | Garfinkle 2026 |
| **Intramuscular naked plasmid** | Simplest; weak alone, used in early/proof-of-concept work | O 2003, Ueda 2008, Ginzkey 2013, Yamanaka 2005 |
| **DNA-launched alphavirus replicon** | Self-amplifying expression + innate RNA sensing | Yamanaka 2005 |
| **Oral live attenuated *Salmonella*** | Mucosal delivery; bacterial adjuvanticity | Feng 2004/2005 ×3 |
| **Bacterial TTSS (cytosolic) delivery** | Direct cytosolic antigen → MHC-I/CTL; rapid antigen screening | Derouazi 2010 |
| **Engineered viral-glycoprotein carrier (pTOP)** | Built-in innate immunogenicity + epitope-position tuning | Lopes 2021, Bausart 2022/2023 |
| **LAMP1 lysosomal-targeting fusion (UNITE)** | Routes antigen to MHC-II → CD4 help | Adhikari 2022 |
| **Genetic adjuvants co-encoded** | IL-12, IL-18, LIGHT, Bcl-xl, hsp70 to amplify/sustain responses | Feng 2005, Yamanaka 2005, Chen 2011, Kim 2005 |

## The proof-of-concept ceiling and combination imperative

- **Ginzkey et al. 2013 (PMID 23132370, OA)** is the field's candid limiting result: IM DNA vaccination against a strong model antigen (E. coli **lacZ**) in syngeneic **9L rat gliosarcoma** produced significantly smaller tumors but **>50% CTL lysis in only a minority of animals and incomplete tumor control** — even with an ideal foreign antigen. This frames why every later effort pairs the vaccine with checkpoint blockade (Bausart 2022, Pearson 2024), IL-12 (Feng series), or ICD chemotherapy (Bausart 2023).

## Reviews / landscape papers

- **Dain et al. 2023 (PMID 37037396, *Int J Pharm*, OA)** — "Nucleic acid immunotherapeutics and vaccines: a promising approach to GBM." Surveys **DNA and (increasingly) mRNA** therapeutics/vaccines for GBM and, importantly, the **delivery problem**: getting nucleic acids across the blood–brain barrier and into the CNS/systemic immune compartment, and the nanoparticle/local-delivery systems used. Positions mRNA as the rising modality alongside DNA, ASOs, siRNA/miRNA, aptamers, and peptide nucleic acids.
- **Lichtor et al. 2023 (PMID 38002466, *Brain Sci*, OA)** — "Cytokine Gene Vaccine Therapy for Treatment of a Brain Tumor." Reviews **cytokine gene vaccines** (IL-2, IL-15 and the four-α-helix-bundle cytokine family IL-2/4/7/9/15/21): e.g. **allogeneic fibroblasts transfected with tumor cDNA and engineered to secrete IL-2**, and **poxvirus engineered to secrete IL-15**, as survival-extending strategies in brain-tumor models. Bridges DNA/gene vaccination with cytokine-armoring concepts.
- **Trojan et al. 2024 (PMID 38031775, *Curr Med Chem*; abstract only)** — review/case of **anti-gene IGF-I vaccines** for GBM, using antisense (AS) or triple-helix (TH) episomal vectors to suppress IGF-I in autologous cell vaccines; included as a vaccination-intent gene strategy for GBM (note: this is a gene-modified-cell vaccine rather than an in-vivo plasmid injection — see scope note in `04`).

## Where the field stands (as captured here)

- **Preclinically**: many antigens (TRP-2, gp100, SOX6, EphA2, VEGFR2, HCMV) and platforms work to varying degrees in GL261/9L/U251 models, but **monotherapy rarely cures orthotopic GBM**.
- **Clinically**: a single phase 1 (GNOS-PV01/GT-20, 2026) shows a **personalized neoantigen DNA vaccine + electroporation is safe and immunogenic** in MGMT-unmethylated GBM — the translational milestone of this collection.
- **Trajectory**: from single shared antigens → personalized neoantigens; from naked IM plasmid → electroporation and engineered carriers; from vaccine-alone → checkpoint/cytokine/ICD combinations; and a parallel migration of interest toward mRNA.
