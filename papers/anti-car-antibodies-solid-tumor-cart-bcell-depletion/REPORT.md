# Rituximab / B-cell-depletion dosing to avoid anti-CAR antibodies in solid-tumour CAR-T

Scope: humoral anti-CAR immunogenicity (anti-idiotype / anti-drug antibodies, ADA) in CAR-T therapy of
**solid tumours**. Lymphoma, leukaemia and myeloma CAR-T are used only where they supply mechanism or
assay methodology, and are explicitly flagged as such. Rituximab used as a CAR **kill switch** or as
anti-tumour/target-sensitising therapy is catalogued separately as a confusable, not as evidence.

---

## 1. Bottom line

1. **There is no published rituximab dosing schedule for solid-tumour CAR-T given to prevent anti-CAR
   antibodies.** Targeted PubMed searching (~3,100 records screened, `notes/search_strategy.md`) found no
   clinical trial, case report, or protocol in which rituximab was administered around a solid-tumour CAR-T
   product for ADA prophylaxis. Any schedule quoted as "the" schedule for this indication is extrapolation.
2. **The one in-vivo test of anti-CD20 before a CAR-T product failed to prevent anti-CAR antibodies.**
   Pampusch 2023 (PMID 36825014, non-human primate, SIV — not a tumour) gave **anti-CD20 7 mg/kg IV as a
   single dose 7 days before CAR-T infusion**. B cells were fully depleted in blood but only partially in
   lymph nodes, and **all three CAR-T-treated animals still had anti-CAR IgG at day 56**; the authors
   attribute the failure to incomplete depletion of lymphoid follicles. Pre-treatment was also associated
   with prolonged IL-6 elevation and *faster* CAR-T disappearance. This is the closest thing to direct
   evidence and it is negative for a single low pre-dose.
3. **The problem being solved is real and solid-tumour-specific.** Anti-idiotype/anti-CAR humoral responses
   have neutralised or curtailed solid-tumour CAR-T in: CAIX CAR-T in renal cell carcinoma (PMID 20889925,
   23423337), FRα CAR-T in ovarian cancer (17062687), TAG-72 CAR-T in colorectal cancer (28344808),
   mesothelin CAR-T where human anti-chimeric antibodies appeared in 8/14 patients (31420241), and most
   severely mRNA mesothelin CAR-T, where intermittent repeat dosing of a murine scFv produced **anaphylaxis
   and cardiac arrest** via IgE (24777247).
4. **The field's own B-cell-depletion attempt in a solid tumour used a CAR, not rituximab — and was
   negative**: in metastatic pancreatic cancer a CD19 CAR was co-infused with a mesothelin CAR to deplete
   B cells; B cells became undetectable by 7–10 days and stayed so for ≥28 days, but CART-Meso persistence
   did not improve at the dose tested (n = 3, PMID 32730744).
5. **If a rituximab-containing regimen is to be designed, the transferable schedules come from immune
   tolerance induction (ITI) in enzyme replacement therapy, AAV gene therapy and haemophilia** (§3), and
   from one solid-tumour precedent using cyclophosphamide rather than rituximab (§4). All are indirect.
6. **Design-side mitigation is better evidenced than immunosuppression**: humanised/fully human binders,
   linker choice, and ADA monitoring before redosing (§6).

---

## 2. Direct evidence table (solid tumour / CAR product)

| Setting | Product & dosing | ADA finding | B-cell-directed prophylaxis? | PMID |
|---|---|---|---|---|
| mRCC | CAIX CAR-T, repeated IV infusions ± IL-2 | anti-idiotype antibodies **neutralising CAR function** in most patients; also anti-vector immunity | none | 20889925, 23423337, 16648493 |
| Ovarian | FRα CAR-T, IV ± IL-2 | inhibitory serum factor in **3/6 patients tested**, blocking T-cell responses to FR+ tumour; no persistence | none | 17062687 |
| Colorectal | first-generation TAG-72 CAR-T (humanised CC49), IV or hepatic artery, up to 1e10 cells | induced **interfering antibody to the CC49 binding domain** (seen as an artefactual fall in serum TAG-72); persistence ≤14 weeks; authors recommend fully human constructs | none | 28344808 |
| Mesothelioma / pancreas / ovary | **mRNA** mesothelin CAR-T, intermittent repeat infusions | IgE anti-murine-scFv → **anaphylaxis, cardiac arrest on 3rd infusion** | none | 24777247, 24579088 |
| Mesothelioma / ovarian / pancreas | lentiviral SS1 (murine scFv) mesothelin CAR-T, single infusion ± Cy | **HACA in 8/14 patients**; fully human CAR taken forward | none | 31420241 |
| Pancreas (n = 3) | mesothelin CAR-T **co-infused with CD19 CAR-T** | B cells undetectable 7–10 d and ≥28 d, but **CART-Meso persistence not improved** | yes — CAR-mediated, not rituximab; **negative** | 32730744 |
| NHP, SIV (not tumour) | CD4-MBL-CAR/CXCR5 T cells | anti-CAR IgG in **all** animals, ADCC-competent | — | 36582226 |
| NHP, SIV (not tumour) | same CAR + **anti-CD20 7 mg/kg IV, day −7, single dose** | **anti-CAR IgG still developed in all animals**; partial LN depletion only | yes — **failed** | 36825014 |

