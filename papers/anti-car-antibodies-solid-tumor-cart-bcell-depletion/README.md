# Anti-CAR antibodies in solid-tumour CAR-T, and rituximab / B-cell-depletion dosing

Literature collection for one question: **is there a rituximab dosing schedule, given around CAR-T therapy
for solid tumours, to avoid anti-CAR (anti-idiotype / anti-drug) antibodies?**

**Short answer: no such schedule has been *published*, but two active trials now specify one**, and their
results are not out yet (`notes/registry_and_unpublished_evidence.md`):

- **Stanford GD2-CAR T in H3K27M+ diffuse midline glioma, NCT04196413 Arm D** — rituximab **750 mg/m²/day IV
  on days −6 and −5 for the first round, then 750 mg/m² on day −5 for each subsequent round**, with
  Cy 500 / Flu 30 mg/m² on days −4 to −2 before each repeat ICV infusion. The rationale is now explicit:
  anti-CAR T-cell responses and human anti-CAR antibodies (HACAs) track with loss of CAR-T persistence and
  progression in this trial (medRxiv 2026, PMID 42465905), and Arm D is described as the
  "intensified lymphodepletion regimen designed to reduce or eliminate anti-CAR immune responses".
- **Penn CART-EGFR-IL13Rα2 in newly diagnosed GBM, NCT06973096 Cohort B** — rituximab **375 mg/m² × 1 day**
  with Flu 30 / Cy 300 mg/m² × 3 days before each q6-week repeat ICV cycle.

Evidence for benefit remains absent: the one in-vivo experiment that gave anti-CD20 before a CAR-T product
(7 mg/kg, 7 days pre-infusion, SIV-infected macaques) **did not prevent anti-CAR IgG** (PMID 36825014), and
the only in-human attempt at B-cell depletion alongside a solid-tumour CAR used a CD19 CAR rather than
rituximab and did not improve persistence (n = 3, PMID 32730744). Every rituximab schedule with an actual
outcome attached still comes from a *different* indication — enzyme replacement therapy, AAV gene therapy,
haemophilia inhibitors, autoimmunity — and is labelled indirect. See `REPORT.md`.

## Files

- `REPORT.md` — the synthesis: direct evidence table, dosing-schedule table with evidence class, timing/depth
  principles, CAR-T-specific hazards, alternatives, and an explicitly-labelled extrapolated schedule.
- `notes/administration_protocol.md` — how the drug is actually given: dose/timing of the two trial
  schedules, infusion rates and dilution, premedication (including whether to add a corticosteroid around
  CAR-T), infusion-reaction management, HBV/PJP/TLS/IgG screening and prophylaxis, late-onset neutropenia,
  CNS/ICV considerations, fasting vs sedation, and a per-round checklist. Every block labelled
  LABEL / REGISTRY / LIT / INFERENCE.
- `index.tsv` — 252 curated records (evidence categories `A`–`I`, plus 59 administration-level records in
  `J`–`N`, 4 trial-registry records and a funder presentation) with category, PMID/PMCID/DOI, local
  full-text path, and a per-paper note on why it is included.
- `notes/dosing_schedules_extracted.md` — dose, route, number of doses, and timing relative to antigen
  exposure, quoted from the primary sources.
- `notes/registry_and_unpublished_evidence.md` — ClinicalTrials.gov records, the anti-CAR-immunity preprint,
  and the CIRM board presentation: the two rituximab-containing solid-tumour CAR-T regimens, quoted verbatim,
  plus what is *not* there (no B7-H3 CAR-T trial at Penn; no B7-H3 trial anywhere uses rituximab).
- `notes/search_strategy.md` — queries, record counts, screening, and the inclusion/exclusion rules.
- `fulltext/` — 128 open-access full texts (JATS XML from Europe PMC/PMC, or publisher OA PDFs). Rows marked
  `not_open_access` are paywalled; abstract-level evidence only.

## Categories in `index.tsv`

| Category | Meaning |
|---|---|
| `A_anticar_evidence_solid` | Anti-CAR/anti-idiotype antibodies documented in solid-tumour (or non-B-cell-malignancy) engineered T cells, and the two B-cell-depletion attempts. **Primary evidence.** |
| `B_mechanism_assays_regulatory` | Mechanism, ADA assays, immunogenicity guidance. Haematology-derived papers here are marked MECHANISM ONLY. |
| `C_solid_redosing_trials` | Solid-tumour CAR-T trials that redose (IV, ICV, intrapleural, intraperitoneal, intra-arterial) — the setting where ADA matters. |
| `D_ritux_pharmacology_schedule` | What determines a rituximab schedule: dose–depletion–duration, tissue vs blood depletion, plasma-cell escape, resistance, safety cost. |
| `E_prophylaxis_gene_therapy` | Rituximab/anti-CD20 prophylaxis that *did* prevent anti-drug antibodies to a novel protein — AAV and gene therapy. Indirect. |
| `F_prophylaxis_ITI_regimens` | Immune tolerance induction regimens with hard schedules: Pompe/MPS ERT and haemophilia. Indirect but the best-specified. |
| `G_solid_tumour_HAMA_precedent` | Solid-tumour precedent for suppressing anti-murine-protein humoral responses (high-dose cyclophosphamide, cyclosporin A, deoxyspergualin). |
| `H_lymphodepletion_context` | Lymphodepletion and concomitant immunosuppression already used with CAR-T, and the cost of B-cell ablation. |
| `I_confusables_do_not_confuse` | **Not evidence.** Rituximab as a CD20/RQR8 CAR kill switch, rituximab as anti-tumour/target-sensitising therapy, dual CD19/CD20 targeting. |
| `J_admin_premedication_infusion_reactions` | Premedication trials and cohorts (H1 generation, H2, corticosteroid), rapid-infusion schedules, IRR recognition/grading/management, desensitisation, serum sickness. **Administration, not efficacy.** |
| `K_admin_screening_prophylaxis` | HBV screening and antiviral prophylaxis, PJP/herpes prophylaxis, hypogammaglobulinaemia and IgG replacement, late-onset neutropenia, PML, TLS, vaccination. |
| `L_admin_dose_route_pk` | Dose–exposure–duration, anti-rituximab antibodies and clearance, subcutaneous/biosimilar formulations, intra-CSF delivery routes and the CNS B-cell sanctuary. |
| `M_admin_cart_context` | The CAR-T side of the same round: lymphodepletion dosing, CRS/ICANS and TIAN grading and management, locoregional/ICV delivery. |
| `N_admin_fasting_procedure` | Preoperative/procedural fasting guidelines — cited only to separate anaesthesia fasting from the (non-existent) fasting requirement for the infusion itself. |

## Scope rules

Excluded from the evidence set (per the request not to be misled by B-cell cancers): CAR-T for lymphoma,
leukaemia, myeloma or other B-cell malignancies; rituximab as direct anti-tumour therapy; rituximab as a
CAR safety switch; autoimmune CD19 CAR-T. Where such a paper carries transferable mechanism (e.g. the first
human demonstration of anti-transgene rejection, or plasma-cell survival during B-cell aplasia) it is
retained with an explicit MECHANISM ONLY flag in its note.

The administration categories (`J`–`N`) are deliberately exempt from that rule: infusion rate,
premedication, HBV screening, IgG monitoring and fasting are properties of the **drug and the procedure**,
not of the indication, so the best evidence for them is lymphoma-, autoimmune- and anaesthesia-derived.
They say nothing about whether rituximab prevents anti-CAR antibodies.
