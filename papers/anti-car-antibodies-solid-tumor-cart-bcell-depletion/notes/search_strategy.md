# Search strategy, screening, and inclusion rules

Database: PubMed/Europe PMC via NCBI E-utilities (esearch/esummary/efetch), searched 2026-08-06.
**3,107 unique records** were retrieved across 49 queries in 5 rounds and screened on title/abstract;
185 were curated into `../index.tsv`; 101 open-access full texts were downloaded into `../fulltext/`.

## Inclusion rules

Included as **direct evidence** only if the record reports humoral anti-CAR / anti-idiotype / anti-drug
antibodies (or an intervention against them) in engineered T cells used **outside** B-cell malignancy —
solid tumours preferentially, plus the SIV/HIV CAR-T primate work because it is the only setting where
anti-CD20 was actually given before a CAR product.

Included as **indirect/contextual**, always labelled: AAV and other gene-therapy prophylaxis; enzyme
replacement and haemophilia immune tolerance induction; rituximab pharmacology; historical HAMA suppression
in solid tumours; ADA assays and regulatory guidance.

Retained with an explicit `MECHANISM ONLY` flag: a small number of lymphoma/leukaemia/myeloma CAR-T papers
that supply transferable biology unavailable elsewhere (first human demonstration of anti-transgene
rejection; plasma-cell survival during B-cell aplasia; ADA assay validation; fully human binder redesign
motivated by ADA-blocked retreatment).

## Explicit exclusions

- CAR-T for lymphoma, leukaemia, myeloma, or other B-cell malignancies as a source of *conclusions*.
- Rituximab as anti-tumour therapy, or to sensitise/upregulate a target on tumour cells.
- Rituximab as a CAR **safety/suicide switch** (CD20, RQR8, QBEnd10) — collected separately in
  `I_confusables_do_not_confuse` because it is the dominant false-positive in every query combining
  "rituximab" with "chimeric antigen receptor", and because it is a contraindication rather than a therapy.
- Autoimmune-disease CD19 CAR-T, anti-CD20 vaccine-response studies, and generic HAMA literature, except
  where used purely for B-cell-depletion timing/depth principles.

## Notable zero-hit queries (evidence of absence, within PubMed indexing)

- `t7_rituximab_prior_cellular_therapy` — rituximab given *prior to* adoptive cell therapy for
  immunogenicity/anti-CAR/anti-drug-antibody purposes: **0 records**.
- `t10_second_infusion_solid_tumor_outcome` — loss of expansion after a second/subsequent infusion in solid
  tumours, as an indexed phrase: **0 records**.

These are the two searches that would have surfaced a rituximab-plus-solid-tumour-CAR-T prophylaxis protocol
if one were indexed. Absence in PubMed does not exclude unindexed trial protocols, conference abstracts, or
ClinicalTrials.gov records, which were not exhaustively searched.

## Screening notes

Automated keyword scoring was used for triage only; it over-ranked records where "CAR", "antibody" and
"rituximab" co-occur incidentally (autoimmunity, vasculitis, vaccine, and lymphoma literature), so every
curated record was confirmed by reading its title and abstract, and dose/schedule claims were taken from
full text where available (`dosing_schedules_extracted.md`).

## Queries

### Round 1

- `q1_car_immunogenicity`
  ```
  ("chimeric antigen receptor" OR "CAR-T" OR "CAR T") AND (immunogenicity OR "anti-drug antibod*" OR "anti-CAR antibod*" OR "anti-idiotype" OR "anti-idiotypic" OR "neutralizing antibod*" OR "humoral immune response" OR HAMA)
  ```
- `q2_car_rituximab_prevent`
  ```
  ("chimeric antigen receptor" OR "CAR-T") AND rituximab AND (immunogenicity OR "anti-drug antibod*" OR "anti-CAR" OR "B cell depletion" OR prophyla* OR tolerance)
  ```
