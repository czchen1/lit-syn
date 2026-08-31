# Benchmarking a Vδ1-dominant γδ T-cell result against the literature

Result being benchmarked (as provided):

- ~80% Vδ1 γδ T cells in the product
- a CD4−CD8− (double-negative, DN) population
- cytotoxicity measured at an E:T ratio of 10:1

The three numbers benchmark very differently: **80% Vδ1 is a meaningful, comparable purity number**; **DN is an expected lineage property and not a discriminating readout**; and **"10:1" is an assay setting, not a result** — it cannot be compared to anything until the target, assay duration, readout, and % killing are stated. Each section below gives the published values, then what the comparison does and does not support.

---

## 1. Vδ1 purity: 80% is a real enrichment, mid-pack among Vδ1 products

Baseline: Vδ1 cells are a minor blood subset. Vδ1 T cells are 0.2–1.0% of PBMCs (Nishimoto 2025, PMID 40592738), and starting Vδ1 frequency before expansion has been measured at a median 0.36% (range 0.02–0.71%) of the culture input (Makkouk 2021, PMID 34916256). Reaching 80% Vδ1 is therefore a ~100–400-fold enrichment over input frequency, i.e. squarely in the range that requires selective expansion plus αβ (and usually Vδ2) depletion.

| Product / protocol | Reported Vδ1 content of final product | Source |
| --- | --- | --- |
| ADI-001 allogeneic Vδ1 CAR (large-scale GMP) | 93% Vδ1+, 0.2% Vδ2+, 0.9% Vδ1−Vδ2− γδ, 1.8% NK, 0.03% αβ; 23,983-fold Vδ1 expansion (range 9,569–34,321) | Nishimoto 2022, PMID 35136603 |
| ADI-270 (CD70 CAR-Vδ1) | 92.5% ± 2.1% Vδ1, of which 72.0% ± 7.5% CAR+ | Nishimoto 2025, PMID 40592738 |
| GPC-3.CAR/sIL-15 Vδ1 | 72.4% (range 35.3–92.6%) after expansion, ~90% (83.3–96.2%) after αβ depletion; "routinely >80% purity"; ~20,000-fold expansion | Makkouk 2021, PMID 34916256 |
| Vδ1 product with Vδ2 depletion mid-culture | ~77% Vδ1 with ~17% Vδ1−Vδ2− γδ; ~72% Vδ1 / ~20% Vδ1−Vδ2− if depleted at harvest; without depletion, ≥50% Vδ1 only when input Vδ1:Vδ2 > 0.4:1 | Ferry 2022, PMID 35711450 |
| Delta One T (DOT) cells | release criterion for experimental use: ≥65% Vδ1+ | Carreira 2026, PMID 42208977 |
| αβ-depleted polyclonal γδ product | 88.1% ± 4.2% purity — *total γδ*, not Vδ1 | Siegers 2013, PMID 23100099 |

Interpretation:

- 80% Vδ1 is **above** the DOT experimental threshold (≥65%) and above Vδ2-depleted Vδ1 products (~72–77%), **within** the "routinely >80%" band reported for Makkouk-type Vδ1 CAR products, and **below** the 92–93% reported for the ADI-001/ADI-270 GMP process.
- The comparison is only valid against *Vδ1-specific* purity. Do not benchmark 80% Vδ1 against numbers like Siegers' 88.1%, which is total TCRγδ+ purity and would correspond to a much lower Vδ1 fraction unless Vδ1-dominant.
- For an allogeneic product the more decision-relevant number is **not** Vδ1 purity but residual αβ T cells (GvHD risk) — reported at 0.03% by Nishimoto 2022. A 20% non-Vδ1 remainder is only interpretable once broken down into Vδ2, Vδ1−Vδ2− γδ, NK (CD3−CD56+), and αβ T cells. Ferry 2022 is the cautionary case: the non-Vδ1 fraction there was mostly Vδ1−Vδ2− γδ cells (~17–20%), and CD56 rose on 50–70% of Vδ1 cells during expansion, so CD56 cannot be used to gate out contaminants.

