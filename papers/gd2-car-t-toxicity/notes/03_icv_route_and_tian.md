# 03 — The ICV route: what it removes, what it adds, and TIAN

## What ICV administration removes

From the internal IV-vs-ICV comparison in NCT04196413 arm A (Monje 2025, PMID 39537919)
[GD2-clinical, ICV-clinical]:

- **Dose-limiting CRS**: grade 4 CRS was the IV DLT at 3×10⁶/kg; across 62 ICV infusions there was no
  DLT and CRS was absent in 41/62 infusions, grade 1 in 16.
- **ICANS entirely**: 0/62 ICV infusions, versus 5/11 patients after IV. This was explicitly
  unexpected because CSF cytokines are *higher* after ICV — consistent with ICANS being driven by
  systemic inflammation and endothelial/BBB injury from the blood side rather than by CSF cytokine
  concentration per se.
- **Lymphodepletion**, and with it the grade 3–4 cytopenias, febrile neutropenia and infection risk
  that dominate the AE tables of IV GD2 CAR-T trials. ICV re-dosing in arm A used no lymphodepletion.
- **Measurable systemic organ derangement**: no attributed hepatic, renal or electrolyte toxicity in
  the ICV experience; in the ICV-only B7-H3 trial the sole haematologic AE recorded during the DLT
  window was one grade 1 lymphocytopenia (Vitanza 2025, PMID 39775044).

## What ICV administration adds or keeps

1. **TIAN** — near-universal on first ICV exposure in DIPG, then attenuating.
2. **Intracranial pressure and CSF-outflow risk** — the dangerous, minutes-to-hours toxicity.
3. **Hardware** — Ommaya/Rickham reservoir or CNS catheter as an eligibility requirement, with its own
   infection, malposition and revision burden; ICV trials require a catheter before enrolment
   (Vitanza 2025).
4. **Intratumoural haemorrhage** — the single DLT in ICV B7-H3 (grade 4, PMID 39775044) and the one
   grade 5 event in GD2 arm A (PMID 39537919). Both cohorts argue background DIPG haemorrhage rates
   (~20% by 12 months) make attribution ambiguous; neither can exclude a contribution.
5. **Repeat-dosing exposure** — ICV programmes give many infusions (arm A median 4, range 1–17;
   BrainChild-03 median 9, range 1–81 over up to 37.5 months), so cumulative and late toxicity, and
   anti-CAR immunity, become the relevant questions rather than single-infusion peak toxicity.

## TIAN: definition, incidence, management

TIAN is **not** ICANS. It is neurotoxicity attributable to inflammation at the tumour site, graded by
CTCAE, and split into two types (Majzner 2022, PMID 35130560; retrospective application in
BrainChild-03, Ronsley 2026, PMID 41798119):

- **Type 1 — mechanical**: oedema, mass effect, obstruction of CSF flow → raised ICP, obstructive or
  communicating hydrocephalus, herniation risk. Treatment is **CSF removal via reservoir/EVD,
  hypertonic saline**, then anti-cytokine agents and corticosteroids.
- **Type 2 — electrophysiologic**: transient worsening of existing focal deficits without a mechanical
  cause (cranial-nerve dysfunction, trismus, hearing loss, ataxia, weakness), mapping to tumour
  neuroanatomy and often with corresponding T2/FLAIR change.

Incidence:

| Cohort | Route | TIAN |
|---|---|---|
| GD2-CAR DMG arm A (n=11) | IV then ICV | 91% of patients after IV; 100% after first ICV; 44/62 (71%) of ICV infusions; grade 3–4 in 8/62 ICV, 5/11 after IV; all reversible, no DLT |
| C7R-GD2.CART CNS tumours (n=8 C7R) | IV | grade 1 in 7/8 (88%), anakinra-controlled |
| B7-H3 CAR-T DIPG, BrainChild-03 (n=21) | ICV | 16/21 (76%) met TIAN criteria; 49/152 infusions (32%); 34 grade 1, 14 grade 2, 1 grade 3; 1 needed CSF diversion; 13 had worsening pre-existing deficits |

