# NK-cell engagers, CD16 biology and ADCC combinations

Engagers supply tumour specificity without gene transfer, which makes them the cheapest way to redirect an
otherwise unmodified (and therefore easily manufactured) NK product.

## BiKEs → TriKEs → multispecific NKCEs

- **BiKE (CD16 × CD33)** activated NK cells against primary MDS blasts and MDSC targets (Gleason 2014,
  PMID 24652987) — proof that crosslinking CD16 to a tumour antigen is sufficient for NK redirection.
- **TriKE** adds an IL-15 moiety to the same scaffold: the 161533 (CD16 × IL-15 × CD33) TriKE conferred
  specificity **plus** persistence, in vivo expansion and enhanced function (Vallera 2016, PMID 26847056).
  This is the key conceptual step — the engager also becomes the cytokine support.
- Target expansion: CD19-TriKE restores NK function in CLL (PMID 30890546), CLEC12A-TriKE targets AML blasts
  and leukaemic stem cells (PMID 33097838), and an IL-15-modified **NKp30 × HER2** TriKE avoids reliance on
  CD16 altogether (PMID 40694640).
- **Beyond CD16**: a trifunctional NKp46 × CD16a × CD123 NKCE controlled AML in vivo and overcame CD64-mediated
  resistance to anti-CD123 ADCC (Gauthier 2023, PMID 36635380). Engaging NKp46 sidesteps CD16 polymorphism and
  shedding.
- Construction methods are published as protocols (PMID 27177679), and reviews map the class (PMID 37638058).

## AFM13: the engager that carries a cell product

**AFM13** (CD30 × CD16A) is the clearest example of engager–product co-formulation:

- Pre-complexing AFM13 with cytokine-activated blood- or cord-blood-derived NK cells produced "CAR-like"
  responses against CD30+ malignancies without gene transfer (Kerbauy 2021, PMID 33986022).
- That combination reached the clinic: **cord-blood-derived, cytokine-preactivated, expanded NK cells
  pre-complexed with AFM13** in CD30+ lymphoma refractory to brentuximab vedotin *and* checkpoint inhibitors
  (phase 1, PMID 40186077) — one of the strongest recent efficacy signals for a non-CAR NK product.
- Manufacturing consequence: engager-loaded NK cells must survive cryopreservation *as a complex*, and this
  has been shown to be feasible with retained activity and specificity (PMID 35225870).

## CD16 (FcγRIIIa) is the limiting component of ADCC

- **Shedding.** Activation induces ADAM17-mediated CD16A cleavage as negative feedback. Blocking ADAM17
  enhances IL-15-mediated NK activation and proliferation (PMID 39053944), CD16A shedding limits
  engager-induced **serial killing** (PMID 41116262), and ADAM17 knockout is an established edit
  (PMID 31704085).
- **Non-cleavable, high-affinity CD16.** iPSC-NK cells expressing high-affinity non-cleavable CD16a (hnCD16)
  mediate improved ADCC (PMID 31856277) and this module is part of the clinically tested FT596 product
  (PMID 39798981). Alternatively, high-affinity CD16-158V can be knocked into the *CD38* locus while
  simultaneously deleting CD38 (PMID 35135865).
- **Polymorphism.** The FcγRIIIA L48-H/R polymorphism enhances ADCC by promoting serial killing
  (PMID 39666369) — relevant both to donor selection and to which CD16 variant an engineered product should
  carry.

## Antibody and drug combinations

- **Anti-CD38 (daratumumab) + expanded NK cells** in myeloma: effective ex vivo against patient cells
  (PMID 33457074), but daratumumab depletes CD38-high NK cells — hence CD38 knockout products
  (PMID 32603414, PMID 33375774). Epigenetic control of CD38/CD48 by KDM6A modulates the NK response
  (PMID 38355622), and the marrow NK profile predicts MRD negativity on daratumumab-based therapy
  (PMID 40019438).
- **Rituximab**: T-cell help in the TME enhances rituximab-mediated NK ADCC (PMID 38457360); the SUMOylation
  inhibitor subasumstat potentiates rituximab activity via IFN-I-dependent macrophage and NK stimulation
  (PMID 35226739).
- **Cetuximab**: CTLA-4+ Tregs expand in cetuximab-treated head-and-neck cancer and suppress NK cytotoxicity,
  correlating with poor prognosis (PMID 25832655) — a rationale for the CTLA-4 blockade arm in the CIML NK
  head-and-neck trial (PMID 39948608). Autologous NK cells (SNK01) plus chemotherapy and/or cetuximab were
  tested in NSCLC after TKI failure (PMID 38538093).
- **Radiotherapy** orchestrates NK-dependent responses through CXCL8 (PMID 35319989) and enhances NK
  cytotoxicity and tumour localisation, including a first-in-dog clinical trial (PMID 29254507).
- **Proteasome/epigenetic sensitisation of the target**: bortezomib suppresses HLA-E and upregulates DR5,
  sensitising myeloma to NK cells (PMID 30713790); BET inhibition activates NK cells via BRD4/SMAD3 in NSCLC
  (PMID 38519469); STING agonists enhance CAR-NK activity in pancreatic cancer (PMID 35371622).

## Practical implications

1. If the product is unmodified NK cells, an IL-15-containing TriKE gives specificity **and** persistence in
   one reagent — an attractive alternative to CAR engineering.
2. Protect CD16: ADAM17 blockade or knockout, or express hnCD16.
3. For antibody combinations, check whether the antibody target is also expressed on NK cells (CD38 is the
   cautionary example) and delete it if so.
4. Engager pre-complexing is compatible with cryopreserved, off-the-shelf logistics.
