# 09 — Conventional chemotherapy, tumour-microenvironment/metabolic therapy, and drug repurposing

Buckets: `chemo_conventional` (second-largest bucket overall, and the largest source of phase 3 trials), `tme_metabolic`, `repurposed`, plus the small `microbiome` bucket (covered with vaccines/oncolytics in note 05).

## 1. Chemotherapy: still where most randomised evidence is generated

The chemotherapy bucket's phase 3 trials are mostly *optimisation* — regimen intensity, sequencing, de-escalation and route — rather than new agents:

- **ctDNA-guided adjuvant chemotherapy** is the clearest new idea: chemotherapy for ctDNA-positive stage II colon cancer (CIRCULATE AIO/ABCSG, *Ann Oncol*, PMID 42225236); post-adjuvant chemotherapy in ctDNA-positive resected colorectal cancer, phase 3 (*Nat Med*, PMID 42260101); ctDNA-guided intensification in rectal cancer (PMID 41556959).
- **Colorectal and peritoneal disease:** tumour debulking with chemotherapy in multiorgan metastatic CRC (ORCHESTRA, *JAMA*, PMID 41837962); perioperative systemic therapy vs surgery alone for peritoneal-only metastases (CAIRO6, *Lancet Oncol*, PMID 42372745); gastrectomy + CRS/HIPEC vs systemic therapy alone in gastric peritoneal disease (*Lancet Oncol*, PMID 42419336); intraperitoneal + IV paclitaxel plus S-1 in gastric peritoneal metastasis, phase 3 (*JAMA Oncol*, PMID 42166134); high-dose vitamin D3 added to standard treatment in mCRC (SOLARIS, *JAMA*, PMID 42545685; no PFS benefit).
- **Rectal and GI radiochemotherapy:** total neoadjuvant therapy with long-course RT vs CRT (*JCO*, PMID 42492015); irinotecan added to preoperative CRT (ARISTOTLE, *Lancet Oncol*, PMID 42508427); adjuvant chemotherapy ± CRT in pancreatic head adenocarcinoma (*JCO*, PMID 42456089); adjuvant SOX vs S-1 in gastric cancer (CAPITAL, PMID 42600610); oral vs IV paclitaxel in gastric cancer (PMID 42617423); TACE + thermal ablation in HCC (TORCH, *JAMA Oncol*, PMID 42530948).
- **Breast:** anthracycline→taxane vs taxane-carboplatin (neo)adjuvant, phase 3 (*Ann Oncol*, PMID 42218963); oral paclitaxel DHP107 vs IV weekly paclitaxel (OPTIMAL, PMID 41833903); intensified vs standard chemotherapy then olaparib in HRD disease (PMID 42372741); eribulin vs taxane with dual HER2 blockade (PMID 42480197); fulvestrant vs capecitabine maintenance (PMID 42168151); neoadjuvant palbociclib + ET vs chemotherapy (PMID 41951647); ovarian reserve as a marker of adjuvant chemotherapy benefit (PMID 42613139).
- **Lung:** gotistobart or docetaxel in squamous NSCLC (PRESERVE-003 stage 1, *Nat Med*, PMID 41896648); LIBRETTO-431 chemoimmunotherapy comparator outcomes in RET-fusion lung cancer (PMID 42431264).
- **Head and neck / gynaecological:** weekly vs tri-weekly cisplatin CRT (PMID 41812622; JCOG1008 long-term, PMID 42361282); adjuvant metronomic capecitabine in nasopharyngeal carcinoma (*Nat Cancer*, PMID 42380630); induction TPF vs adjuvant PF (PMID 42604670); relacorilant + nab-paclitaxel OS in platinum-resistant ovarian cancer (ROSELLA, *Lancet*, PMID 41974149); cisplatin CRT non-inferiority in cervical cancer (ConCERT, PMID 42636269); adjuvant 5-FU-platinum vs paclitaxel-platinum in penile cancer (PMID 42636270).
- **Hematology:** tafasitamab + lenalidomide + R-CHOP in high-risk DLBCL, phase 3 (*Lancet*, PMID 42217458); SWOG S0016 15-year follow-up (PMID 41746629); low-dose pediatric AML induction (PMID 41812214); CPX-351 vs standard induction in pediatric AML (AAML1831, *JCO*, PMID 42497367); DA-EPOCH-R + venetoclax (PMID 42660130); high-dose chemotherapy + ASCT vs non-myeloablative consolidation in PCNSL (*Lancet*, PMID 42486133).
- **Sarcoma and pediatric solid tumours:** Euro-EWING99 long-term (PMID 42537000); zoledronic acid added to Ewing consolidation (EE2012, PMID 41832299); trabectedin ± regional hyperthermia (PMID 41962307); ependymoma post-irradiation chemotherapy (PMID 41423745).
- **Pharmacology and dosing:** PK-guided melphalan (PMID 42654041); metronomic capecitabine combinations (PMID 41986320); paricalcitol added to gemcitabine/nab-paclitaxel in pancreatic cancer (*Nat Cancer*, PMID 42185478; safety run-in with paired biopsies showing stromal/CD8 modulation, filed here but really a TME study).