Practical points that recur across these cohorts:

- Symptoms are **predictable from tumour location** — pontine tumours give cranial-nerve and bulbar
  dysfunction; thalamic/cerebellar bulk was an *exclusion criterion* on the GD2 trial precisely
  because the preclinical models showed lethal hydrocephalus there.
- The therapeutic window is **short**: ICP 22 and 34 mmHg episodes in Majzner 2022 resolved "within
  minutes" of CSF drainage. This is why reservoir access, not pharmacology, is the primary
  intervention, and why ICP monitoring capability is an eligibility requirement rather than a nicety.
- **Fever after an ICV infusion is expected** and is not by itself CRS: BrainChild-03 explicitly
  interpreted fever as evidence of local immune activation (PMID 39775044).
- TIAN grade **falls with successive infusions** in both GD2 and B7-H3 cohorts — the first exposure is
  the risky one.
- Corticosteroids are used, but the algorithms put CSF diversion and IL-1/IL-6 blockade first, partly
  to protect CAR T-cell activity. Anakinra crosses into CSF after IV dosing (measurable CSF IL-1RA,
  PMID 35130560); ICV dexamethasone has been used in a refractory case (PMID 41479887 documents early
  intrathecal dexamethasone/methotrexate for ICANS), and Majzner 2022 used ICV steroids plus dasatinib
  as an off-label CAR "off-switch".

## Comparator locoregional CAR-T trials (route-specific safety)

- **ICV B7-H3, DIPG, BrainChild-03 arm C** (PMID 39775044): 21 patients, **253 ICV doses**, up to
  10×10⁷ cells/dose declared the maximally tolerated dose regimen; commonest AEs headache 81%,
  nausea/vomiting 81%, fatigue 62%, fever 57%, hiccups 29%; mostly grade 1–2; **hydrocephalus in 1
  (grade 3)**; no ICANS; single DLT = grade 4 intratumoural haemorrhage. Multiyear repeat dosing was
  tolerable.
- **ICV B7-H3 for non-pontine DMG / other pediatric CNS tumours** (PMID 42503899) and **intracranial
  B7-H3 for recurrent GBM** (PMID 42562965) extend the same safety pattern.
- **Intraventricular/intrathecal bivalent EGFR + IL13Rα2 CAR-T in recurrent GBM**
  (PMID 38480922, PMID 40451950) and **CARv3-TEAM-E** — locoregional CNS CAR-T with early
  inflammatory neurotoxicity managed without dose-limiting systemic toxicity.
- **EGFR806-CAR locoregional in pediatric CNS tumours** (PMID 40070357) and **IL13Rα2 intraventricular**
  (BrainChild-01) complete the picture: across targets, the locoregional route consistently converts
  the toxicity problem from systemic-inflammatory to intracranial-mechanical.
- **Lymphodepletion in solid/brain-tumour CAR-T** (PMID 39542517) reviews whether the systemic
  conditioning that drives most measurable organ toxicity is even needed for locoregional delivery —
  the question arms B/C of NCT04196413 are now testing prospectively.

## Route-specific unknowns

- Whether repeated ICV dosing causes cumulative ependymal/leptomeningeal injury, or CSF-flow
  impairment, is unmeasured; nobody reports longitudinal CSF dynamics.
- Device-related infection rates specific to CAR-T ICV programmes are not reported separately from
  general reservoir experience; the collection does contain post-CAR-T CNS infection reports
  (e.g. carbapenem-resistant *Klebsiella* CNS infection, PMID 41511674).
- Whether ICV dosing can *cause* CRS at higher cell doses than tested (>10×10⁷ per dose) is unknown —
  the grade 3 CRS in arm A ICV occurred with concurrent urosepsis, and CSF-to-blood cell egress is
  documented.
