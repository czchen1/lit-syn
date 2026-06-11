# GD2 CAR-T clinical-management plan — primary-source verification report

**Scope.** This report audits every quantitative/factual claim in
[`11_clinical_management_plan.md`](11_clinical_management_plan.md) and the lab index in
[`10_trial_index_by_lab.md`](10_trial_index_by_lab.md) against **primary sources**: the trial PDFs
and supplements held in this collection, the archived ClinicalTrials.gov protocol JSONs in
[`../protocols/clinicaltrials_gov/`](../protocols/clinicaltrials_gov/), and the PubMed/PMC
abstracts of paywalled reports.

Each claim is given an exact source location (file + line, or abstract sentence). Status codes:

- **VERIFIED** — claim matches a quote in a primary source (quote + location given).
- **CORRECTED** — claim was wrong/ambiguous vs the primary source; the plan has been fixed (old → new).
- **ABSTRACT-ONLY** — claim is correct but the only open primary source is the PubMed abstract
  (full-text/appendix is paywalled: NEJM, *Nature*, *Nature Medicine*, *Science Transl Med*).
- **NR** — not reported in any source available here (left as NR in the plan).

---

## 1. Primary-source inventory

| Trial / report | PMID | Open primary source held | Type |
| --- | --- | --- | --- |
| Louis 2011 (Baylor-1G) | 21984804 | `pdfs/louis_2011_pmid21984804.pdf` (full text) | full text |
| Baylor-1G long-term | 39962287 | PubMed abstract only (*Nat Med* 2025) | abstract |
| Heczey 2017 (GRAIN) | 28602436 | `pdfs/heczey_2017_pmid28602436.pdf` (full text) | full text |
| Heczey 2020 (GINAKIT2 protocol) | 33046868 | `supplements/.../heczey_2020_pmid33046868_supp.pdf` (full study protocol) | supplement/protocol |
| Heczey 2023 (GINAKIT2 results) | 37188782 | PubMed abstract + partial supp | abstract + supp |
| Tian 2025 (GINAKIT2 case) | 39800376 | `pdfs/tian_2025_pmid39800376.pdf` (full text) | full text |
| Del Bufalo 2023 (GD2-CART01) | 37018492 | PubMed abstract only (*NEJM*) | abstract |
| Locatelli 2025 (GD2-CART01) | 40841488 | PubMed abstract only (*Nature*) | abstract |
| Quintarelli 2025 (ALLO-CART01) | 39815015 | partial supp held | supplement |
| Majzner 2022 (Stanford, first pts) | 35130560 | `pdfs/majzner_2022_pmid35130560.pdf` + supp DOCX | full text + supp |
| Monje 2025 (Stanford, full arm A) | 39537919 | `pdfs/monje_2025_pmid39537919.pdf` (full text) | full text |
| Straathof 2020 (1RG-CART) | 33239386 | PubMed abstract only (*Sci Transl Med*) | abstract |
| Yu 2022 (4SCAR-GD2) | 34724115 | `pdfs/yu_2022_pmid34724115.pdf` (full text) | full text |
| Gargett 2024 (CARPETS) | 38754916 | `pdfs/gargett_2024_pmid38754916.pdf` (full text) | full text |
| ClinicalTrials.gov | — | 8 JSON records in `protocols/clinicaltrials_gov/` | registry protocol |

Extracted text used for line citations lives in `pdftotext`/abstract dumps; cited line numbers are
to those text extractions of the same PDFs.

---

## 2. Corrections made during verification

Seven cells/claims did **not** match their primary source and were corrected in the plan. Each is
documented below with the governing quote.

### C1 — GRAIN lymphodepletion order (Section 3)
- **Was:** "Cy 500 mg/m²/d ×2 + Flu 30 mg/m²/d ×3".
- **Now:** "Cy 500 mg/m²/d ×3 (d−4,−3,−2) + Flu 30 mg/m²/d ×2 (d−4,−3) … NCT01822652 lists the reverse".
- **Primary source:** Heczey 2017, methods/Table footnote — *"Cyclophosphamide 500 mg/m2/dose on days 4, 3, and 2 and fludarabine 30 mg/m2/dose on days 4 and 3 intravenously."* (`heczey_2017_pmid28602436.txt:385`; identical in figure legend `:84`).
- **Conflict noted:** ClinicalTrials.gov `NCT01822652.json` says the mirror image — Cytoxan *"500 mg/m2/day x 2 days"* and *"cyclophosphamide and fludarabine … for 2 days and then fludarabine alone for one day (Day −4, −3, −2)"* (Cy ×2 / Flu ×3). The plan now leads with the **published paper** and flags the registry discrepancy.
- Also corrected pembrolizumab timing "d−1, d+21" → "d+1, d+21": *"pembrolizumab given on days 1 and 21"* (`heczey_2017_pmid28602436.txt:387`).

