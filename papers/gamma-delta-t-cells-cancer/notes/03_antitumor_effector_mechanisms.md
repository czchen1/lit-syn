# Antitumor effector mechanisms

Once a γδ T cell decides a target is "transformed/stressed," it kills and recruits in several complementary ways. The therapeutic appeal is that these mechanisms are largely **HLA‑independent** and often **redundant**, making escape by single‑pathway loss harder than for αβ T cells.

## 1. Granule‑mediated cytotoxicity
The dominant direct‑kill pathway: polarized release of **perforin** and **granzymes** induces target apoptosis. Activated Vγ9Vδ2 and Vδ1 cells are strongly granzyme‑B⁺/perforin⁺ after expansion. Granule exocytosis is the principal mechanism in most ex‑vivo‑expanded products used clinically.

## 2. Death‑receptor (extrinsic) killing
γδ cells express **TRAIL** and **FasL (CD95L)** and kill TRAIL‑R/Fas⁺ tumors independently of granules. This matters because it engages tumors that resist perforin and contributes to bystander killing. Studies dissecting γδ cytotoxicity against malignant pleural mesothelioma describe **three distinct mechanisms** operating in parallel (perforin/granule, death‑receptor, and pyroptosis‑linked) (PMID 37006249), and anti‑PD‑1 was reported to promote regression without necessarily improving pyroptosis (PMID 38077396) — illustrating mechanism‑level heterogeneity across tumors.

## 3. Antibody‑dependent cellular cytotoxicity (ADCC)
A large fraction of expanded γδ cells (especially Vγ9Vδ2) upregulate **CD16 (FcγRIIIa)** and can be armed with tumor‑targeting monoclonal antibodies to mediate **ADCC** — combining γδ adoptive transfer with rituximab (CD20), trastuzumab (HER2), cetuximab (EGFR), or anti‑GD2. This is one of the most clinically tractable combination strategies because it borrows approved mAbs (see `08_combinations_and_resistance.md`).

## 4. Cytokine secretion and immune orchestration
Activated antitumor γδ cells are major **IFN‑γ** and **TNF‑α** producers, which:
- directly inhibit tumor proliferation/angiogenesis,
- upregulate MHC and antigen‑processing machinery on tumors,
- and license dendritic cells and αβ T cell responses.
The opposite cytokine program — **IL‑17** — is protumor and is covered in `04_dual_role_and_protumor.md`.

## 5. Professional antigen presentation ("γδ T‑APC")
Vγ9Vδ2 cells can upregulate MHC‑II, CD80/CD86, and CCR7, acquire migratory/APC features, and **cross‑present** tumor antigens to CD8⁺ αβ T cells (Brandes et al., *Science* 2005). This positions γδ cells as a bridge that can **initiate** an adaptive antitumor response, not just execute one — an increasingly exploited rationale for combining γδ therapy with vaccines or antigen‑release (radiation, oncolytic virus).

## 6. NK‑receptor‑driven cytotoxicity
Via **NKG2D, DNAM‑1, NKp30/44/46**, γδ cells kill cells displaying stress ligands regardless of TCR engagement (see `02_antigen_recognition.md`). For Vδ1/DOT cells this is often the primary antitumor axis; e.g. **CD155/PVR–DNAM‑1** determines AML targeting by DOT cells (PMID 38437507), and KIRs define a potent effector program (PMID 42044172).

## Tumor‑microenvironment fitness as an effector variable
Effector output is only useful if the cell survives and functions inside the tumor. Recurring themes:
- **Lactate/acidosis:** Vδ1 cells show high lactic‑acid resistance and retain antitumor activity in acidic conditions (PMID 42106736), a Vδ1 advantage over Vγ9Vδ2.
- **Hypoxia, adenosine, TGF‑β, Tregs/MDSCs:** broadly suppress γδ effector function and can repolarize cells.
- **Exhaustion:** chronic stimulation drives PD‑1/TIM‑3/LAG‑3 expression; checkpoint blockade and armoring are used to counter this (see `08`).
- **Trafficking:** CXCR3 (PMID 42208977) and other chemokine axes govern whether infused cells reach the tumor — a major determinant of solid‑tumor efficacy.

## Implication for product design
Because killing is multi‑modal, two design philosophies coexist:
1. **Preserve and unleash native polyfunctionality** (expansion + agonist/bisphosphonate + checkpoint relief), and
2. **Add a defined redirection** (CAR/TCR/engager) *on top of* retained innate killing — the explicit selling point of CAR‑γδ over CAR‑αβ.