## 2. Double-negative: expected for γδ, and easy to conflate with the DNT field

- CD4−CD8− is the **default** γδ phenotype: most peripheral γδ T cells are CD3+CD4−CD8− (Re 2005, PMID 15686597), with ~20–30% CD8 single-positive and 0.1–7% CD4+ among Vγ9Vδ2 cells (Holmen Olofsson 2021, PMID 34149689). The DN state is a lineage property retained on thymic exit rather than an activation or potency marker (Deniger 2014, PMID 25566249). Intratumoral γδ T cells are likewise largely CD4−CD8− (Lee 2021, PMID 34071865), and expanded Vγ9Vδ2 products are described as primarily CD3+CD4−CD8− (Baker 2019, PMID 32038628).
- So a DN population in a Vδ1-dominant product is **consistent with**, not distinctive of, the literature. It carries no potency information on its own.
- The reverse inference is invalid: a CD3+CD4−CD8− gate is not a γδ gate. γδ T cells were only 39.6% ± 21.1% of CD4−CD8− T cells in healthy donors (and significantly less in AML patients) — Eckstrom 2025, PMID 41097694. Gating conventions differ across papers (e.g. DN T = CD3+CD4−CD8− vs γδ = CD3+CD4−CD8−TCRγδ+ in Kowli 2025, PMID 39965168; DNT = CD3+TCRαβ+CD4−CD8− in Ma 2026, PMID 42344891), so the definition must be stated.
- **Do not benchmark against the "DNT cell" therapy literature as if it were the same product.** Those products are defined as CD3+CD4−CD8− and contain αβ T cells plus both Vδ1 and Vδ2 cells (Tin 2025, PMID 40246580); their killing data (e.g. 20.34% specific killing of TNBC at E:T 10:1, Wang 2022, PMID 35894707; CD19-CAR-DNT, Wang 2024, PMID 39720695) are not Vδ1 benchmarks.
- High DN fractions also occur as disease phenomena unrelated to manufacturing — e.g. DN 67.4% of CD3+ cells in STK4 deficiency, which proved to be Vδ2+ γδ cells (Ying 2024, PMID 39110273).

What to report to make the DN number comparable: DN% **within** TCRγδ+Vδ1+ cells (not within CD3+), plus the CD8+ fraction of Vδ1 cells, since CD4/CD8 co-receptor status has been proposed — but not established for Vδ1 — to track with cytotoxic capacity (David 2026, PMID 42008532, discusses this explicitly as an open possibility).

## 3. Cytotoxicity at E:T 10:1: the ratio alone is not comparable

Published % killing at 10:1 spans ~20% to ~78% depending almost entirely on effector subset, target, assay length, and readout.

| Effector | Target | E:T 10:1 result | Assay | Source |
| --- | --- | --- | --- | --- |
| Cord-blood Vδ1+ | U937 | 77.7% ± 10.5% (vs adult Vδ2+ 63.8% ± 12.8%) | flow killing | Hur 2023, PMID 36851283 |
| Cord-blood Vδ1+ | K562 | 49.5% ± 17.4% (vs adult Vδ2+ 57.2% ± 34%) | flow killing | Hur 2023, PMID 36851283 |
| Sorted Vδ1 | endometrial lines KLE / RL95-2 / Ishikawa | 34.8% ± 1.3 / 35.9% ± 14.2 / 37.8% ± 4.3 | specific lysis | Hudecek 2021, PMID 34691070 |
| Healthy-donor sorted Vδ1 | primary CML cells | 30.1% ± 3.0 at 10:1 vs 22.6% at 5:1 (CML *lines* only 12–15% at 5:1) | 4 h specific lysis | Knight 2023, PMID 36376516 |
| Expanded Vδ1 vs Vδ2 | OVCAR8 / MDA-MB-231 | Vδ1 > Vδ2 at 2.5:1 and 5:1; **no gain from 5:1 to 10:1** | 5 h | Portillo 2025, PMID 40996786 |
| Vγ9Vδ2 | breast cancer organoids | maximal killing at 10:1 (5.2 ± 0.5 RFU fold-change), less at 1:1 and 5:1 | 24 h | Su 2026, PMID 42035083 |
| Bulk γδ | TNBC lines | 10:1 significantly > 5:1 **and > 20:1** | coculture | Qiu 2025, PMID 40289760 |
| Bulk γδ | GBM PDX cells | 10:1 used as the previously published optimum for GBM | — | Jones 2024, PMID 39199623 |
| DNT product | TNBC | 20.34% average specific killing | — | Wang 2022, PMID 35894707 |

