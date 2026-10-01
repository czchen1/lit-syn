# CAR-T + immune checkpoint inhibitors: what the clinical evidence shows

*Literature review. Scope: published patient data (prospective trials, retrospective
cohorts, case series) on CAR-T combined with or sequenced around checkpoint blockade,
in hematologic malignancies and solid tumors, plus CAR-T products engineered for
checkpoint resistance. Preclinical work appears only as rationale.*

**Headline.** Across every published setting, adding systemic PD-1/PD-L1 blockade to
CAR-T is **feasible and does not produce a distinctive new toxicity signature**, but
**no study has demonstrated an efficacy advantage over CAR-T alone in a controlled
comparison**. The two prospective trials with real statistical power to show
improvement (ZUMA-6, PORTIA) did not show one; the one trial that randomized *timing*
(JCAR014 + durvalumab) found pre-infusion blockade **worse**. The only datasets with a
visible benefit signal are retrospective PD-1 maintenance cohorts whose designs are
heavily biased toward responders. ICI *after* CAR-T failure is a low-yield salvage.

---

## 1. Why the combination was expected to work (rationale, not evidence)

Under high antigen load CAR-T cells upregulate PD-1; PD-L1 on tumor and myeloid cells
then suppresses CAR-T cytotoxicity and proliferation — shown directly in orthotopic
mesothelioma models, where PD-1 blockade or cell-intrinsic PD-1 disruption restored
CAR-T function (PMID 27454297). Unlike CAR-intrinsic fixes, systemic ICI can also
re-activate endogenous tumor-specific T cells (PMID 39617146). Antigen-driven CAR-T
activation/deletion is itself checkpoint-modulated (PMID 27019998). The clinical
hypothesis is therefore "ICI rescues CAR-T persistence/function"; the human data below
test it.

## 2. Hematologic malignancies: ICI as part of the CAR-T regimen

| Study | Design / n | Efficacy | Key safety | Benchmark read |
|---|---|---|---|---|
| **ZUMA-6** axi-cel + atezolizumab, r/r DLBCL (PMID 41231109) | phase 1/2, single-arm, n=34, 56.9-mo median follow-up | CR 54%; mPFS 9 mo; mOS 32.2 mo | grade ≥3 TEAE 88%; grade ≥3 CRS 9%; grade ≥3 neurologic 32%; 1 DLT (grade 4 cytopenias) | CR rate and PFS sit within the range of axi-cel monotherapy (ZUMA-1 CR ~58%); no signal of added efficacy |
| **PORTIA** tisagenlecleucel + pembrolizumab, r/r DLBCL (PMID 36044388) | phase 1b, 3 timing cohorts (pembrolizumab day +15 / +8 / −1), n=12 treated | feasible; "emerging efficacy" only in the day −1 cohort; too small for conclusions | no DLTs; CRS in most patients, one grade 3 CRS, one grade 2 ICANS | pembrolizumab did **not** augment CAR-T expansion; delayed peak expansion when given day −1 |
| **JCAR014 + durvalumab**, LBCL (PMID 37903325) | phase 1 with durvalumab started **before or after** infusion, n=29 infused (26 evaluable) | ORR 35%, CR 27% overall; pre-infusion cohort **inferior**; historical JCAR014-alone ORR 50%, CR 42% | no excess autoimmune or immune-effector toxicity; 2 DLTs (grade 4 CRS; prolonged grade 3 neurotoxicity) | strongest causal evidence in the field — and it is evidence of **harm from early blockade**, via soluble PD-L1 and slower CAR-T accumulation |
| CD19 CAR-T + nivolumab, r/r B-NHL (PMID 31482064) | single-center, n=11 | ORR 81.8%, CR 45.5%; mPFS 6 mo (median follow-up 6 mo) | CRS grade 1 25%, grade 2 50%; 1 neurotoxicity; no DLT | high ORR but tiny, uncontrolled, short follow-up; PFS unremarkable |
| Pembrolizumab "refueling" after CAR-T (PMID 28031179) | case report | re-expansion of CAR-T with response | — | mechanistic proof of concept that generated the whole clinical program |
| PD-1/CD28 switch-receptor CD19 CAR-T, PD-L1+ B-cell lymphoma (PMID 33028589) | small prospective series | responses reported in PD-L1-positive disease | low-grade CRS | receptor-level, not systemic ICI; see §7 |

