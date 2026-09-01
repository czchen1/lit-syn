# 10 — ICV dosing without lymphodepletion

Locoregional CNS CAR-T is given **without conditioning chemotherapy**. That single design choice
explains most of the toxicity difference documented in `notes/03` and `notes/05`, and imposes its own
constraints. This note separates what is protocol fact, what is measured, and what is inference.

## 1. What the protocols actually specify [GD2-clinical / ICV-clinical]

**Stanford NCT04196413** (PMIDs 35130560, 39537919): one **IV** dose *after* Cy/Flu, then repeated
**ICV** infusions of 10–30 × 10⁶ cells **with no lymphodepletion before any ICV dose**. Re-dosing was
gated on: evidence of clinical or radiographic benefit, ≥28 days from the first infusion or ≥21 days
from subsequent ones, **circulating CAR T cells <5%**, and toxicity resolved to <grade 2. Sixty-two ICV
infusions were delivered in nine patients. No non-protocol chemotherapy, targeted therapy or
immunotherapy was permitted while on study.

**BrainChild-03 Arm C** (PMID 39775044) is the clean test of never-lymphodepleted dosing: **exclusively
ICV from inception**, q14 days across the 8-week DLT window with intra-patient dose escalation to
10 × 10⁷ cells per dose, continuing beyond; **253 doses in 21 patients**, some for multiple years. It
also **allowed enrolment on dexamethasone ≤2.5 mg m⁻² d⁻¹** and required only ALC ≥100 µl⁻¹ — i.e. it
did not merely omit conditioning, it tolerated ongoing immunosuppression.

## 2. Why omitting conditioning is coherent here

Lymphodepletion exists to make a systemically infused product expand: it opens niche space, raises
homeostatic **IL-7/IL-15**, and removes Tregs and suppressive myeloid cells. ICV substitutes
**placement for amplification** — the cells are delivered directly into a low-cellularity compartment at
the disease site, so the required local effector:target ratio is achieved by the dose itself rather than
by in-vivo expansion. Functionally this is closer to intrathecal drug dosing than to the single-infusion
"living drug" paradigm. [inference, consistent with the data below]

## 3. What is actually measured after ICV without conditioning

- **Compartment enrichment**: flow cytometry showed a significantly higher proportion of GD2-CAR T cells
  in **CSF** after ICV than after IV, and CSF cytokines/chemokines were higher after ICV while plasma
  cytokines were higher after IV (PMIDs 35130560, 39537919).
- **Local expansion does occur** but is modest: GD2-CART expansion was "evident in CSF following multiple
  repeated infusions"; in BrainChild-03, CAR T cells were detectable by EGFRt in **40/105 (38.1%) CSF
  specimens**, with **13/18 (72%) evaluable patients** positive at ≥1 timepoint — intermittent detection,
  not sustained engraftment.
- **Confounder in the GD2 trial**: Stanford's ICV doses were given on top of a lymphodepleted IV prime,
  and blood CAR levels (which expanded to magnitudes comparable to active haematological CAR-T trials)
  **persisted through the ICV period before declining**. So GD2 ICV re-dosing is not a pure
  no-conditioning experiment; BrainChild-03 is.
- **Loss of detection tracks progression**: two Stanford patients lost detectable blood CAR by PCR
  temporally correlated with clinical/imaging progression (PMID 39537919) — association, mechanism
  unknown.

## 4. What omitting conditioning buys

Every systemic toxicity attributed to Cy/Flu in `notes/05` disappears with it:

- no conditioning-driven grade 3–4 cytopenias, no prolonged ICAHT, no attendant transfusion and G-CSF
  burden, less infection risk stacking;
- CRS is largely eliminated (41/62 ICV infusions with **no** CRS; the rest mostly grade 1) and **ICANS
  did not occur after any ICV infusion**;
- no fludarabine (renally cleared, eGFR-dependent dosing) and no cyclophosphamide (CYP2B6/3A4
  bioactivation, haemorrhagic cystitis, marrow suppression) — which removes the largest concrete
  drug-interaction and organ-function exposures in `notes/06`. What remains as perturbers of concomitant
  therapy are hypertonic saline, corticosteroids and anakinra given for TIAN;
- it makes **multiyear repeat dosing** feasible; BrainChild-03 had patients alive at 44, 45 and 52 months
  from diagnosis, with median OS 19.8 months from diagnosis and 10.7 months from first infusion.

## 5. What it costs

- **Dose density replaces persistence.** 62 and 253 infusions respectively — the therapy becomes a
  chronic procedure programme, not an event.
- **Hardware dependence**: Ommaya/reservoir or catheter is mandatory, so device infection, malfunction,
  haemorrhage and shunt issues become the route by which patients lose access to therapy (BrainChild-03's
  DLT was a grade 4 intratumoural haemorrhage; one grade 3 hydrocephalus).
- **TIAN recurs with each infusion** (44/62 infusions), gating the interval, although grade attenuated
  over successive doses.
- **Re-dosing gates are restrictive**: requiring circulating CAR <5% and toxicity <grade 2 deliberately
  prevents stacking, at the price of delaying re-exposure.
- **Depth of response may be capped**: no conditioning means no removal of Tregs/MDSC and no homeostatic
  cytokine surge, in a tumour type where MDSC-driven suppression demonstrably abolishes long-term CAR.GD2
  control preclinically (PMID 39695851, `notes/09`). The Stanford authors explicitly list **"the role of
  lymphodepleting chemotherapy"** as an unresolved question for future arms.
- **Intact host immunity is retained**, which is the classic setting for **anti-transgene immune
  rejection** on repeat dosing — the constructs carry murine 14g2a scFv, iCasp9 and (in BrainChild)
  EGFRt. No anti-CAR antibody or T-cell response was reported in either trial: **unmeasured, not
  excluded**. Declining CAR detection over time is compatible with rejection but equally with exhaustion,
  antigen clearance or sampling.

## 6. Practical reading

The trade is: **systemic safety and repeatability in exchange for persistence, and procedural risk in
exchange for chemotherapy risk.** For a compartmentalised, CSF-accessible tumour that requires
re-treatment anyway, that trade is currently favourable, and it is why ICV toxicity is dominated by TIAN
and hardware rather than by cytopenias, hepatic/renal change and drug interactions.

Unresolved, in order of tractability:

1. Does light or CNS-directed conditioning before ICV deepen or lengthen response, or merely reimport
   systemic toxicity?
2. Can **local cytokine support** (C7R, IL-15 armouring) substitute for the homeostatic niche that
   conditioning provides, without reproducing TIAN severity?
3. Are anti-CAR humoral/cellular responses developing across dozens of ICV exposures? This is measurable
   today and is not being reported.
4. Optimal dose density: fixed q14-day dosing (BrainChild) versus benefit- and CAR-level-gated dosing
   (Stanford) has never been compared.