Solid-tumour trials that depend on repeat dosing — and therefore carry the ADA risk this question is about —
are indexed under `C_solid_redosing_trials` (HER2 sarcoma up to 12 infusions, 25800760; repeated
intracerebroventricular GD2 / HER2 / B7-H3 dosing, 35130560, 39537919, 34253928, 39775044; repeated
intracavitary IL13Rα2, 28029927; hepatic-artery and intraperitoneal CEA CAR-T, 32843493, 31155611, 41760800).

---

## 3. Dosing schedules that do exist, and what they were given for

All extracted verbatim from the sources in `fulltext/` (see `notes/dosing_schedules_extracted.md`).
**Evidence class**: none of these were given to prevent anti-CAR antibodies.

| Regimen | Timing relative to antigen | Outcome | Setting (evidence class) | PMID |
|---|---|---|---|---|
| Rituximab **375 mg/m² IV weekly × 4** + methotrexate **0.4 mg/kg × 3 cycles** (with first 3 doses of antigen) + IVIG **500 mg/kg monthly** — "5-week short-course ITI" | started **at or before the first antigen exposure** | prevented/blunted anti-drug antibody; sustained tolerance | CRIM-negative infantile Pompe ERT (prophylactic ITI in humans) | 32849613, 22237443, 28814660, 23825616, 26167453 |
| Rituximab **375 mg/m² IV weekly × 3** + methylprednisolone 10 mg/kg, then **sirolimus daily**, **rituximab every 12 weeks**, IVIG monthly (IgG trough 700–1000 mg/dL) | rituximab started **~20 days before** first antigen exposure | **non-responsiveness to both capsid and transgene**, redosing possible | AAV1-GAA gene therapy, single human subject | 25541616 |
| Rituximab **20 mg/kg IV (≈375 mg/m²)** + cyclosporine A | after antibody had formed (rescue) | eradicated anti-FIX inhibitors in some animals | NHP AAV8-FIX | 22565846 |
| Anti-CD20 mAb **before vector**, ± rapamycin / anti-BAFF / anti-CD19+CD22 | **before** first exposure | prevented neutralising antibody, permitted re-administration | mouse/NHP AAV | 40057826, 38440160, 36994804, 32670285 |
| Anti-CD20 **+ rapamycin** (4 mg/kg 3×/week) with antigen | concurrent | tolerance where anti-CD20 alone was insufficient | haemophilia A inhibitors (human 2-patient + preclinical) | 31985872, 27683758, 32670285 |
| Rituximab 375 mg/m² weekly × 4 **+ bortezomib** 1.3 mg/m² days 1/4/8/11 ± MTX ± IVIG | after high titres established (rescue) | titres fell only when the **plasma-cell arm** was added | Pompe with entrenched ADA | 23060045, 27493997 |
| **Cyclophosphamide ≥ 4,000 mg/m²** | before, and murine protein started **< 90 days after** | HAMA-positivity reduced to 2/76 vs 17/27 if started > 120 days | **neuroblastoma (solid tumour), murine 3F8 antibody** | 16421906 |
| Cyclosporin A; deoxyspergualin | around repeated murine antibody dosing | suppressed HAMA, permitted repeat dosing | solid-tumour radioimmunotherapy (historical) | 3265333, 8306252, 7606728, 9815950 |
| Standard rituximab **375 mg/m² weekly × 4**; also 1 × 375 mg/m², 2 × 375 mg/m² d0/d7, 1000 mg d0/d14, 500 mg, 100 mg | — | dose determines **duration** of depletion (median B-cell return 2.5 vs 5.0 vs 6.6 months for 100 mg/m², 375 mg/m², 2 × 375 mg/m²) | pharmacology/autoimmunity | 9310469, 30109447, 24609057, 40374120, 38247568, 38595918 |

---

## 4. Timing and depth principles that any schedule must respect

- **Prophylaxis works, rescue mostly does not.** Anti-CD20 ablates a *de novo* antibody response but spares
  pre-established immunity (35015688); it blunts primary *and* secondary responses to a true neoantigen
  (bacteriophage φX174 in humans, 15636611; hapten in primates, 11161973). So rituximab must precede the
  **first** CAR-T infusion — HAMA-type primary responses appear ~2 weeks after exposure (1711007).
- **An established anti-CAR titre is made by CD20-negative long-lived plasma cells** and will not be
  reversed by rituximab: plasma cells and their antibody survive years of complete B-cell aplasia after
  CD19 CAR-T (27166358), and bortezomib only *delays* rather than eradicates inhibitor-producing cells
  (21251202). Rescue requires a plasma-cell agent (bortezomib), IgG cleavage (imlifidase, 32483358), or
  plasmapheresis (38327805, 40705999).