**Reading.** The two industry trials designed to beat monotherapy did not; the Chinese
single-center series with eye-catching ORRs are n≈10 with months of follow-up. In
JCAR014, ongoing durvalumab *after* infusion was associated with CAR-T re-expansion
and some late responses — the most credible pro-combination observation, but
non-randomized and within a trial that overall underperformed its own historical
control.

### CD30 CAR-T + PD-1 blockade (Hodgkin / T-cell lymphoma)

CD30 CAR-T + camrelizumab (phase II, ChiCTR-2100046763; PMID 41795113): 18 enrolled,
12 infused, 11 evaluable — ORR 63.6%, CR 36.3%, median PFS 11.1 months. In the seven
classical Hodgkin lymphoma patients: ORR 100%, CR 57.1%, 2-year PFS 57.1%, 2-year OS
100%, including responses in five patients who had already failed PD-1 blockade.
Toxicity was low-grade CRS with grade 3–4 cytopenias. This is the most encouraging
prospective combination dataset, and the "failed prior PD-1" subgroup argues the
CAR-T component is doing real work — but n=7 in a disease where PD-1 blockade alone is
highly active, and 6/18 enrolled never got infused. A separate CD30 CAR-T + nivolumab
cohort (ACTION) is conference-abstract only and is not treated here as published
outcome data.

## 3. PD-1 blockade as post-CAR-T maintenance / consolidation

These are the only datasets showing survival separation, and all three are
retrospective with the same structural bias: **maintenance is offered to patients who
are alive, well, and responding** weeks after infusion.

- n=44, high-tumor-burden r/r DLBCL, PD-1 inhibitor + CAR-T then maintenance in
  responders vs CAR-T alone (PMID 35195933): ORR essentially unchanged (65.4% vs
  61.1%) but higher PFS/OS at 3 and 12 months; CRS/ICANS grades comparable.
- n=81 of 173 r/r B-NHL receiving PD-1 maintenance after CD19/22 CAR-T (PMID 38564164):
  ORR 82.9% vs 60% and 2-year PFS 59.8% vs 21.3% versus no maintenance, with longer
  CAR-T persistence but no difference in peak expansion. Notably, in the parallel
  CAR-T + ASCT trial maintenance added **nothing** (2-year PFS 74.9% vs 72.3%) — i.e.
  the apparent benefit disappears once the control arm does well.
- Propensity-matched 22 vs 22, r/r NHL, sintilimab consolidation (PMID 41204365):
  median PFS 42.9 vs 3.0 months (HR 0.32), OS not reached vs 21.5 months, largest
  effect in double-expressor/TP53-altered disease; CRS/ICANS comparable.

**Reading.** Effect sizes this large in n=22 matched cohorts (3.0-month control PFS)
indicate residual confounding and guarantee-time bias more than they indicate drug
effect. The consistent mechanistic correlate — longer CAR-T *persistence* without
higher peak expansion — is nonetheless the most reproducible biological finding in the
whole literature. This is the setting a randomized trial should test.

## 4. Checkpoint blockade as salvage after CAR-T failure

- Pembrolizumab after CD19 CAR-T failure/relapse, n=12 (PMID 34496014): ORR 25% (1 CR,
  2 PR), clinical benefit 33%; only grade ≥3 toxicity was neutropenia (25%). Responders
  showed increased CAR-T percentage/transgene and less exhaustion — a real
  pharmacodynamic effect in a few patients.
- 96 patients, 15 US centers, PD-1 blockade after CAR-T failure (PMID 37026796):
  ORR 19%, CR 10%, median DOR 221 days, **median PFS 54 days, median OS 159 days**,
  grade ≥3 AEs 19%; 83% died; only **5% had durable responses**. Better outcomes in
  primary mediastinal B-cell lymphoma and in late (>180-day) relapse.
- Context for expectations after CAR-T failure generally: PMID 36335261.

**Reading.** Unselected ICI salvage after CAR-T failure is largely ineffective. The
defensible indications are histology-driven (PMBCL, and by extension Hodgkin) or late
relapse, not "CAR-T failed, try PD-1."

## 5. Timing and prior ICI exposure

- Pre-infusion blockade can be harmful: in JCAR014 (PMID 37903325), durvalumab before
  infusion delayed and shortened CRS, slowed CAR-T accumulation, raised soluble PD-L1
  at the time of peak expansion, and produced inferior efficacy; soluble PD-L1
  suppressed CAR-T function dose-dependently in vitro. PORTIA's day −1 cohort likewise
  delayed peak expansion (though that cohort had the numerically best responses in
  n=4).