Key caveats this table makes explicit:

1. **Target identity dominates.** The same Vδ1 effectors killed U937 at 77.7% and K562 at 49.5% in one study; sorted Vδ1 cells reached only ~30–38% against solid-tumor lines in 4–5 h assays. A 10:1 number against a hematologic line and a 10:1 number against an adherent solid-tumor line are not the same benchmark.
2. **Assay duration is confounded with ratio.** Modern Vδ1 products are usually characterized at *low* ratios over long assays: ADI-270 at 1:1 for 24–72 h (PMID 40592738), DOT cells at 5:1 for 3 or 24 h (Mensurado 2024, PMID 38437507), CAR-Vδ1 at 1:2–2:1 for 24 h (Li 2025, PMID 40930745). A 10:1 short-duration assay is a comparatively permissive condition, and David 2026 (PMID 42008532) attributes its own failure to detect killing at 1:1 to exactly this difference from studies using 5:1–20:1.
3. **10:1 is often at or past saturation.** Portillo 2025 saw no improvement from 5:1 to 10:1; Qiu 2025 found 10:1 *better* than 20:1. A single 10:1 point therefore cannot establish dose-dependence; a titration (e.g. 1:1, 2.5:1, 5:1, 10:1) is what makes the result comparable and is standard in the papers above.
4. **The denominator of "E" matters.** In an 80% Vδ1 product, a nominal 10:1 is ~8:1 in Vδ1 cells. Nishimoto 2025 defines effectors as Vδ1+CAR+ viable cells; Morandi 2026 (PMID 41694338) explicitly flags that not normalizing for the NK fraction in a mixed product makes its stated E:T "highly challenging" and non-comparable. State whether E is total viable cells or Vδ1-gated.

## 4. Bottom line

- 80% Vδ1 is a legitimate, well-supported Vδ1-enriched product composition — better than Vδ2-depletion-based protocols (~72–77%) and DOT release criteria (≥65%), short of the 92–93% GMP Vδ1 processes. It is not an outlier in either direction.
- The DN population is expected and adds no benchmark signal; it must be reported within TCRγδ+ cells, and must not be compared to CD3+CD4−CD8− "DNT cell" products.
- The 10:1 cytotoxicity result cannot yet be placed. Against solid-tumor lines in short assays the relevant Vδ1 comparators are ~30–38% specific lysis at 10:1; against myeloid/lymphoid lines ~50–78%. Which band applies depends on details not yet specified.

## 5. What is needed to complete the comparison

1. % specific lysis / killing at 10:1, with SD and donor n.
2. Target cells (line vs primary vs organoid) and their relevant ligand expression (e.g. CD70, MICA/B, ULBP, GPC-3).
3. Assay duration and readout (4 h flow/chromium vs 24–72 h luciferase/IncuCyte/LDH).
4. Whether E:T is calculated on total viable cells or on Vδ1-gated cells.
5. Composition of the non-Vδ1 20%: Vδ2, Vδ1−Vδ2− γδ, NK, αβ T.
6. Whether the DN gate was drawn within CD3+ or within TCRγδ+, and CD8+ fraction of Vδ1.
7. Cell source (adult PB vs cord blood — Hur 2023 shows source changes Vδ1 killing substantially) and expansion protocol / fold expansion.