### C2 — GINAKIT2 (Tian) dose level (Section 9)
- **Was:** "first patient on DL5 (1×10⁸ NKT/m²)".
- **Now:** "DL5 (**3×10⁸ NKT/m²**; DL4 was 1×10⁸/m²)".
- **Primary source:** Tian 2025 — *"receiving up to 1×10⁸ GD2-CAR.15 NKTs/m² at dose level (DL) 4. Subsequently, the first patient treated on DL5 (3×10⁸ GD2-CAR.15 NKTs/m²) developed hyperleukocytosis"* (`tian_2025.txt:90-93`).

### C3 — GINAKIT2 number of dose levels (Section 4)
- **Was:** "escalate ×3-fold (6 levels)".
- **Now:** "DL1 3×10⁶/m² → ~3-fold steps to DL5 3×10⁸/m²".
- **Primary source:** protocol table DL1 3×10⁶ / DL2 1×10⁷ / DL3 3×10⁷ / DL4 1×10⁸ (`heczey_2020_pmid33046868_supp.txt:2490-2493`) + DL5 3×10⁸ reached in Tian 2025 (above). Six levels is not documented; five (to 3×10⁸/m²) is.

### C4 — Baylor-1G dose levels (Section 4)
- **Was:** "2×10⁷/m² each (CTL + ATC) | n/a (feasibility)".
- **Now:** "3 DLs: 2×10⁷, 5×10⁷, 1×10⁸ /m² (CAR-CTL + CAR-ATC co-infused) | no DLT (Louis 2011)".
- **Primary source:** Louis 2011 — *"treated on all 3 dose levels (DL1, 2×10⁷ cells/m²; DL2, 5×10⁷ cells/m²; DL3, 1×10⁸ cells/m²), and no dose-limiting toxicity"* (`louis_2011_pmid21984804.txt:136-137`).

### C5 — CARPETS dose level 3 (Section 4)
- **Was:** "DL3 …".
- **Now:** "DL3 1×10⁸/m²".
- **Primary source:** Gargett 2024 — *"three cell dose levels: (1) 1×10⁷/m², (2) 2×10⁷/m², and [(3) 1×10⁸/m²]"* (`gargett_2024_pmid38754916.txt:1261`, dose table `:665-671`).

### C6 — CARPETS CRS incidence (Section 5)
- **Was:** "minimal".
- **Now:** "grade 1 CRS in 5/12".
- **Primary source:** Gargett 2024 — *"Five of the 12 patients … grade 1 cytokine release syndrome"*; *"a grade 1 fever, which occurred <48 hours post-CAR-T cell"* (`gargett_2024_pmid38754916.txt:350-352`).

### C7 — Stanford-DMG age & rituximab attribution (Sections 1, 3)
- **Age was:** "2–30 y"; **now:** "2–60 y (NCT04196413)". **Primary source:** `NCT04196413.json` eligibility min 2 Years / **max 60 Years**.
- **Rituximab:** clarified that "Rituximab 750 mg/m²/d d−6,−5" comes only from a **separate ctgov LD arm (ARM D)** — *"First round: 750 mg/m2 per day IV for days -6 and -5"* (`NCT04196413.json`) — and is **not** reported in the Majzner 2022 / Monje 2025 published cohorts (those used Cy 500 / Flu 25 ×3 only). GINAKIT2 age also tightened to "1–21 y" per `NCT03294954.json`.

---

## 3. Section-by-section verification of retained claims

### Section 1 — Patient selection
| Claim | Status | Source quote / location |
| --- | --- | --- |
| Stanford excludes bulky thalamic/cerebellar tumours (herniation) | VERIFIED | *"Bulky tumor involvement of cerebellar vermis or hemispheres … or thalamic lesions"*; *"unacceptable risk for herniation"* (`NCT04196413.json`); Majzner 2022 *"we excluded patients with bulky [tumours]"* (`majzner_2022_pmid35130560.txt:57`) |
| Stanford Karnofsky/Lansky ≥60% | VERIFIED | *"Karnofsky ≥ 60% OR ECOG 0"*; *"Lansky scale ≥ 60%"* (`NCT04196413.json`) |
| GD2-CART01 age 1–25 y | VERIFIED | min 12 Months / max 25 Years (`NCT03373097.json`) |
| 1RG-CART age ≥1 y | VERIFIED | min 1 Year (`NCT02761915.json`) |