- Prior ICI does not preclude CAR-T benefit: real-world axi-cel in PMBCL, a
  heavily PD-1-pretreated population, had outcomes comparable to other LBCL
  (PMID 34474474); ICI-containing bridging/holding regimens before CAR-T are
  described without a distinct safety signal (PMIDs 41968224, 40963380).

**Reading.** The published data support **ICI after CAR-T engraftment**, not before.

## 6. Solid tumors

| Study | Design / n | Efficacy | Safety |
|---|---|---|---|
| Intrapleural mesothelin CAR-T → pembrolizumab, malignant pleural disease (PMID 34266984) | phase I, 27 infused, 18 received pembrolizumab | median OS 23.9 mo from CAR-T (1-yr OS 83%); SD ≥6 mo in 8; 2 complete metabolic responses | combination safe, no added toxicity attributed to it |
| EGFRvIII CAR-T + pembrolizumab, newly diagnosed GBM (PMID 38216766) | phase I, n=7 | **no efficacy**: mPFS 5.2 mo, mOS 11.8 mo, all progressed | no DLT; post-treatment tumors *more* exhausted/regulatory — PD-1 blockade did not prevent exhaustion. (Earlier UPenn experience included severe pembrolizumab-attributed immune hepatitis.) |
| Satri-cel (CLDN18.2) ± anti-PD-1, GI cancers (PMID 38830992) | phase I final, n=98 total; anti-PD-1 cohort n=15 | anti-PD-1 cohort ORR 26.7%, DCR 73.3%, no CR — not better than the n=61 monotherapy cohort (whole-trial ORR 38.8%, mPFS 4.4 mo, mOS 8.8 mo) | whole trial: no DLTs, no treatment-related deaths, no ICANS; CRS 96.9% all grade 1–2; gastric mucosal injury 8.2% |
| GD2-CAR3 ± Cy/Flu ± PD-1 inhibitor, neuroblastoma (PMID 28602436) | phase I, 3 cohorts, n=11 | modest responses at 6 weeks; **PD-1 inhibition did not further enhance expansion or persistence** (lymphodepletion did, up to 3 logs) | no DLTs |
| Mesothelin CAR-T with PD-1 + TCR disruption, MSLN+ solid tumors (PMID 34381179) | phase I | feasibility/safety | — |
| Anti-PD-1 nanobody-armored MSLN CAR-T (NAC-T), mesothelioma (PMID 41134065) | first-in-human, n=11 | ORR 63.6% (1 CR), DCR 100%, mPFS 5.0 mo, mOS 25.6 mo | no DLT |

**Reading.** Solid-tumor data are n≤20 phase I trials with safety primary endpoints.
Two patterns recur: (i) where benefit is claimed (mesothelioma), it is survival in a
single-arm cohort with regional delivery, not response rate, and cannot be attributed
to the ICI component; (ii) where the design allows an internal comparison (satri-cel
cohort 2 vs cohort 1; GD2-CAR cohort 3 vs 2), **adding PD-1 blockade did not help**.
GBM is an outright negative result with mechanistic evidence of why.

## 7. CAR-T with built-in checkpoint blockade (distinct from systemic ICI)

- **PD1-19bbz**, non-viral CRISPR knock-in of a CD19 CAR into the *PDCD1* locus
  (PMID 37251628): 21 infused r/r B-NHL, no DLTs, all patients responded with 18 CRs;
  CRS was low-grade in 14 and ICANS grade 1–2 in 4. The best efficacy/safety numbers
  in this entire review — but phase I, single-center, and the CAR construct, delivery
  and manufacturing all differ from approved products, so PD-1 disruption is not
  isolable as the cause.
- **CRISPR PD-1-edited (non-CAR) T cells**, refractory NSCLC (PMID 32341578): 12
  treated, all treatment-related AEs grade 1–2, off-target editing 0.05%, mPFS 7.7
  weeks, mOS 42.6 weeks — safe and feasible, minimal activity.
- PD-1/CD28 or PD-1/IL-15Rβ switch receptors and anti-PD-1/PD-L1-secreting CARs are
  mostly preclinical (indexed as `tier:preclinical`), with scattered small clinical
  series (PMIDs 33028589, 35261791, 41134065).

**Reading.** Cell-intrinsic checkpoint disruption looks at least as promising as
systemic ICI with less systemic autoimmune exposure, but every clinical dataset is
phase I and confounded by the rest of the product design.