- `q3_car_redosing_solid`
  ```
  ("chimeric antigen receptor") AND ("solid tumor" OR "solid tumour") AND (redosing OR "repeat infusion" OR "repeated infusions" OR reinfusion OR "multiple doses")
  ```
- `q4_immune_tolerance_induction_rituximab`
  ```
  rituximab AND ("immune tolerance induction" OR "antibody formation" OR "inhibitor development" OR "anti-drug antibod*") AND (methotrexate OR IVIG OR "intravenous immunoglobulin" OR sirolimus OR bortezomib OR cyclophosphamide)
  ```
- `q5_aav_gene_therapy_rituximab`
  ```
  ("gene therapy" OR "AAV" OR "adeno-associated virus") AND rituximab AND ("neutralizing antibod*" OR immunosuppress* OR "antibody response" OR prophylaxis)
  ```
- `q6_cd20_safety_switch`
  ```
  ("chimeric antigen receptor") AND (rituximab OR CD20) AND ("safety switch" OR "suicide gene" OR RQR8 OR "elimination marker")
  ```
- `q7_scfv_humanization_car`
  ```
  ("chimeric antigen receptor") AND ("murine scFv" OR humanized OR humanization OR "fully human") AND (immunogenicity OR "anti-CAR" OR rejection OR "transgene product")
  ```

### Round 2

- `a_anticar_humoral`
  ```
  (("chimeric antigen receptor" OR "CAR T" OR "CAR-T" OR "engineered T cell*" OR "TCR-T" OR "transgenic TCR") AND ("anti-CAR antibod*" OR "anti-CAR immune" OR "anti-idiotyp*" OR "human anti-mouse antibod*" OR HAMA OR "antibody against the CAR" OR "antibodies against the transgene" OR "transgene immunogenicity" OR "anti-transgene immune response" OR "host immune response against" OR "immune-mediated rejection of"))
  ```
- `b_car_ada`
  ```
  (("chimeric antigen receptor" OR "CAR-T" OR "CAR T cell*") AND ("anti-drug antibody" OR "anti-drug antibodies" OR "antidrug antibod*" OR immunogenicity[Title]))
  ```
- `c_rituximab_car_any`
  ```
  rituximab AND ("chimeric antigen receptor" OR "CAR-T" OR "CAR T cell*") AND ("solid tumor*" OR "solid tumour*" OR glioma OR neuroblastoma OR sarcoma OR mesothelioma OR "renal cell" OR prostate OR ovarian OR pancrea*)
  ```
- `d_bcell_depletion_prevent_ada`
  ```
  (rituximab OR "anti-CD20" OR obinutuzumab OR ocrelizumab OR "B-cell depletion" OR "B cell depletion") AND ("prevent* the formation of" OR "prevent antibody" OR "prevention of antibody" OR "prevent* anti-drug antibod*" OR "immune tolerance induction" OR "immunosuppressive prophylaxis" OR "prophylactic immunomodulation") 
  ```
- `e_repeat_dosing_solid_car`
  ```
  ("chimeric antigen receptor") AND ("repeat dosing" OR "repeated dosing" OR "redosing" OR "re-dosing" OR "multiple infusions" OR "repeat infusions" OR "second infusion" OR reinfusion OR "re-infusion")
  ```
- `f_lamers_kershaw_maus`
  ```
  ("carboxy-anhydrase-IX" OR "CAIX" OR "folate receptor alpha" OR mesothelin OR "HER2" OR "GD2" OR "IL13Ralpha2" OR "IL13Ra2" OR "EGFRvIII") AND ("chimeric antigen receptor") AND (immunogenic* OR "antibody response" OR anaphylax* OR "anti-idiotyp*" OR "cellular immune response against")
  ```
- `g_aav_bcell_ritux`
  ```
  ("adeno-associated viral" OR "adeno-associated virus vector*" OR "AAV vector*" OR "gene transfer") AND rituximab AND (sirolimus OR "neutralizing antibod*" OR "antibody formation" OR redosing OR "immune modulation")
  ```
