# 00 — Overview: what "GD2 CAR-T toxicity" means, and why the route is the question

## The three toxicity engines

GD2 CAR-T toxicity is not one thing. Three mechanisms produce overlapping syndromes and are treated
differently:

1. **Systemic cytokine release** — CAR T cells activate, myeloid cells amplify (IL-1, IL-6, MCP-1),
   and the patient develops fever, hypotension, hypoxia, endothelial activation, transient organ
   dysfunction. Downstream of this sit CRS, IEC-HS/HLH, coagulopathy, hepatic and renal changes, and
   most of the drug-interaction risk. Dose- and route-dependent.
2. **Inflammation at the tumour site** — in CNS tumours the antitumour response happens inside a
   closed box. Oedema, mass effect, CSF-outflow obstruction and local electrophysiologic dysfunction
   produce **TIAN** (tumour inflammation-associated neurotoxicity), which is distinct from ICANS:
   symptoms map to tumour neuroanatomy, and the treatment is CSF drainage / hypertonic saline /
   anti-cytokine therapy rather than steroids alone (Majzner 2022, PMID 35130560).
3. **On-target / off-tumour engagement of normal GD2** — GD2 is expressed on peripheral nerve, some
   CNS neurons and melanocytes. With antibodies this reliably produces neuropathic pain; with CAR T
   cells it has been essentially absent clinically at standard affinity, but is fatal in preclinical
   models when scFv affinity is raised (Richman 2018, PMID 29180536).

A fourth, mostly non-CAR effect matters practically: **lymphodepletion**. Cyclophosphamide/fludarabine
causes the grade 3–4 cytopenias reported in most GD2 CAR-T trials, and ICV re-dosing is typically
given *without* lymphodepletion — which is a large part of why ICV looks safer.

## Why the route dominates the answer

For H3K27M+ DMG the same product has now been given both ways in the same trial
(NCT04196413, arm A), so the comparison is internal rather than cross-trial
(Monje 2025, PMID 39537919; 11 patients, 11 IV and 62 ICV infusions):

| Toxicity | IV (DL1 1×10⁶/kg, DL2 3×10⁶/kg) | ICV (10–30×10⁶ flat, no lymphodepletion) |
|---|---|---|
| CRS | 100% of infusions; grade 4 in 3/8 at DL2 (dose-limiting) | 33.9% of infusions; 16/21 grade 1, one grade 3 (in urosepsis) |
| ICANS | 5/11 patients (1 grade 3) | 0 of 62 infusions |
| TIAN | 100% DL1, 87.5% DL2; grade 3–4 in 5/11 | 71% of infusions; grade 3–4 in 8/62 |
| Dose-limiting toxicity | Yes — CRS defined DL1 as MTD | None across 62 infusions |

The route changes *which* compartment inflames. CSF cytokines are **higher** after ICV; blood
cytokines and CRS are higher after IV. Systemic organ-function toxicity and ICANS track the blood
compartment; TIAN and intracranial pressure track the CSF/tumour compartment.

## Evidence taxonomy used in these notes

Claims are labelled by source strength, because the temptation in this field is to import
CD19-lymphoma numbers into a 30-patient pediatric CNS experience:

- **[GD2-clinical]** — from a GD2 CAR-T/CAR-NKT trial. Small n, phase 1, mostly pediatric.
- **[ICV-clinical]** — from an ICV/locoregional CAR-T trial of any target (GD2, B7-H3, IL13Rα2,
  EGFR806, bivalent EGFR/IL13Rα2). Route-specific but often not GD2-specific.
- **[CART-general]** — from CD19/BCMA/CD22 experience. Large n, adult-dominant, systemic route;
  transfers for mechanism and for lymphodepletion-related toxicity, over-predicts for ICV.
- **[GD2-antibody]** — dinutuximab/naxitamab/hu14.18/3F8. Defines the on-target-off-tumour ceiling
  for the antigen but not for the modality.
- **[preclinical]** — mouse/xenograft. Predicted the brainstem-oedema/hydrocephalus problem and the
  affinity/CNS-toxicity relationship, so it is not decorative here.
- **[mechanistic-PK]** — inflammation/cytokine effects on drug-metabolising enzymes, mostly from
  rheumatoid arthritis, surgery, sepsis, COVID-19 and PBPK modelling. **No GD2 CAR-T study has
  measured a drug–drug interaction**; this literature supports plausibility and monitoring, not a
  quantified GD2-specific interaction.

## What the collection says in one paragraph

At standard affinity and clinically used doses, GD2 CAR T cells have not produced the on-target
off-tumour neurotoxicity that preclinical high-affinity constructs predicted; the dominant clinical
toxicities are CRS (IV, dose-limiting), TIAN (both routes, near-universal in DIPG but reversible with
a defined algorithm), lymphodepletion-driven cytopenias, and — in neuroblastoma — grade 3 ICANS in a
minority, aborted by iCasp9 activation. ICV administration without lymphodepletion largely removes
systemic CRS, ICANS and measurable hepatic/renal/haematologic derangement, and concentrates risk into
intracranial pressure, hydrocephalus, device-related events and intratumoural haemorrhage. Transient
organ-function change — and therefore concomitant-drug risk — is essentially a function of *systemic*
inflammation: it is real after IV infusion (hepatic dysfunction in up to 64% of grade 3–4 CRS,
AKI ~18% pooled after systemic CAR-T, resolving in ~79% within a month) and near-absent after ICV
dosing.
