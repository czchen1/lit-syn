# 05 — Cancer vaccines, oncolytic viruses and bacteria, microbiome interventions

Buckets: `cancer_vaccine`, `oncolytic_virus`, `microbiome`. Together the smallest immunotherapy block in the corpus and the most exploratory: clinical entries are almost entirely phase 1/2, single-arm or small randomised, with immune-response readouts rather than survival endpoints.

## 1. Cancer vaccines

**Personalised neoantigen platforms are the centre of clinical activity.**

- Adjuvant personalised multivalent neoantigen **DNA** vaccination in MGMT-unmethylated glioblastoma (phase 1, PMID 42120910) and personalised synthetic-long-peptide/DNA vaccines inducing neoantigen-specific T cells in pancreatic cancer (PMID 42696575); the intramuscular personalised SLP IMPACT trial in advanced disease (PMID 42095629); personalised neoantigen-pulsed autologous dendritic cells in newly diagnosed GBM (phase Ib, PMID 42401550).
- **Shared-driver vaccines as cancer interception** — first-in-human mutant-KRAS vaccine in high-risk cohorts *before* cancer develops (PMID 42458705) is conceptually the most novel clinical entry in the bucket.
- **Defined-antigen vaccines in pediatrics and hematology** — anti-NeuGcGM3 anti-idiotype racotumomab in high-risk neuroblastoma (PMID 42136000); WT1 peptide-dosing emulsion in recurrent/refractory DIPG (PMID 42176363); WT1 vaccine as post-allo-HCT maintenance in pediatric acute leukemia (PMID 42308229).
- **Long-term and combination readouts of older platforms** — pTVG-HP DNA vaccine survival analysis in PSA-recurrent prostate cancer (PMID 42303538); melanoma helper-peptide vaccine ± agonistic anti-CD27 (PMID 41960901); GM-CSF and two-site vaccination effects on multipeptide melanoma vaccination (PMID 41849224); heat-conditioned tumour-lysate vaccine TRIMELVax in anti-PD-1-refractory melanoma (PMID 42062531); tri-antigen IGFBP-2/HER2/IGF-IR vaccine (PMID 42082270); mammaglobin-A DNA vaccine with neoadjuvant endocrine therapy (PMID 41650206); therapeutic HPV vaccine in a placebo-controlled phase I/II (PMID 42249801).
- **Why vaccines fail** — single-cell dissection of persistent tumour antigens in non-responders, pointing to TAA-targeted vaccination as salvage (PMID 42019971), is the most useful mechanistic clinical paper here.

Preclinically the field splits into *antigen discovery* (cryptic/non-canonical peptides, splice- and retained-intron-derived neoantigens, tumour glycopeptides) and *platform engineering* (self-amplifying and circular RNA, LNP and nanoparticle scaffolds, lymph-node-targeting adjuvants) — the RNA/LNP side is covered in notes/08.

## 2. Oncolytic viruses and gene-mediated cytotoxic therapy

The single strongest randomised result is not a classical oncolytic but a gene-mediated cytotoxic immunotherapy: **aglatimagene besadenovec (CAN-2409) with radiotherapy in localised prostate cancer**, a phase 3 double-blind trial (*Lancet Oncol*, PMID 42225101) — filed under `radiotherapy` because radiation is the primary modality in the trial design.

Clinical oncolytic reports are phase 1/2 and mostly CNS or intraperitoneal:

- Recurrent glioma — engineered oncolytic HSV-1 ON-01 (phase 1/2, PMID 41527280); systemic immune correlates of long-term survival after Delta-24-RGD (DNX-2401) (PMID 41609523).
- Ovarian — Olvi-Vec (vaccinia) reversing platinum resistance (PMID 42383154).
- Combination with definitive chemoradiation — OBP-301 in locally advanced esophageal cancer (NRG-GI007, PMID 42269787).
- Systemic administration — fully intravenous split-dose oncolytic adenovirus TILT-123 in advanced solid tumours (PMID 42136030), with an immune-cytokine signature predicting survival in melanoma (PMID 42624531). Intravenous delivery remains the field's hardest problem, and these are the papers that address it directly.
- Armed vectors as TME engineering — LOAd703 (TMZ-CD40L/4-1BBL-armed adenovirus) in solid malignancies (LOKON002, PMID 42053989); an oncolytic HSV-2 repolarising tumour-associated macrophages (PMID 42217049).

Preclinical work is dominated by **arming** (IL-12, IL-15/IL-15Rα, GM-CSF, CD3 engagers, checkpoint scFvs), **shielding for systemic delivery** (polymer/carrier-cell-mediated), and **engineered bacteria** (attenuated *Salmonella*, *E. coli* Nissle, *Listeria*) acting as in-situ cytokine or antigen factories — where the operative mechanism reported is adaptive priming rather than direct lysis.

## 3. Microbiome

Two clinical results are decision-relevant:

- **Exposures that erode immunotherapy benefit** — proton-pump inhibitors and antibiotics after chemoradiotherapy in stage III NSCLC (*Lancet Oncol*, PMID 42398520), and gut microbiome composition associated with recurrence-free survival under adjuvant checkpoint blockade in resected melanoma (*Cell*, PMID 41999744).
- **Deliberate microbiome modification** — FMT in checkpoint-resistant solid cancers (phase 2, PMID 42476727) and FMT + anti-PD-1 in refractory MSS gastric cancer (PMID 41871875); *Bifidobacterium animalis* subsp. *lactis* V9 overcoming immunochemotherapy resistance in NSCLC (PMID 42685222); 2'-fucosyllactose modifying the gut microbiome after pediatric bone-marrow transplant (*Blood*, PMID 42622257); microbiome dynamics under neoadjuvant chemotherapy (PMID 42218533) and perioperative microbiome restructuring in colorectal surgery (PMID 42482993).

Preclinically, microbiota-derived metabolites are treated as pharmacology: microbiota-derived UDP-galactose mediating the antitumour effect of a low-protein diet in pancreatic cancer (*Nat Cancer*, PMID 42608587), plus short-chain fatty acid, bile-acid and indole axes acting on T-cell and myeloid function, defined consortia, engineered strains, and intratumoural bacteria as direct targets.

## Reading guidance

Outside CAN-2409, there is no phase 3 evidence in these buckets in this window. Immunogenicity endpoints (T-cell response rates, cytokine signatures) are the norm and do not establish clinical benefit. Bucket boundaries are deliberately fuzzy — a cytokine-armed bacterium can plausibly sit in `oncolytic_virus`, `microbiome` or `cytokine_innate`; `topics` records secondary modalities as `also:<bucket>`.
