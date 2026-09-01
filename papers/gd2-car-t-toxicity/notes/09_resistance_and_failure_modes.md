# 09 — Resistance mechanisms and failure modes

Toxicity is one axis of failure; this note collects the other one. Evidence labels as elsewhere
([GD2-clinical], [preclinical], [CART-general], [GD2-antibody]).

## 0. How well does it actually work?

- **Neuroblastoma, meta-analysis of 8 trials / 146 patients** (PMID 41530803) [GD2-clinical]:
  pooled CR **39.6%** (21.2–58.0), PR 15.8%, SD 30.8%, PD 20.9%. Authors' own verdict: efficacy
  "moderate"/limited.
- **GD2-CART01, final phase 1/2 + hospital-exemption cohort, 54 children** (PMID 40841488;
  interim PMID 37018492) [GD2-clinical]: ORR **66%**, CR 37–40% across timepoints, 5-year OS **42.7%**
  in the trial cohort; in the low-disease-burden target population ORR **77%**, 5-year OS 68%, EFS 53%.
  Persistence ≥12 months in **64%** (interim median persistence only 3 months, range 1–30).
- **CNS disease is worse than neuroblastoma**: DMG responses are transient tumour-volume reductions and
  neurological improvements, not remissions (PMIDs 35130560, 39537919, 38771986).
- **CAR-NKT** (PMID 37188782): ORR 25% (3/12).

## 1. Failure before the cells are ever infused (attrition)

Under-discussed but quantitatively the largest failure mode in DMG [GD2-clinical]:

- Stanford NCT04196413 (PMID 39537919): of the screened population, **36 patients progressed to
  ineligibility while on the waitlist or chose other options**; of 13 enrolled, **2 were removed before
  treatment** for rapid progression and performance-status decline. In the first report (PMID 35130560),
  a spinal DMG patient progressed *during manufacturing* and had to be treated on a compassionate eIND.
- Manufacturing itself is **not** the bottleneck: GD2-CART01 reported no manufacturing failures in 27
  patients, and Stanford manufactured successfully for all patients.
- **T-cell fitness at collection is**: GD2-CART01 outcomes were substantially better when apheresis was
  performed **at diagnosis** rather than late, and after **1–2 prior lines** versus ≥3 (PMID 40841488).
  Prior cytotoxic therapy is therefore a resistance mechanism acting on the drug product, not the tumour.

## 2. Loss of function: exhaustion and short functional persistence

- The GD2 CAR is a **structurally exhaustion-prone construct**: the 14g2a scFv drives ligand-independent
  tonic signalling and early exhaustion, mitigated by 4-1BB costimulation (Long 2015, cited in
  PMID 35130560) and reversible by **transient rest**, including dasatinib-induced rest with epigenetic
  remodelling (Weber 2021, same citation set) [preclinical]. This is the mechanistic reason GD2 CAR
  design keeps changing.
- In the Stanford product, CAR⁺ cells already expressed significantly more **PD-1** than CAR⁻ cells at
  release (CD39, LAG3, TIM3 not different) [GD2-clinical].
- **C7R trial** (PMID 38771986) is the cleanest in-human demonstration of persistence-limited failure:
  plain GD2.CART patients had neurologic improvement lasting **≤3 weeks**, progressed, and **none
  qualified for a second cycle**; adding a constitutively active IL-7 receptor gave longer PFS
  (P < .005), 7/8 eligible for repeat cycles, PR in 2/7 DMG — **but most still progressed eventually**.
- **CAR-NKT** (PMID 37188782): response tracked product composition (**CD62L⁺** frequency higher in
  responders), and peripheral CAR-NKTs upregulated **BTG1**, a driver of exhaustion-associated
  hyporesponsiveness; BTG1 knockdown restored control of metastatic disease in mice.
- Response correlates in DMG were weak and product-independent: no CD4:CD8 difference between the 8
  responders and 3 non-responders; responders had higher post-IV plasma **IL-2** (PMID 39537919).

## 3. Compartmental failure: the drug does not reach all the disease

The single most instructive case in the corpus (spinal DMG-1, PMID 35130560) [ICV-clinical]:

- After ICV dosing her **spinal cord tumour regressed** with motor/urinary improvement and resolution of
  neuropathic pain, while a **temporal lobe metastasis did not respond at all**;
- the resected non-responding lesion showed **high and uniform GD2 by flow cytometry**;
- both compartments progressed by day +75.

So failure there was **access/delivery**, not antigen. ICV distributes through CSF and reaches
CSF-adjacent and leptomeningeal disease better than bulky parenchymal disease remote from the
ventricles — which is also why route optimisation (IV priming then ICV, multi-route, intratumoural) is
the open question the trialists themselves name. Related, from the same corpus [CART-general]: poor
trafficking into solid tumours is one of the three canonical explanations for the liquid-versus-solid
efficacy gap (PMID 39537919 discussion).

