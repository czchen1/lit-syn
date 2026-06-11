# GD2 CAR-effector clinical trials: index by lab/group

This note indexes every **published GD2-targeting CAR-effector clinical trial** in the
collection, grouped by the originating lab/group. It is the human-trial companion to the
machine-readable [`index_by_lab.tsv`](../index_by_lab.tsv) and feeds the comparative tables in
[`11_clinical_management_plan.md`](11_clinical_management_plan.md).

Scope note: only trials in which an **engineered cell** carries the GD2 (or O-acetyl-GD2) CAR
are listed; dinutuximab/naxitamab antibody trials are excluded. Manufacturing-correlate papers
that were tagged `clinical_trial` in `index.tsv` but report process/biology rather than a distinct
trial (Stroncek 2016/2017 NIH elutriation & myeloid-inhibition studies; Tanaka 2017 VZV-CTL)
are noted under their parent group.

Trial registration IDs were extracted from the paper PDFs and reconciled against
ClinicalTrials.gov; the structured protocol records for the registered trials are archived under
[`../protocols/clinicaltrials_gov/`](../protocols/clinicaltrials_gov/).

---

## 1. Baylor College of Medicine — Center for Cell and Gene Therapy (CAGT)
*Texas Children's Hospital / Houston Methodist, Houston, USA. Brenner, Heslop, Rooney, Metelitsa, Heczey, Louis.*

The longest-running GD2 CAR program; it produced the first-in-human GD2 CAR-T trial and the
first-in-human CAR-NKT trial.

| Trial (NCT) | Product | Construct | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- | --- |
| **NCT00085930** | 1st-gen GD2 CAR | 14g2a-CD3ζ, retroviral, no costim | Autologous ATC **+** EBV-specific CTL | r/r & high-risk NB | Pule 2008 *Nat Med* (foundational, not in corpus); **Louis 2011** *Blood* (PMID 21984804); **Li 2025** *Nat Med* 18-yr follow-up (PMID 39962287) |
| **NCT01822652 (GRAIN)** | iC9-GD2-CAR3 | 14g2a-CD28-OX40-CD3ζ + iCasp9, retroviral | Autologous T cells | r/r NB | **Heczey 2017** *Mol Ther* (PMID 28602436) — ± pembrolizumab |
| **NCT03294954 (GINAKIT2)** | GD2-CAR.15 NKT ("GINAKIT cells") | 14g2a-CD28-CD3ζ + transgenic IL-15, retroviral | Autologous Vα24-invariant **NKT** cells | r/r NB | **Heczey 2020** *Nat Med* interim (PMID 33046868); **Heczey 2023** *Nat Med* update (PMID 37188782); **Tian 2025** lethal-hyperleukocytosis case report (PMID 39800376) |
| **NCT01953900** | iC9-GD2-CAR-VZV-CTL | 14g2a-CD28-OX40-CD3ζ + iCasp9, retroviral | Autologous VZV-specific CTL | r/r GD2+ sarcoma | **Tanaka 2017** *Clin Cancer Res* (PMID 28183713) |
| NCT03635632 (pipeline) | C7R-GD2.CART | GD2 CAR + constitutive IL-7Rα (C7R) | Autologous T cells | r/r NB / solid | (no mature clinical paper in corpus) |

The full **GINAKIT2 study protocol** is archived as `supplements/heczey_2020_pmid33046868_supp.pdf`
(includes CRS/neurotoxicity grading appendices, lymphodepletion rationale, dose-escalation
schema and pain-assessment plan) — the single most detailed primary-source protocol document in
the collection.

---

## 2. IRCCS Ospedale Pediatrico Bambino Gesù — Rome
*Locatelli, Quintarelli, Del Bufalo, De Angelis, Caruana.*

Producer of **GD2-CART01**, the most widely cited clinical-stage GD2 CAR-T product.

| Trial | Product | Construct | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- | --- |
| **NCT03373097** (phase 1/2) | **GD2-CART01** | 14.G2a-CD28-OX40-CD3ζ (3rd gen) + iCasp9, SFG retroviral | Autologous T cells | high-risk r/r NB (+ exploratory GD2+ solid) | **Del Bufalo 2023** *NEJM* (PMID 37018492); **Locatelli 2025** *Nat Med* final (PMID 40841488) |
| Hospital exemption | **ALLO_GD2-CART01** | same construct, **allogeneic** donor | HLA-matched intrafamilial donor T cells | r/r NB without feasible autologous product | **Quintarelli 2025** *Nat Med* (PMID 39815015) |