The clinical_other layer beneath this is large: real-world cohorts, secondary analyses of completed trials, and Chinese-language regimen comparisons. They are retained for completeness but should not be weighted with the randomised readouts.

## 2. Tumour-microenvironment and metabolic therapy

`tme_metabolic` is ~1,300 records, ~90% preclinical. Clinically it is thin and mostly combination arms inside IO trials (oleclumab/CD73 with durvalumab and SBRT, *Nat Med*, PMID 42350643; adenosine-axis and TGF-β trap agents in note 02/04). The preclinical literature is coherent around a few axes:

1. **Myeloid reprogramming:** CSF1R, CD40 agonism, TREM2, SIRPα/CD47, MARCO and macrophage-polarising nanoparticles; consistent across models, inconsistent in trials.
2. **Fibroblast/stroma:** FAP-directed radioligands and CAR-T (notes 01, 07); LRRC15, hyaluronidase and Hedgehog-pathway stroma modulation revisited with better patient selection.
3. **Metabolic checkpoints:** IDO/TDO revival via combination logic, glutaminase and glutamine antagonists (DRP-104-like prodrugs), arginase, lactate/MCT1-4, PI3Kδ/γ myeloid inhibitors; ketogenic/fasting-mimicking diets as chemotherapy sensitisers with early randomised signals.
4. **Ferroptosis/cuproptosis inducers**, GPX4 inhibition and iron-loaded nanocarriers as a distinct sub-literature that overlaps `nanomedicine_delivery`.
5. **Neuro-immune and stress-axis modulation:** β-blockade (propranolol, PMID 42662047), angiotensin-pathway modulation (PMID 42081750), and sympathetic denervation.
6. **Angiogenesis** — anti-VEGF backbone combinations (bevacizumab with PD-1/VEGF bispecifics in note 02; ramucirumab, PMID 42081056) plus normalisation strategies to improve drug penetration.

## 3. Drug repurposing and chemoprevention

The `repurposed` bucket (~250 records) is the least evidence-dense. Notable clinical entries: aspirin for cancer prevention in Lynch syndrome dose comparison (CaPP3, *Lancet Gastroenterol Hepatol*, PMID 42425127); metformin's Lac-Phe axis in prostate cancer (PMID 41942753) and enzalutamide + metformin (PMID 41862335); eflornithine for gastric precancerous lesions (PMID 41801147); itraconazole for basal cell carcinoma (PMID 42101092); GLP-1 receptor agonist outcomes in breast cancer/diabetes (PMID 41801847); high-dose vitamin C pharmacokinetics (PMID 42378816) and toxicity mitigation (PMID 41973719); ivermectin/mebendazole prospective observational cohort (PMID 42203321) — hypothesis-generating at best; curcumin/omega-3 lung chemoprevention imaging endpoints (PMID 42649879).

Preclinically, statins, metformin, disulfiram, antipsychotics, antihelminthics, SGLT2 inhibitors, and antihistamines recur; the field's structural problem — supraphysiological in-vitro concentrations — is unchanged in this window. Rows in this bucket with `evidence` = `preclinical` should be treated as leads, not evidence.

## 4. Cross-cutting observations

- The chemotherapy backbone remains the control arm in the majority of positive phase 3 trials in other buckets (ADC, bispecific, checkpoint, RAS). Reading `chemo_conventional` together with those buckets gives the comparator context.
- The TME literature is increasingly *combination-first*: fewer monotherapy claims, more triplets with checkpoint blockade or radiation.
- Repurposing is trending toward *prevention and interception* (Lynch aspirin, KRAS vaccines in note 05, eflornithine) rather than late-line treatment.