- `h_ert_iti_ritux`
  ```
  ("enzyme replacement therapy" OR "Pompe disease" OR alglucosidase OR "hemophilia" OR "factor VIII inhibitor*") AND rituximab AND ("immune tolerance induction" OR "antibody titer*" OR prophyla*)
  ```
- `i_ritux_dosing_pk`
  ```
  rituximab AND ("dosing schedule" OR "dose schedule" OR "375 mg/m2" OR "pharmacokinetic*" AND "B cell recovery") AND ("B-cell depletion" OR "B cell depletion" OR repopulation)
  ```
- `j_car_solid_tumor_immunosuppression`
  ```
  ("chimeric antigen receptor") AND ("solid tumor*" OR "solid tumour*") AND ("host immunity" OR "host immune response" OR "immune rejection" OR "anti-CAR" OR "limited persistence" OR "transgene-specific")
  ```
- `k_mska_hama_compartmental`
  ```
  (HAMA OR "human anti-mouse antibody") AND (rituximab OR immunosuppress*) AND ("radioimmunotherapy" OR "monoclonal antibody therapy" OR omburtamab OR 8H9 OR 3F8)
  ```
- `l_car_autoimmune_ritux`
  ```
  ("chimeric antigen receptor") AND ("anti-CD20" OR rituximab) AND ("pretreatment" OR "pre-treatment" OR conditioning OR lymphodepletion) AND (antibod* )
  ```

### Round 3

- `s1_anticar_specific`
  ```
  ("anti-CAR antibod*"[tw] OR "anti-CAR immune response*"[tw] OR "anti-idiotype antibod*"[tw] AND "chimeric antigen receptor"[tw])
  ```
- `s2_immunogenicity_cart_review`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR T"[tw]) AND immunogenic*[ti]
  ```
- `s3_transgene_rejection`
  ```
  ("chimeric antigen receptor"[tw] OR "gene-modified T cell*"[tw] OR "engineered T cell*"[tw]) AND ("transgene product"[tw] OR "transgene-specific"[tw] OR "anti-transgene"[tw] OR "immune rejection"[tw] OR "immunological rejection"[tw] OR "host-mediated rejection"[tw] OR "cellular immune response against the"[tw])
  ```
- `s4_scfv_ada_assay`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR T"[tw] OR "TCR-T"[tw]) AND ("anti-drug antibod*"[tw] OR "antidrug antibod*"[tw] OR "ADA assay"[tw] OR "immunogenicity assessment"[tw] OR "immunogenicity assay*"[tw])
  ```
- `s5_solid_car_trials_repeat`
  ```
  ("chimeric antigen receptor"[tw]) AND ("clinical trial"[pt] OR "phase 1"[tw] OR "phase I"[ti]) AND ("solid tumor*"[tw] OR sarcoma[tw] OR glioma[tw] OR glioblastoma[tw] OR neuroblastoma[tw] OR mesothelioma[tw] OR "renal cell carcinoma"[tw] OR "prostate cancer"[tw] OR "ovarian cancer"[tw] OR "pancreatic cancer"[tw] OR "colorectal"[tw] OR "pontine glioma"[tw] OR "midline glioma"[tw]) AND ("repeat"[tw] OR "repeated"[tw] OR "multiple infusions"[tw] OR "second infusion"[tw] OR redos*[tw] OR reinfus*[tw] OR "re-infusion"[tw] OR "intracranial"[tw] OR "intraperitoneal"[tw] OR "intrapleural"[tw] OR "hepatic artery"[tw])
  ```
- `s6_ritux_prophylaxis_gt`
  ```
  rituximab[tw] AND ("gene therapy"[tw] OR "gene transfer"[tw] OR "adeno-associated"[tw] OR "AAV vector"[tw] OR "enzyme replacement"[tw] OR "factor VIII"[tw] OR "factor IX"[tw] OR "asparaginase"[tw] OR "immune tolerance induction"[tw]) AND (prophyla*[tw] OR prevent*[tw] OR "antibody formation"[tw] OR "antibody titer*"[tw] OR "anti-drug antibod*"[tw] OR "neutralizing antibod*"[tw] OR "inhibitor development"[tw])
  ```