## 4. Antigen-side resistance

- **No confirmed GD2-negative escape** has been documented in these GD2 CAR-T cohorts — unlike CD19,
  where antigen loss is the dominant relapse mechanism. The recurrent pattern is instead **antigen
  retained, response lost**. This is a weak negative: re-biopsy and autopsy antigen profiling was
  performed in only a handful of patients, so escape is unexcluded rather than excluded.
- **Antigen density thresholds** matter mechanistically: CAR efficacy is governed by target and receptor
  density (Walker 2017, cited in PMID 35130560), so partial GD2 downregulation below the activation
  threshold could produce escape without producing an antigen-negative tumour [preclinical].
- Density is also the axis being engineered *deliberately* — velcro-like density-dependent targeting of
  tumour-associated carbohydrate antigens (PMID 41005308) — which trades sensitivity for safety and
  therefore risks converting a safety margin into a resistance mechanism.
- [GD2-antibody] For dinutuximab, ~40% of patients fail or become resistant; tumour-derived **small
  extracellular vesicles** were shown to induce that resistance, reversible with the
  farnesyltransferase inhibitor **tipifarnib** (PMID 35483745). Whether sEVs blunt CAR-T as well as
  ADCC is untested.

## 5. Microenvironmental suppression

- **MDSC/G-CSF axis** (PMID 39695851) [preclinical, GD2-specific]: CAR.GD2 T cells cleared disseminated
  rhabdomyosarcoma and orthotopic osteosarcoma, but co-presence of MDSCs **abolished long-term control**;
  tumour-derived **G-CSF** was identified as a key driver of MDSC expansion — a directly druggable node.
- **Myeloid suppression in neuroblastoma** more broadly: M-MDSC and PMN-MDSC are expanded in murine and
  human disease (PMID 41972140); **IGF2BP1** maintains the immunologically cold, immunosuppressive TME
  and its knockdown converts tumours to immunogenic (PMID 41328513) [preclinical].
- **In-patient evidence of a suppressive myeloid state**: CSF single-cell RNA-seq after **IV** dosing and
  at late timepoints showed phagocytic/lipid-metabolic myeloid cells with **DAM- and MDSC-like
  immunosuppressive signatures**, whereas peak ICV timepoints were interferon-responsive
  (PMID 35130560) — i.e. the same myeloid axis implicated in TIAN (see `notes/08`) plausibly also
  terminates the response. Untested causally.
- Standard countermeasures under study in this space: TGF-β dominant-negative receptors and armoured
  CARs (PMID 34572932 review; TGF-β-insensitive armouring validated clinically for PSMA, PMID 35314843),
  cytokine armouring (C7R, IL-15), microenvironment-actuated CARs (PMID 39841845), oncolytic-virus
  priming for DMG (PMID 42100144).

## 6. Iatrogenic and design-imposed failure (toxicity management defeating efficacy)

This is where `notes/07` and this note collide:

- **Corticosteroids** given for TIAN/ICANS blunt CAR-T activity; **dasatinib** deliberately switches CAR
  signalling off; **rimiducid/iCasp9** ablates the product outright — it rapidly resolved grade 3 ICANS
  in four GD2-CART01 children (PMID 40841488), at the cost of the therapy.
- **Toxicity capped the delivered dose**: grade 4 CRS at IV DL2 made **DL1 the MTD**, so the IV arm
  cannot be dosed at the level tested for efficacy (PMID 39537919).
- **ICV without lymphodepletion** removes systemic toxicity but also removes the homeostatic-cytokine
  niche that supports expansion; the trialists explicitly list "the role of lymphodepleting chemotherapy"
  as unresolved.
- **TIAN limits re-dosing cadence** even when re-dosing is the strategy that works — although TIAN
  severity attenuated with successive ICV infusions.
- Repeated ICV delivery depends on **hardware** (reservoir/EVD), so device complications are a route to
  losing the therapy rather than merely an adverse event.

## 7. What would resolve the ambiguities

1. Paired pre/post antigen profiling (GD2 density by flow, not just IHC positivity) at progression — the
   only way to separate density-threshold escape from functional failure.
2. CSF CAR-T phenotyping at progression versus peak, to test whether local exhaustion or myeloid
   suppression dominates.
3. A trial arm testing **MDSC/G-CSF or CCL2 blockade** alongside GD2 CAR-T; the preclinical rationale
   (PMID 39695851) is unusually direct and untested in humans.
4. Route comparison in patients with both CSF-adjacent and parenchymal lesions — the spinal DMG-1
   pattern predicts a dissociation that is measurable.
5. Reporting apheresis timing and prior-line count as prespecified covariates; GD2-CART01 suggests they
   dominate outcome.
