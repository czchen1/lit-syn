# 01 — Adoptive and engineered cell therapy; transplantation

Buckets: `cell_therapy` and `transplant`. Together these are the most clinically mature part of the corpus: `cell_therapy` carries the largest phase-1 count of any modality, which is the signature of a field where product engineering, not indication expansion, is the rate-limiting step.

## 1. CAR-T moves earlier in the disease course

The clearest trend of the window is CAR-T being tested *before* the classic relapsed/refractory setting:

- **Smouldering myeloma.** Ciltacabtagene autoleucel in high-risk smouldering multiple myeloma (CAR-PRISM, *Nat Med*, PMID 42010117) — treating before overt disease, with the attendant risk/benefit argument.
- **First-line and consolidation lymphoma.** Lisocabtagene maraleucel plus ibrutinib in R/R CLL/SLL (TRANSCEND CLL 004, *Blood*, PMID 42520199) and 3-year TRANSCEND FL durability (PMID 42462111) push toward earlier lines; blinatumomab consolidation in high-risk Ph− B-ALL (GRAALL-2014/B-QUEST, PMID 42126414) is the engager analogue.
- **Pediatric leukemia with dual targeting.** Bicistronic CD19/CD22 CAR-T in pediatric B-ALL (*JAMA Oncol*, PMID 42690647).

## 2. Product engineering: dual antigen, armouring, knockdown, allogeneic, in vivo

Phase 1 activity is dominated by construct innovation rather than new diseases:

- **Dual/multi-antigen.** Anti-BCMA/GPRC5D CAR-T for extramedullary myeloma (PMID 42166352); concurrent BCMA + GPRC5D CAR-T (PMID 42413007); multi-antigen T cells for pediatric CNS tumours (*Nat Med*, PMID 42380677).
- **New solid-tumour targets.** GPC3 CAR-T armoured with dnTGFβRII for HCC (*Nature*, PMID 42457964); GPNMB-directed CAR-T in MiT/TFE fusion tumours (*Nat Cancer*, PMID 42387022) with a matching AI-discovery preclinical paper (*Cell*, PMID 42349383) and a glioblastoma myeloid/tumour dual-targeting paper (*Nature*, PMID 42386964); B7-H3 CAR-T delivered intracranially for recurrent GBM (*Nat Med*, PMID 42562965); uPAR as a recurrent-GBM target (*Sci Transl Med*, PMID 42127223; *Cell*, PMID 41916312).
- **Cytokine/checkpoint armouring and knockdown.** PD-1/TIGIT-knockdown CD19 CAR-T (anbalcabtagene autoleucel, PMID 42284198); ultralow-dose IL-10-expressing CAR-T in DLBCL (*JAMA Oncol*, PMID 42490071).
- **Off-the-shelf / gene-edited.** Base-edited "off-the-shelf" CAR33 for AML (BE-CAR33, *Sci Transl Med*, PMID 42616838); triple-knockout allogeneic BCMA CAR-T (CT0590, PMID 42275247); CRISPR-Cas9 CD33-deleted transplant with gemtuzumab maintenance (*Nat Med*, PMID 42120728) — a genotype-engineered *host* rather than a genotype-engineered product.
- **In vivo CAR generation.** Anti-BCMA CAR-T generated in vivo in R/R myeloma (*Nat Med*, PMID 41882404), plus preclinical erythrocyte-mediated mRNA CAR-myeloid delivery (*Sci Transl Med*, PMID 41880522), liposomal in-situ CAR-alveolar-macrophage reprogramming (*Nat Commun*, PMID 42285952) and FAP-CAR mRNA LNPs against pancreatic tumours (PMID 41686204). This is where cell therapy and the RNA/delivery bucket (notes/08) merge.

## 3. Why CAR-T fails: the preclinical agenda

Preclinical `cell_therapy` work in this window is almost entirely about the *fitness and context* of the product rather than new binders:

- **Metabolic fitness** — on-demand GLUT3 expression improves CAR-T efficacy in GBM models (PMID 41984929); iron-mediated ferroptosis impairs CAR-T function (*Nat Cancer*, PMID 42270901); metabolite-sensing receptors for NK/T cells in solid tumours (*Nat Immunol*, PMID 41872506).
- **Host and niche dependence** — the endogenous immune compartment determines outcome after CAR-T in recurrent GBM (*Cell*, PMID 42296961); tumour irradiation dresses dendritic cells to sustain CAR-T (*Nat Cancer*, PMID 42174275); extracellular ATP–P2RY2–PGE2 signalling drives adaptive resistance (*Immunity*, PMID 42392075).
- **Product-intrinsic transcriptional programs** — NF-κB-driven programs predict durability of myeloma CAR-T response (*Blood*, PMID 42275255); NFIL3 as a driver of T-cell dysfunction from chronic in vivo/in vitro screens (*Cancer Discov*, PMID 41747243).
- **Avidity and co-stimulation engineering** — ferritin aggregation cell engagers for CAR avidity (*Cell*, PMID 41806835); harnessing the CD2 axis (*Blood*, PMID 41490267); CAR-engineered granulocyte-monocyte progenitors (*Cell*, PMID 42320470).

## 4. Long-horizon clinical safety and real-world outcomes

The `clinical_other` rows carry the pharmacovigilance signal that trials cannot: decade-long CD19 CAR-T persistence (*Nat Med*, PMID 42575986); CD4⁺ CAR-T expansion associated with non-ICANS neurotoxicity after cilta-cel (*Sci Transl Med*, PMID 42525783); patient-reported vs physician-assessed adverse events after CAR-T (*Lancet Haematol*, PMID 42285114); blinatumomab non-response predicting poor post-brexu-cel survival (*Blood*, PMID 41643192).

## 5. Transplantation: conditioning intensity and the venetoclax era

`transplant` is mostly clinical and mostly about **making conditioning gentler while keeping relapse control**:

- Total marrow and lymphoid irradiation with cyclophosphamide/etoposide before HCT (*Lancet Haematol*, PMID 42150590); randomised busulfan fractionation with fludarabine/cladribine (PMID 42285355); myeloablative treosulfan/fludarabine (FT14) (PMID 42342968).
- **Venetoclax has moved into conditioning and maintenance** — venetoclax-augmented RIC with PTCy and ven/aza maintenance in poor-risk MDS/AML (PMID 42617873); venetoclax-enhanced RIC in patients ≥55 (PMID 42457583); venetoclax in flu/mel conditioning for older AML/MDS (PMID 42159161).
- **GVHD prophylaxis converging on post-transplant cyclophosphamide**, with ATG comparisons (PMID 42629427) and registry-scale PTCy-vs-tacrolimus/methotrexate comparisons (PMID 41895692); permissive HLA-DPB1 mismatch plus PTCy associated with reduced relapse (*Leukemia*, PMID 41803402).
- **Cell therapy after transplant** — donor-derived anti-CD33 CAR-T (VCAR33) post-allo-HCT (*Blood*, PMID 41636724); Orca-T precision-engineered graft correlates (PMID 41758930).

## Reading guidance

Cell-therapy phase 1 reports in this window are typically 10–40 patients; treat single-arm ORR/CR figures as hypothesis-generating. The dual-antigen and in-vivo-CAR results are the most likely to be revised as follow-up matures.