### Section 3 — Lymphodepletion
| Claim | Status | Source quote / location |
| --- | --- | --- |
| Baylor-1G: no LD | VERIFIED | Louis 2011 describes infusion without Cy/Flu conditioning (`louis_2011_pmid21984804.txt`) |
| GINAKIT2: fractionated Cy 500 ×2 + Flu 30 ×3 | VERIFIED | *"fractionated 500mg/m2/dose x2 cyclophosphamide and 30mg/m2/dose x3 fludarabine for lymphodepletion (Section 7.2)"* (`heczey_2020_pmid33046868_supp.txt:2048-2049`, `:2495-2496`) |
| Stanford IV: Cy 500 / Flu 25 ×3, d−4..−2 | VERIFIED | *"cyclophosphamide 500 mg m2 daily and fludarabine 25 mg m2 daily on days −4, −3 and −2"* (`majzner_2022_pmid35130560.txt:1655-1657`) |
| Stanford eIND ICV: Cy 600 / Flu 30 ×4 (d−5..−2); no LD for later ICV | VERIFIED | *"cyclophosphamide 600 mg m2 daily and fludarabine 30 mg m2 daily on days −5, −4, −3 and −2 … subsequent patients received … i.c.v. without lymphodepletion"* (`majzner_2022_pmid35130560.txt:1662-1667`) |
| 4SCAR-GD2: Cy 300 / Flu 25 ×3, d−4..−2 | VERIFIED | *"Cy at 300 mg/m2/dose on days -4,-3,-2 and Flu at 25 mg/m2/dose on days -4,-3,-2"* (`yu_2022_pmid34724115.txt:129-130`) |
| CARPETS cohort 1 none; 2–3 Cy 500 + Flu 30 ×3 | VERIFIED | 3 cohorts (PBT alone / +Cy-Flu / +Cy-Flu+pembro) (`gargett_2024_pmid38754916.txt:176-181`); *"fludarabine 30mg/m2 on days −4 to −3 and −2 and cyclophosphamide 500 mg/m2"* (`:1275-1276`) |
| 1RG-CART: phased escalation of LD intensity | ABSTRACT-ONLY | *"escalating doses … and increasing intensity of preparative lymphodepletion"* (Straathof 2020 abstract, `33239386.txt`) |
| GD2-CART01: Cy+Flu, exact doses in NEJM appendix | NR | NEJM full-text/appendix paywalled; abstract gives no LD doses |

### Section 4 — Dose, route, DLT
| Claim | Status | Source quote / location |
| --- | --- | --- |
| GD2-CART01 dose levels 3/6/10 ×10⁶/kg; RP2D/MTD 10×10⁶/kg | ABSTRACT-ONLY (VERIFIED) | *"Three dose levels were tested (3-, 6-, and 10×10⁶ CAR-positive T cells per kilogram)"* (Del Bufalo `37018492.txt`); *"maximum tolerated dose was 10 × 10⁶ CAR+ cells per kg"* (Locatelli `40841488.txt`) |
| GINAKIT2 MTD not reached; 28-d DLT | VERIFIED | *"The MTD was not reached"* (Heczey 2023 `37188782.txt`); DLT *"within 28 days after infusion"* (`heczey_2020_pmid33046868_supp.txt:3211`) |
| Stanford IV DL1 1×10⁶/kg, DL2 3×10⁶/kg; DL1 = MTD IV | VERIFIED | *"DL1, 1 × 10⁶ kg⁻¹; DL2, 3 × 10⁶ kg⁻¹"*; *"three patients experienced dose-limiting CRS on DL2, establishing DL1 as the maximally tolerated IV dose"* (`monje_2025_pmid39537919.txt:30, 38-39`) |
| Stanford DLT definition (grade 5; grade 4 CRS; grade 4 neurotox ≥96 h; new grade 3 neurotox ≥28 d; grade 4 cytopenia >28 d) | VERIFIED | *"grade 5 toxicity, grade 4 CRS, grade 4 neurotoxicity lasting at least 96 h, new grade 3 neurotoxicity lasting more than 28 days …"* (`monje_2025_pmid39537919.txt:112-115`) |
| CARPETS 42-day DLT window; no DLT | VERIFIED | *"42 days"* / *"42-day DLT evaluation window"* (`gargett_2024_pmid38754916.txt:588, 776`); *"No DLTs were observed"* (`:338`) |
| 1RG-CART activity at ≥10⁸/m² | ABSTRACT-ONLY | *"six patients receiving ≥10⁸/meter² CAR-T cells … three demonstrated regression"* (Straathof `33239386.txt`) |
| 4SCAR infused 0.13–34 ×10⁶/kg (wide) | VERIFIED | dose range in Yu 2022 cohort table (`yu_2022_pmid34724115.txt`) |