- `s7_ritux_bcell_kinetics`
  ```
  rituximab[tw] AND ("B-cell depletion"[tw] OR "B cell depletion"[tw] OR repopulation[tw] OR reconstitution[tw]) AND (pharmacokinetic*[tw] OR "dose"[ti] OR dosing[tw] OR "375 mg"[tw] OR "1000 mg"[tw] OR schedule*[tw]) AND ("plasma cell*"[tw] OR "memory B cell*"[tw] OR "antibody response"[tw] OR "serum immunoglobulin"[tw] OR "vaccine response"[tw] OR duration[tw])
  ```
- `s8_ritux_kill_switch`
  ```
  (rituximab[tw] OR "CD20"[tw]) AND ("safety switch"[tw] OR "suicide switch"[tw] OR "elimination marker"[tw] OR RQR8[tw] OR "QBEnd10"[tw]) AND ("chimeric antigen receptor"[tw] OR "T cell*"[tw])
  ```
- `s9_hama_solid_mab`
  ```
  ("human anti-mouse antibod*"[tw] OR HAMA[tw] OR "human anti-chimeric antibod*"[tw]) AND (neuroblastoma[tw] OR glioma[tw] OR "solid tumor*"[tw] OR "radioimmunotherapy"[tw] OR "3F8"[tw] OR "8H9"[tw] OR omburtamab[tw] OR dinutuximab[tw] OR "ch14.18"[tw])
  ```
- `s10_bcell_depletion_before_immunogen`
  ```
  (rituximab[tw] OR "anti-CD20"[tw]) AND ("prior to"[tw] OR pretreat*[tw] OR "pre-treatment"[tw] OR preconditioning[tw] OR "before administration"[tw]) AND ("prevent* antibod*"[tw] OR "blunt* the antibody"[tw] OR "abrogat* antibod*"[tw] OR "suppress* antibody"[tw] OR "humoral response"[tw] OR "primary antibody response"[tw])
  ```
- `s11_car_solid_persistence_host`
  ```
  ("chimeric antigen receptor"[tw]) AND ("solid tumor*"[tw] OR "solid tumour*"[tw]) AND ("limited persistence"[tw] OR "lack of persistence"[tw] OR "poor persistence"[tw] OR "host immune response*"[tw] OR "immunogenicity"[tw])
  ```
- `s12_ivig_plasma_cell_ada`
  ```
  ("anti-drug antibod*"[tw] OR "neutralizing antibod*"[tw] OR "inhibitor*"[tw]) AND (bortezomib[tw] OR daratumumab[tw] OR "anti-CD38"[tw] OR "plasma cell depletion"[tw] OR "IdeS"[tw] OR imlifidase[tw] OR "anti-CD20"[tw] OR rituximab[tw]) AND ("gene therapy"[tw] OR "AAV"[tw] OR "enzyme replacement"[tw] OR "cell therapy"[tw] OR "redos*"[tw] OR "re-administration"[tw] OR readministration[tw])
  ```

### Round 4

- `t1_lamers`
  ```
  Lamers CH[au] AND ("chimeric"[tw] OR CAIX[tw] OR "carboxy-anhydrase"[tw] OR "renal cell"[tw])
  ```
- `t2_kershaw_frα`
  ```
  ("folate receptor"[tw]) AND ("chimeric receptor"[tw] OR "chimeric antigen receptor"[tw]) AND (ovarian[tw] OR "phase I"[tw] OR "clinical trial"[pt])
  ```