- **Blood depletion ≠ follicular depletion.** This is why the one CAR-T experiment failed (36825014):
  lymph-node and germinal-centre B cells persist after standard dosing (30649469, 14551029, 15838377,
  33384685, 42162633), and higher NHP doses (20–50 mg/kg, often ×3 weekly) are needed for nodal depletion.
  Type-2 anti-CD20 (obinutuzumab) depletes tissue compartments more deeply (31257724).
- **Inflammation confers resistance to anti-CD20-mediated depletion** (27265023) — directly relevant to a
  patient with bulky tumour, CRS, or IL-6 elevation.
- **Anti-CD20 alone leaves T-cell help intact**; the regimens that actually induced tolerance paired B-cell
  depletion with an mTOR inhibitor or methotrexate (32670285, 31985872, 33205401, 28562666).
- **IVIG timing matters**: IVIG given too close to rituximab can block B-cell depletion and abolish ITI
  efficacy (32681978).

---

## 5. CAR-T-specific hazards of adding rituximab

- **Do not give rituximab to a patient whose CAR-T product carries a CD20/RQR8 safety switch** — rituximab
  is the agent used to *delete* those cells (24970931, 19734426, 37086278, 33526841). This is the single most
  common source of confusion in this literature and is catalogued in `I_confusables_do_not_confuse`.
- Cy/Flu lymphodepletion already reduces B cells; regimen intensity varies (41183747), so the marginal
  benefit and the marginal toxicity of rituximab must be judged against that baseline.
- Rituximab plus corticosteroids around CAR-T is associated with **late cytopenias** (35842124).
- Prolonged B-cell depletion causes hypogammaglobulinaemia and impaired vaccine responses, requiring IgG
  monitoring/replacement (36372267, 41942445, 36906276, 34702753).
- B-cell depletion can impair vaccine-induced **CD8 T-cell** responses in a type-I-interferon-dependent
  manner (34226189) — a theoretical risk of blunting the CAR-T response itself.

---

## 6. Better-evidenced alternatives to immunosuppression

1. **Remove the immunogen**: humanised or fully human binders eliminated the ADA barrier to retreatment in
   the settings where it was formally studied (33512480, 26101914, 22127019, 41881100); framework
   engineering did the same for murine antibodies (14522015). The scFv **linker** itself is a dominant
   epitope (41253492) — a cheap design fix.
2. **Monitor before redosing.** Validated flow-cytometric and cell-based anti-CAR ADA assays exist
   (42033387, 31678267, 37983584, 41518483); the OKT3-era paradigm of screening before re-exposure
   prevented anaphylaxis (8497882, 8090628).
3. **Regional/locoregional repeat dosing** (intracerebroventricular, intrapleural, intraperitoneal,
   intra-arterial) is the delivery strategy actually being used to redose solid-tumour CAR-T
   (35130560, 39537919, 34253928, 39775044, 34266984, 32843493) — how much systemic humoral immunity
   constrains it is, to our reading, not yet reported.
4. **Cyclophosphamide** is the only agent with solid-tumour human data for suppressing an anti-murine-protein
   humoral response (16421906), and it is already part of standard lymphodepletion.

---

## 7. If a schedule must be proposed (extrapolation, not evidence)

Flagged clearly as **hypothesis-generating**; it has never been tested with a CAR-T product, and the only
in-vivo attempt with a single low pre-dose failed (36825014). A defensible starting design, assembled from
§3–§4 and requiring formal protocol review:

- **Precondition, do not react**: rituximab **375 mg/m² IV weekly, starting ≥ 2–4 weeks before the first CAR-T
  infusion**, for ≥ 2–4 doses (the ITI/AAV templates: 32849613, 25541616) — with the explicit caveat that
  standard dosing did not clear nodal/follicular B cells in the CAR-T primate experiment.
- **Verify depth, not just blood counts**: high-sensitivity flow for residual B cells (33384685); consider
  type-2 anti-CD20 for deeper tissue depletion (31257724).
- **Add a T-help arm** (sirolimus or low-dose methotrexate) rather than relying on B-cell depletion alone
  (32670285, 31985872, 32849613).
- **Do not expect rescue**: once anti-CAR titres exist, add a plasma-cell-directed or IgG-cleaving strategy
  (23060045, 32483358) rather than more rituximab.
- **Support IgG** with monthly IVIG, timed away from rituximab dosing (32681978, 36372267).
- **Absolute contraindication**: any CD20-based safety/selection switch in the CAR construct (24970931).
- **Monitor** ADA and CAR-T persistence with a validated assay at each redose (42033387, 31678267).

---

## 8. What is not known

- No solid-tumour CAR-T trial has reported an ADA-prophylaxis intervention arm; there is no dose-response,
  no timing comparison, and no persistence or efficacy endpoint for rituximab in this setting.
- Whether locoregional redosing (ICV, intrapleural) is materially affected by systemic anti-CAR antibodies.
- Whether B-cell depletion impairs CAR-T expansion or antitumour function in humans.
- Whether anti-CAR ADA in solid tumours is predominantly IgG (neutralising/ADCC) or IgE (anaphylaxis), which
  determines whether prophylaxis is a persistence question or a safety question (24777247 vs 20889925).