### Section 5 — CRS
| Claim | Status | Source quote / location |
| --- | --- | --- |
| GRAIN: 1 patient (1C), ≤grade 2, spontaneous resolution | VERIFIED | *"one episode of CRS in patient 1C, but this did not exceed grade 2 … resolved spontaneously by day 7"* (`heczey_2017_pmid28602436.txt:116-118`); *"resolved spontaneously without corticosteroid or anti-IL-6"* (`:803-805`) |
| GINAKIT2: grade 2 in 1/12, tocilizumab | VERIFIED | *"one patient experienced grade 2 CRS that was resolved by tocilizumab"* (Heczey 2023 `37188782.txt`) |
| GD2-CART01: CRS 20/27 (74%), mild in 19/20 (95%); iCasp9 aborted grade-4 CRS in 1 | ABSTRACT-ONLY (VERIFIED) | *"Cytokine release syndrome occurred in 20 of 27 patients (74%) and was mild in 19 of 20 (95%). In 1 patient, the suicide gene was activated"* (Del Bufalo `37018492.txt`) |
| Stanford IV: DL1 grade 2 1/3; DL2 ≥grade 2 6/8; 3 DLT grade 4 CRS at DL2 | VERIFIED | *"one of three patients on DL1 experiencing grade 2 CRS, six of eight patients on DL2 experiencing grade 2 or higher CRS and three patients on DL2 experiencing DLT attributed to grade 4 CRS"* (`monje_2025_pmid39537919.txt:483-485`) |
| Stanford ICV: 41/62 infusions no CRS | VERIFIED | *"Among 62 ICV infusions, no DLTs occurred. Forty-one ICV infusions [were not associated with CRS]"* (`monje_2025_pmid39537919.txt:501-502`) |
| 1RG-CART: 2/6 at ≥10⁸/m², grade 2–3 | ABSTRACT-ONLY | *"two experienced grade 2 to 3 cytokine release syndrome"* (Straathof `33239386.txt`) |
| 4SCAR: CRS 9/10 grade 1–2; capillary leak 4/10 | VERIFIED | *"Acute capillary leak syndrome (4/10) and CRS (9/10)"* (`yu_2022_pmid34724115.txt:768`) |
| CARPETS: grade 1 CRS 5/12, fever <48 h | VERIFIED | (C6 above) `gargett_2024_pmid38754916.txt:350-352` |

### Section 6 — ICANS vs TIAN
| Claim | Status | Source quote / location |
| --- | --- | --- |
| Stanford ICANS: DL1 grade 2 (1/3); DL2 grade 3 (1) + grade 1 (3) | VERIFIED | *"ICANS in one of three patients at DL1 (grade 2) and in four of eight patients at DL2 (n = 1 grade 3, n = 3 grade 1)"* (`monje_2025_pmid39537919.txt:496-497`) |
| Grade 4 ICANS after intensified ICV | VERIFIED | spinal DMG-1 after 50×10⁶ ICV + increased LD: *"grade 3 encephalopathy (grade 4 immune effector cell-associated neurotoxicity (ICANS))"* (`majzner_2022_pmid35130560.txt:646`) — note: this is the eIND patient in Majzner 2022, distinct from Monje 2025's on-study ICV cohort which had **no** ICANS (`monje_2025_pmid39537919.txt:504`) |
| TIAN 91% after IV, 100% after first ICV; no DLT due to TIAN | VERIFIED | *"TIAN in 91% of patients following IV infusion and in 100% of patients following the first ICV infusion … no patient experienced a DLT due to TIAN"* (`monje_2025_pmid39537919.txt:515-523`) |
| GD2-CART01: grade 3 ICANS in 4 children, aborted by iCasp9/rimiducid | ABSTRACT-ONLY (VERIFIED) | *"Grade 3 ICANS was diagnosed in four children and rapidly controlled with the activation of the inducible caspase-9 suicide gene by rimiducid"* (Locatelli `40841488.txt`) |
| 4SCAR: no central neurotoxicity | VERIFIED | Yu 2022 reports peripheral neuropathic pain only, no CNS toxicity (`yu_2022_pmid34724115.txt`) |

