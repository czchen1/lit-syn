# 04 — Checkpoint blockade, cytokine/innate agonists, and TME/metabolic immunomodulation

Buckets: `checkpoint` (largest bucket in the corpus), `cytokine_innate`, and `tme_metabolic` (largest *preclinical* bucket after kinase inhibitors). Read together they describe one programme: **PD-(L)1 blockade is the backbone, and almost everything else is an attempt to fix the ~70–80% of patients it does not durably help.**

## 1. Practice-relevant checkpoint trials in the window

- **Perioperative/curative-intent intensification.** Adjuvant nivolumab vs observation in resected NSCLC (*JAMA*, PMID 42224490); nivolumab with chemoradiotherapy ± ipilimumab in stage III NSCLC (*Nat Cancer*, PMID 42129521); atezolizumab in early TNBC (NSABP B-59/GeparDouze, *Nat Med*, PMID 42680950); cemiplimab + fianlimab (LAG-3) with neoadjuvant chemotherapy in high-risk HER2− breast cancer (I-SPY2, *JAMA Oncol*, PMID 42530945); perioperative tislelizumab + chemotherapy in gastric cancer (*Cancer Cell*, PMID 42456653); neoadjuvant toripalimab ± celecoxib in dMMR/MSI-H disease (*Lancet Oncol*, PMID 42385761).
- **First-line combinations in advanced disease.** Benmelstobart + anlotinib vs pembrolizumab in PD-L1+ NSCLC (CAMPASS, *Lancet Oncol*, PMID 41825453); tiragolumab (TIGIT) + atezolizumab + chemotherapy (SKYSCRAPER-06, *JAMA Oncol*, PMID 42060297); serplulimab ES-SCLC secondary analysis (PMID 42240984); tislelizumab 3-year nasopharyngeal follow-up (RATIONALE-3, PMID 41746630); durvalumab/tremelimumab ± lenvatinib with TACE in HCC (*Lancet Oncol*, PMID 42636832); pembrolizumab ± olaparib maintenance (PMID 42705254); first-line zolbetuximab + mFOLFOX6 + nivolumab in CLDN18.2+ gastric cancer (*Nat Med*, PMID 41840238).
- **Route and schedule as variables.** Intratumoural anti-CTLA-4 with intravenous anti-PD-1 (*Nature*, PMID 42056527); intrathecal nivolumab for leptomeningeal disease (IT-PD1/NOA-26, *Nat Cancer*, PMID 42243276); anti-LAG-3 ± anti-PD-1 in recurrent glioblastoma (*Nat Med*, PMID 42432293); time-of-day administration analyses (PMID 42134900, PMID 42471484) — a still-unresolved chronotherapy signal that recurs across several cohorts.
- **New axes entering the clinic.** Sotigalimab (CD40 agonist) intratumourally with pembrolizumab, with abscopal activation of antigen-presenting cells (*Cancer Discov*, PMID 42013310); quemliclustat (CD73) + chemotherapy ± zimberelimab in pancreatic cancer (*Nat Med*, PMID 41912809); adenosine-receptor antagonists muvadenant/M1069 (PMID 42102781) and INCB106385 (PMID 42201333); cibisatamab + FAP-4-1BBL in MSS colorectal cancer (*Nat Med*, PMID 42010119); BO-112 (intratumoural dsRNA) with hypofractionated radiation ± nivolumab in sarcoma (*Cancer Discov*, PMID 41784328).

## 2. Human-sample resistance biology

The most transferable insights come from on-treatment human tissue rather than models: spatiotemporal immune determinants of response to immune rechallenge in cervical cancer (*Cancer Discov*, PMID 41511850); cellular neighbourhoods governing T-cell infiltration after anti-CTLA-4 in anti-PD-1-resistant melanoma (*Cancer Discov*, PMID 42013417); PD-1 blockade unleashing HBV-related intratumoural B-cell responses in HCC (*Cancer Cell*, PMID 42462708); gut microbiome association with recurrence-free survival under adjuvant checkpoint blockade in resected melanoma (*Cell*, PMID 41999744; see notes/05).

Toxicity biology is being mapped at the same resolution: organ-metastatic landscape shaping site-specific irAEs in NSCLC (PMID 41851435) and irAE/discontinuation analyses from KEYNOTE-355 (PMID 42362563).

## 3. Cytokine and innate agonists: still a delivery problem

`cytokine_innate` is predominantly preclinical, and the recurring structure is *engineering a potent-but-toxic cytokine into a locally-acting form*: IL-2/IL-15/IL-21 scaffolds and fusions, TLR7/8 agonist conjugates, CD40 agonists, STING and interferon gene therapy, and engineered bacteria as cytokine factories. Clinically, the class appears mostly as combination partners (oncolytic + IL-2-free regimens, notes/05) or as intratumoural agents (BO-112, sotigalimab, above). The honest summary is that **no systemic cytokine agent in this window produced a practice-changing clinical result; the innovation is entirely in localisation.**

## 4. TME and metabolic therapy

`tme_metabolic` is the second-largest preclinical mass in the corpus and the most heterogeneous. Recurring, reproducible themes:

- **Adenosine/purinergic suppression** (CD73, A2A/A2B, ATP–P2RY2–PGE2) — the most clinically advanced TME axis.
- **Myeloid reprogramming** — TAM polarisation, macrophage metabolic checkpoints (e.g. ALDH2 silencing CXCL9, PMID 42168200), CSF1R combinations.
- **Amino-acid and lipid metabolism as immune levers** — dietary sulfur amino acids boosting an NKT–XCL1–cDC1 circuit (*Immunity*, PMID 42190649); arginine-metabolism targeting reversing bone immunosuppression in ARID1A-deficient TNBC (PMID 42191692); low-protein diet acting through microbiota-derived UDP-galactose (*Nat Cancer*, PMID 42608587).
- **Mitochondrial and redox targeting** — mitochondrial peroxiredoxin-3 taken from preclinical characterisation into a phase 1 (*Nat Commun*, PMID 42448681); a ketogenic-diet feasibility randomisation in endometrial cancer (PMID 42192131) as the dietary-intervention edge case.
- **Stromal/vascular normalisation** — FAP-directed agonists and conjugates, LOX/collagen axes, vasculogenic mimicry (CVM-1118 phase 2, PMID 42393461).

## Caveat specific to these buckets

`checkpoint` and `tme_metabolic` are the buckets where the modality classifier is least crisp: a trial of chemotherapy + PD-1 is filed under `checkpoint`, and a metabolism paper whose readout is T-cell function may be filed under `tme_metabolic` rather than `checkpoint`. Use the `also:` tags in `topics` when a strict modality partition matters.