- `t3_anticd20_prevent_anticar_preclin`
  ```
  ("anti-CD20"[tw] OR rituximab[tw] OR "B cell depletion"[tw] OR "B-cell depletion"[tw] OR "BAFF"[tw] OR "anti-CD38"[tw] OR daratumumab[tw]) AND ("adoptive transfer"[tw] OR "adoptive cell"[tw] OR "CAR T"[tw] OR "chimeric antigen receptor"[tw] OR "gene-modified T cell*"[tw]) AND ("anti-CAR"[tw] OR "anti-transgene"[tw] OR "antibody response"[tw] OR "humoral response"[tw] OR "repeat dosing"[tw] OR readministration[tw] OR "re-administration"[tw] OR persistence[tw])
  ```
- `t4_hama_prevent_immunosuppression`
  ```
  (HAMA[tw] OR "human anti-mouse antibod*"[tw] OR "human antimouse antibod*"[tw]) AND (prevent*[tw] OR abrogat*[tw] OR suppress*[tw] OR rituximab[tw] OR cyclosporin*[tw] OR "immunosuppress*"[tw] OR methotrexate[tw] OR "deoxyspergualin"[tw]) AND ("repeat*"[tw] OR "retreatment"[tw] OR "multiple cycles"[tw] OR "subsequent"[tw] OR "murine antibod*"[tw])
  ```
- `t5_aav_readmin_immunomod`
  ```
  ("adeno-associated"[tw] OR "AAV"[ti]) AND (readministration[tw] OR "re-administration"[tw] OR redosing[tw] OR "repeat administration"[tw] OR "second dose"[tw]) AND (rituximab[tw] OR "B cell depletion"[tw] OR imlifidase[tw] OR IdeS[tw] OR plasmapheresis[tw] OR bortezomib[tw] OR "immune modulation"[tw] OR sirolimus[tw] OR rapamycin[tw])
  ```
- `t6_solid_car_trials_immunogenicity_named`
  ```
  ("chimeric antigen receptor"[tw]) AND ("HER2"[tw] OR "GD2"[tw] OR "B7-H3"[tw] OR "IL13Ralpha2"[tw] OR "IL13Ra2"[tw] OR "EGFRvIII"[tw] OR mesothelin[tw] OR "CEA"[tw] OR "PSCA"[tw] OR "PSMA"[tw] OR CLDN6[tw] OR "claudin 18.2"[tw] OR GPC3[tw] OR "CAIX"[tw] OR "MUC1"[tw] OR "CD70"[tw]) AND ("phase 1"[tw] OR "phase I"[ti] OR "first-in-human"[tw] OR "clinical trial"[pt]) AND ("solid"[tw] OR glioma[tw] OR sarcoma[tw] OR neuroblastoma[tw] OR carcinoma[tw] OR glioblastoma[tw] OR mesothelioma[tw])
  ```
- `t7_rituximab_prior_cellular_therapy`
  ```
  rituximab[tw] AND ("adoptive cell therapy"[tw] OR "adoptive immunotherapy"[tw] OR "cell therapy"[tw] OR "CAR T"[tw]) AND ("prior to"[tw] OR before[tw] OR prophylactic[tw] OR preemptive[tw]) AND ("antibody formation"[tw] OR "anti-drug antibod*"[tw] OR "immunogenicity"[tw] OR "anti-CAR"[tw] OR "neutralizing"[tw])
  ```
- `t8_ritux_pk_dose_response`
  ```
  rituximab[tw] AND ("low dose"[tw] OR "single dose"[tw] OR "100 mg"[tw] OR "375 mg/m2"[tw] OR "1000 mg"[tw] OR "dose-finding"[tw]) AND ("B cell depletion"[tw] OR "B-cell depletion"[tw]) AND ("kinetics"[tw] OR duration[tw] OR "time to"[tw] OR onset[tw] OR "lymph node"[tw] OR "germinal cent*"[tw] OR "tissue"[tw])
  ```