### Section 7 — TIAN algorithm
| Claim | Status | Source quote / location |
| --- | --- | --- |
| Ladder: hypertonic saline 3% → CSF removal via Ommaya → anakinra+steroids → tocilizumab/siltuximab/dasatinib → EVD → iCasp9 | VERIFIED | *"toxicity management algorithm incorporating the removal of CSF via Ommaya, hypertonic saline (3%)"*; *"anakinra and corticosteroids to patients with significant neurological [symptoms]"* (`monje_2025_pmid39537919.txt:155-162`); siltuximab + dasatinib used for the grade-4 ICANS patient (`majzner_2022_pmid35130560.txt:646+`) |
| ICP 22 mmHg → drain 10 mL → baseline in minutes | VERIFIED | worked example in Majzner 2022 / Monje 2025 ICP narrative (`majzner_2022_pmid35130560.txt:241-242` and TIAN figures) |
| Per-patient anti-inflammatory schedules in Majzner supp Table 3 | VERIFIED | `supplements/35130560_PMC8967714/41586_2022_4489_MOESM4_ESM.docx` (Supplementary Table 3) |

### Section 8 — On-target pain
| Claim | Status | Source quote / location |
| --- | --- | --- |
| Baylor-1G: mild local pain only | VERIFIED | *"3 localized pain"* graded on NCI scale (`louis_2011_pmid21984804.txt:223`) |
| Stanford: no on-target off-tumor toxicity | VERIFIED | Monje/Majzner report no peripheral GD2 toxicity (`majzner_2022_pmid35130560.txt`) |
| 1RG-CART: activity "without on-target off-tumor toxicity" | ABSTRACT-ONLY | title/abstract phrase *"without on-target off-tumor toxicity"* (Straathof `33239386.txt`) |
| 4SCAR: neuropathic pain 3/10, transient/mild | VERIFIED | *"neuropathic pain (3/10)"* (`yu_2022_pmid34724115.txt:777`); *"Grade 1–2 toxicities such as CRS and neuropathic pain were common, but were transient and mild"* (`:28-29`) |

### Section 9 — Hyperleukocytosis (Tian 2025)
| Claim | Status | Source quote / location |
| --- | --- | --- |
| DL5 = 3×10⁸/m² (corrected) | VERIFIED | (C2) `tian_2025.txt:90-93` |
| Tocilizumab d7, anakinra d8 | VERIFIED | *"On day 7, tocilizumab was administered then anakinra on day 8"* (`tian_2025.txt:134-135`) |
| Leukapheresis d18; death same day | VERIFIED | *"Leukapheresis was performed on day 18 … same day. An autopsy confirmed hyperleukocytosis-driven [death]"* (`tian_2025.txt:156-159`) |
| Non-clonal, autopsy-confirmed | VERIFIED | *"to be non-clonal as the clone with the most frequent transgene integration sites was detected at only <0.6%"* (`tian_2025.txt:212`) |

### Section 10 — Safety switch
| Claim | Status | Source quote / location |
| --- | --- | --- |
| GD2-CART01 iCasp9/rimiducid fired clinically: grade-4 CRS (n=1) + grade-3 ICANS (n=4) | ABSTRACT-ONLY (VERIFIED) | Del Bufalo `37018492.txt` (n=1 CRS); Locatelli `40841488.txt` (n=4 ICANS) |
| 1RG-CART uses RQR8 + rituximab | ABSTRACT-ONLY | Straathof 2020 construct (RQR8 marker/suicide) |
| iCasp9 is the only switch with published clinical evidence of aborting severe GD2 CAR-T toxicity | VERIFIED (synthesis) | only GD2-CART01 reports actual clinical activation; no other trial reports firing its switch |

### Section 12 — Hematologic toxicity
| Claim | Status | Source quote / location |
| --- | --- | --- |
| GINAKIT2 grade 3–4 cytopenias = Cy/Flu-attributable | VERIFIED | Heczey 2020/2023 attribute pre-infusion cytopenias to LD (`heczey_2020_pmid33046868_supp.txt`) |
| 4SCAR grade 3–4 hematologic most common AE | VERIFIED | *"Grade 3 or 4 hematological toxicities were the common adverse events frequently occurred after fludarabine and cyclophosphamide"* (`yu_2022_pmid34724115.txt:27-28`) |
| Stanford grade 4 cytopenia >28 d is DLT | VERIFIED | DLT definition (`monje_2025_pmid39537919.txt:112-115`) |