## 8. Safety synthesis

- **CRS**: incidence and severity in combination cohorts are in the expected range for
  the CAR-T product used; grade ≥3 CRS was 9% in ZUMA-6, and CRS was all grade 1–2 in
  the satri-cel trial. ICI timing changes CRS *kinetics* (later onset, shorter
  duration with pre-infusion durvalumab) rather than its frequency.
- **ICANS/neurotoxicity**: driven by the CAR-T product, not the ICI — grade ≥3
  neurologic events were 32% in ZUMA-6 (axi-cel, consistent with axi-cel alone),
  single-digit grade 1–2 in the CD30 and PD1-19bbz studies, and absent in the
  satri-cel trial. One prolonged grade 3 neurotoxicity counted as a DLT in JCAR014.
- **Cytopenias** are the commonest grade ≥3 events (grade 4 neutropenia/thrombocytopenia
  as the ZUMA-6 DLT; grade 3–4 lymphopenia/neutropenia in CD30 cohorts; grade ≥3
  neutropenia in 25% of pembrolizumab-salvage patients).
- **irAEs**: individually serious but uncommon in published series — severe immune
  hepatitis attributed to pembrolizumab in the UPenn GBM program, severe cutaneous
  toxicity reported with ICI in the CAR-T setting (indexed case report). JCAR014
  explicitly found no increase in autoimmune or immune-effector toxicity.
- **No confirmed excess of HLH/MAS, fatal toxicity, or treatment-related death** has
  been attributed to the combination in published cohorts; infection data are
  inconsistently reported and cannot be summarized reliably.
- Caveats: sample sizes of 7–34 cannot exclude rare serious toxicity; follow-up in
  several series is <12 months; late-onset irAEs and autoimmunity are
  under-ascertained; and phase I populations are selected for fitness.

**Net safety conclusion:** the combination is tolerable and toxicities are the
expected ones from each agent. "Safe" here means "no new toxicity class and no
amplified CRS/ICANS", not "no serious toxicity".

## 9. Evidence quality

- **No randomized comparison of CAR-T + ICI vs CAR-T alone exists.** Every efficacy
  claim rests on single-arm trials, historical benchmarks, or retrospectively matched
  cohorts.
- Largest prospective dataset: n=34 (ZUMA-6). Most trials are n≤20; several key
  cohorts (CD30 + nivolumab, some solid-tumor combinations) remain conference
  abstracts.
- Products, ICI agents, doses, timing, lymphodepletion and tumor burden all vary
  between studies, so cross-study comparison is weak; tumor burden in particular
  differs systematically between combination cohorts and their historical controls.
- The maintenance literature is subject to selection and guarantee-time bias; the
  salvage literature is subject to referral bias; positive single-center series are
  subject to publication bias.
- Reported mechanistic endpoints are more consistent than clinical ones: ICI after
  infusion is repeatedly associated with CAR-T re-expansion, longer persistence and a
  less exhausted phenotype **in responders**, while peak expansion is unchanged or
  delayed.

## 10. Bottom line and what would change it

1. Combining CAR-T with PD-1/PD-L1 blockade is feasible and tolerable; it has **not**
   been shown to improve response rates over CAR-T alone in any adequately designed
   comparison, and pre-infusion blockade appears detrimental.
2. The strongest clinical signals, all requiring confirmation, are: PD-1 blockade as
   **post-infusion consolidation/maintenance** in high-risk B-NHL; **CD30 CAR-T +
   camrelizumab in Hodgkin lymphoma**, including after prior PD-1 failure; and
   **cell-intrinsic PD-1 disruption** (PD1-19bbz).
3. The clearest negatives are **ICI salvage after CAR-T failure** (≈5% durable
   responses) and **EGFRvIII CAR-T + pembrolizumab in GBM** (no efficacy, worse
   exhaustion).
4. What would change the picture: a randomized trial of post-infusion PD-1 blockade
   versus observation after CD19 CAR-T, with persistence and a landmark-from-response
   design to defuse guarantee-time bias; disease-restricted trials where PD-1 biology
   is dominant (cHL, PMBCL); and solid-tumor trials that test the ICI component
   internally rather than adding it to everything.

---
*Per-paper listings: `../REPORT.md`. `★` entries there are the papers this review is
built on. Quantitative claims above are taken from the publications' abstracts/results
as mirrored in `../fulltext/` or from the indexed records; where a study reported both
interim and final analyses, the final analysis is used.*