- `t9_regulatory_guidance_immunogenicity`
  ```
  ("immunogenicity"[ti] OR "anti-drug antibod*"[ti]) AND (guidance[tw] OR "regulatory"[tw] OR "FDA"[tw] OR "EMA"[tw] OR "risk assessment"[tw]) AND ("cell therapy"[tw] OR "gene therapy"[tw] OR "CAR-T"[tw] OR "CAR T"[tw])
  ```
- `t10_second_infusion_solid_tumor_outcome`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR-T"[tw]) AND ("solid"[tw] OR glioma[tw] OR sarcoma[tw] OR neuroblastoma[tw] OR mesothelioma[tw] OR carcinoma[tw]) AND ("loss of"[tw] OR "decreased"[tw] OR "diminished"[tw] OR "absent"[tw]) AND ("expansion after the second"[tw] OR "subsequent infusions"[tw] OR "second infusion"[tw] OR "later infusions"[tw] OR "repeat infusions"[tw])
  ```

### Round 5

- `u1`
  ```
  Kershaw MH[au] AND ("folate receptor"[tw] OR "phase I"[tw] OR ovarian[tw])
  ```
- `u2`
  ```
  Ahmed N[au] AND "HER2"[tw] AND (sarcoma[tw] OR glioblastoma[tw]) AND ("chimeric antigen receptor"[tw] OR "virus-specific"[tw])
  ```
- `u3`
  ```
  Beatty GL[au] AND mesothelin[tw] AND (mRNA[tw] OR "chimeric antigen receptor"[tw])
  ```
- `u4`
  ```
  ("PSCA"[tw] OR "prostate stem cell antigen"[tw]) AND "chimeric antigen receptor"[tw] AND ("phase 1"[tw] OR trial[tw])
  ```
- `u5`
  ```
  Thistlethwaite FC[au] OR ("CEA"[tw] AND "chimeric antigen receptor"[tw] AND ("phase I"[tw] OR "first-in-man"[tw]) AND (colorectal[tw] OR "carcinoembryonic"[tw]))
  ```
- `u6`
  ```
  ("anti-CD20"[tw] OR rituximab[tw]) AND ("KLH"[tw] OR "keyhole limpet"[tw] OR "neoantigen challenge"[tw] OR "primary immunization"[tw] OR "de novo antibody"[tw] OR "T-dependent antigen"[tw])
  ```
- `u7`
  ```
  ("germinal center"[tw] OR "lymph node"[tw] OR "tissue-resident"[tw] OR spleen[tw]) AND (rituximab[tw] OR "anti-CD20"[tw]) AND ("incomplete depletion"[tw] OR "residual B cells"[tw] OR "depletion of B cells"[tw] OR "resistance to depletion"[tw])
  ```
- `u8`
  ```
  ("chimeric antigen receptor"[tw] OR "CAR T"[tw]) AND ("cyclophosphamide"[tw] AND "fludarabine"[tw]) AND ("lymphodepletion"[tw]) AND ("B cell"[tw] OR "humoral"[tw] OR "antibody"[tw] OR "immunogenicity"[tw])
  ```
- `u9`
  ```
  ("mycophenolate"[tw] OR "tacrolimus"[tw] OR "sirolimus"[tw] OR "rapamycin"[tw] OR "belatacept"[tw] OR "abatacept"[tw] OR "CTLA4-Ig"[tw]) AND ("anti-drug antibod*"[tw] OR "antibody formation"[tw] OR "immune tolerance"[tw]) AND ("gene therapy"[tw] OR "cell therapy"[tw] OR "transgene"[tw] OR "biologic*"[tw])
  ```
- `u10`
  ```
  ("humanized"[tw] OR "fully human"[tw]) AND "chimeric antigen receptor"[tw] AND (retreatment[tw] OR "second infusion"[tw] OR "anti-CAR"[tw] OR "anti-murine"[tw] OR immunogenic*[tw]) AND ("solid"[tw] OR glioma[tw] OR sarcoma[tw] OR neuroblastoma[tw] OR myeloma[tw])
  ```