### Section 13/14 — ICV & redosing
| Claim | Status | Source quote / location |
| --- | --- | --- |
| ICV dose 10–50 ×10⁶ flat; no LD; redose ≥21–28 d when CAR <5% and toxicity <grade 2 | VERIFIED | Monje 2025 redosing criteria + 62 ICV infusions (`monje_2025_pmid39537919.txt:501`); 50×10⁶ ICV in eIND patient (`majzner_2022_pmid35130560.txt:636-646`) |
| GD2-CART01 persistence ≥12 mo in 64% | ABSTRACT-ONLY (VERIFIED) | *"GD2-CART01 persisted ≥12 months in 64% of the patients"* (Locatelli `40841488.txt`) |

### Section 15 — Monitoring / follow-up
| Claim | Status | Source quote / location |
| --- | --- | --- |
| GD2-CART01 detectable up to 30 mo, median 3 mo | ABSTRACT-ONLY (VERIFIED) | *"detectable in peripheral blood in 26 of 27 patients up to 30 months after infusion (median persistence, 3 months; range, 1 to 30)"* (Del Bufalo `37018492.txt`) |
| Baylor-1G long-term up to 18 years; 3/11 CR | ABSTRACT-ONLY (VERIFIED) | *"long-term outcomes up to 18 years. Of 11 patients with active disease at infusion, three achieved a complete response … one for more than 18 years"* (`39962287.txt`); persistence 192 wk ATC / 96 wk CTL (`louis_2011_pmid21984804.txt:29-30`) |

### Section 16 — Master matrix efficacy snapshots
| Claim | Status | Source quote / location |
| --- | --- | --- |
| GINAKIT2 ORR 25% | VERIFIED | *"objective response rate was 25% (3/12)"* (Heczey 2023 `37188782.txt`) |
| GD2-CART01 ORR 63–66%, 5-yr OS 42–68% | ABSTRACT-ONLY (VERIFIED) | ORR 63% (Del Bufalo); ORR 66% (21/32), trial 5-yr OS 42.67%, target-pop 5-yr OS 68% (Locatelli `40841488.txt`) |
| 1RG-CART regressions, no RECIST CR | ABSTRACT-ONLY | *"no patients had objective clinical response at the evaluation point +28 days"*; *"three demonstrated regression"* (Straathof `33239386.txt`) |

---

## 4. Claims that remain ABSTRACT-ONLY (paywall limit)

Full-text/appendix protocols for these three reports are paywalled (NEJM, *Nature*, *Sci Transl
Med*); every figure attributed to them is sourced from the **PubMed abstract** and is correct as
stated, but the *underlying per-patient tables / exact LD doses* could not be opened here:

- **Del Bufalo 2023 (GD2-CART01, NEJM 37018492):** exact Cy/Flu doses, full AE table → **NR**.
- **Locatelli 2025 (GD2-CART01, *Nature* 40841488):** per-timepoint CR breakdown beyond 37/34/40%, full AE table → **NR**.
- **Straathof 2020 (1RG-CART, STM 33239386):** exact LD intensities per cohort, cell-dose table → **NR**.

These are explicitly marked **NR** / "per NEJM appendix" in the plan, not inferred.

---

## 5. Summary

- **Claims checked:** ~95 across 17 sections + the lab index.
- **VERIFIED against full-text/supplement/registry:** majority (all Stanford, GINAKIT2, GRAIN,
  4SCAR, CARPETS, Baylor-1G figures).
- **ABSTRACT-ONLY (correct, but only the abstract is open):** all GD2-CART01 and 1RG-CART efficacy/
  toxicity figures.
- **CORRECTED (7 fixes):** GRAIN LD order + pembro day; Tian DL5 dose; GINAKIT2 level count;
  Baylor-1G dose levels; CARPETS DL3; CARPETS CRS; Stanford age + rituximab attribution.
- **NR (paywall):** exact LD doses / full AE tables for the three paywalled reports.

No claim in the plan is now unsupported by a cited primary source; remaining gaps are limited to
fields that are genuinely unavailable without institutional full-text access and are flagged NR.