Construct-defining and platform-extension companions (with supplements): Quintarelli 2018
*OncoImmunology* (2G vs 3G design selection); Caforio 2021 *JITC* (medulloblastoma);
Tumino 2021 (γδ variant context); Ciccone 2024 *Clin Cancer Res* (medulloblastoma, NCT05298995).
The ALLO_GD2-CART01 supplement (`supplements/quintarelli_2025_pmid39815015_supp.pdf`) documents
the clinical **iCasp9 activation to abort grade 4 CRS** in the autologous program
(personal communication, Locatelli).

---

## 3. Stanford University
*Mackall, Monje, Majzner.*

The CNS-delivery program; defined **TIAN** (tumour inflammation-associated neurotoxicity).

| Trial (NCT) | Product | Construct | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- | --- |
| **NCT04196413** | **GD2CART (DMG)** | 14g2a-CD8h/TM-4-1BB-CD3ζ + iCasp9, retroviral; CliniMACS Prodigy + IL-7/IL-15 + dasatinib | Autologous CD4/CD8 T cells | H3K27M+ DIPG, spinal & thalamic DMG | **Majzner 2022** *Nature* interim (PMID 35130560); **Monje 2025** *Nature* final (PMID 39537919) |

Route is **IV first, then intracerebroventricular (ICV) via Ommaya** for redosing. Rituximab is
incorporated into lymphodepletion (750 mg/m² on days −6/−5) to blunt anti-CAR humoral responses
and enable redosing. Companion preclinical paper: Mount 2018 *Nat Med*.

---

## 4. UCL / Great Ormond Street Hospital / Cancer Research UK / Autolus
*Pule, Anderson, Straathof.*

| Trial (NCT) | Product | Construct | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- | --- |
| **NCT02761915** | **1RG-CART** | huK666 GD2 scFv-CD8-4-1BB-CD3ζ (2nd gen) + **RQR8** epitope, retroviral | Autologous T cells | r/r NB | **Straathof 2020** *Sci Transl Med* (PMID 33239386) |

Distinctive design choices: a humanized (huK666) scFv to limit anti-murine immunogenicity, an
**RQR8** marker/safety element (CD20 + CD34 epitopes) making the cells **rituximab-ablatable**,
and a trial design that **escalated lymphodepletion intensity (phased) rather than cell dose**.

---

## 5. 4SCAR platform — Lung-Ji Chang (China)
*Zhujiang Hospital / Southern Medical University / Shenzhen Geno-Immune Medical Institute.*

| Trial (NCT) | Product | Construct | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- | --- |
| **NCT02765243** | **4SCAR-GD2** | GD2-CD28-4-1BB-CD27-CD3ζ (4th gen) + iCasp9, lentiviral | Autologous T cells | refractory/recurrent NB | **Yu 2022** *J Cancer Res Clin Oncol* (PMID 34724115) |
| Geno-Immune registry | 4SCAR-GD2 (GBM) | same 4th-gen + iCasp9, lentiviral | Autologous T cells | GD2+ glioblastoma | **Liu 2023** *Mol Cancer* (PMID 36617554) |

---

## 6. CARPETS — University of Adelaide / Royal Adelaide Hospital (Australia)
*Gargett, Brown.*

| Trial | Product | Construct | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- | --- |
| **ACTRN12613000198729 (CARPETS)** | **GD2-iCAR-PBT** | 14g2a-CD28-OX40-CD3ζ + iCasp9, retroviral | Autologous peripheral-blood T cells | metastatic GD2+ melanoma & other solid | **Gargett 2024** *JITC* (PMID 38754916); Gargett 2016 *Mol Ther* (PD-1/AICD, PMID 27019998) |

Three sequential cohorts: (1) CAR-T alone, (2) Cy/Flu + CAR-T, (3) Cy/Flu + CAR-T + pembrolizumab.

---

## 7. Children's Mercy Hospital, Kansas City
| Trial (NCT) | Product | Cells | Disease | Key papers |
| --- | --- | --- | --- | --- |
| **NCT01460901** | donor tri-virus-specific GD2 CAR | allogeneic donor multivirus-specific CTL | r/r NB post-allo-HSCT | (pilot; no primary clinical paper in corpus) |

---

## Cross-reference: trial → primary effector lineage

| Effector cell | Trials |
| --- | --- |
| Autologous αβ T cells | Baylor GRAIN; Bambino Gesù GD2-CART01; Stanford GD2CART; UCL 1RG-CART; 4SCAR-GD2; CARPETS |
| Autologous αβ T + EBV/VZV-specific CTL | Baylor NCT00085930, NCT01953900 |
| Vα24-invariant NKT | Baylor GINAKIT2 |
| Allogeneic donor T cells | Bambino Gesù ALLO_GD2-CART01; Children's Mercy NCT01460901 |
