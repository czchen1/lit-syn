# DHG-H3G34 pathway-directed treatment options, prioritized for brain penetrance

## Scope

For the same DHG-H3G34 CSF ctDNA variant set analyzed in `dhg_h3g34_mutation_pathway_synthesis.md`, this note ranks **pathway-directed therapeutic options by blood–brain-barrier (BBB) penetrance**, combining (a) mechanism fit to a detected alteration, (b) documented CNS/intracranial exposure, and (c) glioma-specific clinical evidence. Trials listed in the source report are cross-referenced. This is a literature synthesis, **not** clinical advice; treatment decisions require a neuro-oncology tumor board, germline/confirmatory testing, and eligibility review.

Two genome-wide modifiers from the report shape the whole strategy:
- **TMB low / MSI stable (MSS)** → single-agent immune-checkpoint blockade is unlikely to benefit on a biomarker basis.
- **TP53 R273C is the dominant clone (VAF 54.3%)** → strategies that depend on *reactivating wild-type p53* (MDM2/MDM4 inhibitors) are mechanistically undermined (see §p53).

## Brain-penetrance tiers (agents referenced here)

- **CNS-optimized / direct glioma PK or efficacy data:** paxalisib; niraparib; BDTX-1535 (silevertinib); capmatinib; vebreltinib; mirdametinib; avapritinib; abemaciclib.
- **Moderate / mixed:** trametinib; ribociclib; brigimadlin (BI 907828; GBM phase 0/1a but TP53-WT only).
- **Efflux-limited / poor CNS:** navtemadlin (Kp,brain ≈ 0.009); olaparib; talazoparib (P-gp substrate); alpelisib; palbociclib.

## Prioritized table

| Priority | Pathway / target (alteration) | Lead brain-penetrant agent(s) | Brain penetrance | Glioma/CNS evidence | Report-matched trial | Caveats |
|---|---|---|---|---|---|---|
| 1 | DDR / ALT (ATRX loss history; H3G34R; TP53) | **Niraparib** ± topotecan/irinotecan | High — superior to olaparib; adequate GBM tumor PK in phase 0 | Phase 0/2 niraparib GBM; phase 0 in recurrent ATRX-mutant glioma (NCT05076513); niraparib+topotecan response in a DHG-H3G34R_ATRX patient (Kfoury 2025) | TalaCom (talazoparib combos, NCT04693468) — note talazoparib is more P-gp-effluxed than niraparib | **ATRX/ALT was not detected in this CSF specimen** — confirm ALT/ATRX status before relying on this rationale; myelosuppression (thrombocytopenia) |
| 2 | PI3K/AKT/mTOR (PIK3CA H1047R; converges with PDGFRA/EGFR/MET) | **Paxalisib (GDC-0084)** | High — purpose-built brain-penetrant PI3K/mTOR | Phase 2 newly-diagnosed GBM (NCT03522298); GBM AGILE | — | Hyperglycemia/stomatitis; pan-PI3K (not mutant-selective) |
| 2b | PI3Kα-mutant-selective (PIK3CA H1047R) | RLY-2608 (zovegalisib), STX-478 (tersolisib), OKI-219, ETX-636 | Unproven in CNS | First-in-human solid-tumor responses; far less hyperglycemia than alpelisib | RLY-2608 (NCT05216432); STX-478 (NCT05768139); OKI-219 (NCT06239467); ETX-636 (NCT06993844); TER-2013 (NCT07109726) | CNS exposure not yet established; better *selectivity* than paxalisib but weaker *brain-penetrance* evidence |
| 3 | RTK — PDGFRA Y288C | **Avapritinib** | High — BBB penetrance + responses in PDGFRA-altered pediatric HGG (Cell 2025) | Real-world radiographic responses in PDGFRA-altered HGG | Avapritinib (NCT04771520) | **Extracellular Y288C neomorph is reported resistant to PDGFR TKIs** (Ip 2018) and signals via PI3K/mTOR+MEK — favor downstream blockade for this specific allele; subclonal (3.1%); intracranial-hemorrhage risk |
| 4 | RTK — EGFR gain | **BDTX-1535 (silevertinib)** | High — 4th-gen brain-penetrant EGFR "MasterKey" | Dedicated GBM CNS-penetration trials (NCT06072586 phase 0/1; NCT05256290) | BDTX-1535 ± RT ± TMZ (NCT06072586) | EGFR-targeted therapy historically low yield in GBM; copy gain ≠ activating mutation |
| 5 | RTK — MET gain | **Capmatinib** or **Vebreltinib** | High — both favorable BBB, minimal P-gp efflux | Capmatinib effective in MET-fusion pHGG models + RT synergy; vebreltinib phase III glioma (PTPRZ1-MET) | Vebreltinib (NCT03175224) | Strongest MET data is for *fusions/exon14*; here MET is arm-level gain (weaker rationale) |
| 6 | RAS/MAPK — PTPN11 S502P (SHP2) | **Mirdametinib** (brain-penetrant MEK1/2) or **trametinib**; SHP2i KQB198 | Mirdametinib CNS-optimized (St. Jude SJ901 pLGG); trametinib used in CNS | MEK inhibitors active in pediatric LGG/MAPK-driven glioma | KQB198 (SHP2, NCT06507306); avutometinib (RAF/MEK, NCT06104488) | Subclonal (0.8%); SHP2-inhibitor CNS penetrance unknown; MEKi also rational downstream of PDGFRA-Y288C |
| — | p53 — MDM4 gain / TP53 R273C / PPM1D | MDM2i: brigimadlin (BI 907828), navtemadlin | Brigimadlin has GBM phase 0/1a (NCT05376800); navtemadlin **poor** (Kp,brain ≈ 0.009) | Navtemadlin GBM window-of-opportunity trial | BTP-114, LP-184 (NCT02950064, NCT05933265) | **Deprioritize:** MDM2/MDM4 inhibition needs *wild-type* p53; dominant TP53 R273C abrogates it (brigimadlin GBM trial enrolls TP53-WT only). Theoretical exception: a *p53-wildtype, PPM1D-truncated* subclone (PPM1D-mut models are MDM2i-sensitive) |
| — | Cell cycle — RB1 loss | CDK4/6i: abemaciclib (best CNS), ribociclib | Abemaciclib highest brain TER; ribociclib moderate; palbociclib not recommended | Abemaciclib rGBM trial requires **intact RB** | CID-078 (CDK, NCT06577987) | **Deprioritize:** CDK4/6 act upstream of RB; **RB1 loss predicts resistance** (Wiedemeyer 2010). Contrast with CDK6 dependency seen in *RB-intact* DHG-H3G34 (Liu 2024) |
| — | Epigenetic — H3-3A G35R / H3K36me3 | No brain-penetrant targeted standard | n/a | ONC201/dordaviprone is **H3K27M-specific**, not G34; DOT1L/EZH2/HDAC limited CNS | gene-therapy/immunotherapy trials (NCT06914479, NCT06896110) | Backbone remains maximal safe resection + RT + temozolomide (MGMT is frequently methylated in G34, predicting TMZ benefit — confirm patient MGMT status) |

## PI3K/AKT/mTOR — expanded brain-penetrant asset landscape (paxalisib alternatives)

Agents in the same axis as paxalisib, ranked by documented CNS exposure × glioma/CNS clinical data. Recurring theme: several of these achieve **proven brain penetration yet minimal single-agent efficacy** in PI3K-activated glioma (adaptive feedback/reactivation), so combinations and pathway co-targeting are the realistic path.

| Agent | Target | Brain penetrance | Best CNS/glioma clinical data | Key toxicities |
|---|---|---|---|---|
| **Buparlisib (BKM120)** | pan-class-I PI3K | High — tumor:plasma ≈ 1.0 *proven in rGBM* | Phase 2 recurrent GBM with PI3K activation (NCT01339052); brain penetration confirmed but **PFS6 only ~8%** (minimal single-agent efficacy) | Hyperglycemia, lipase/ALT elevation, fatigue, rash; **neuropsychiatric (mood/depression/anxiety, rare suicidal ideation)** is the class-defining buparlisib AE (not seen in this GBM cohort but prominent elsewhere) |
| **Sapanisertib (TAK-228/MLN0128)** | mTORC1/2 (ATP-competitive) | Demonstrated BBB penetration in surgical-window rGBM | Phase 1 pre/post-surgery rGBM (NCT02133183); phase 1 + bevacizumab (NCT02142803) | Hyperglycemia, stomatitis/mucositis, rash, fatigue, nausea |
| **Samotolisib (LY3023414)** | PI3K/mTOR + **DNA-PK** | Oral; CNS-tumor exposure (pediatric CNS cohorts) | Pediatric MATCH APEC1621D (NCT03213678), incl. 5 HGG; **no ORR, 3-mo PFS 12%** | Mucositis & pneumonitis (DLTs), hyperglycemia, fatigue; RP2D 115 mg/m²/dose BID |
| **Bimiralisib (PQR309)** | dual pan-PI3K/mTOR | **Designed brain-penetrant**; crosses BBB at therapeutic levels | Phase 2 primary CNS lymphoma (NCT02669511); refractory lymphoma phase 1/2 | Hyperglycemia, fatigue, rash, mucositis, thrombocytopenia; milder neuropsychiatric profile than buparlisib |
| **Perifosine** | AKT / membrane (alkylphospholipid) | Modest CNS | Pediatric phase 1 CNS+solid (PLOS One 2017); stable disease in DIPG/HGG, no ORR | GI (nausea/vomiting/diarrhea), hyperuricemia; RP2D 50 mg/m²/day; cytostatic |
| **MK-2206** | allosteric AKT1/2/3 | Studied in pediatric CNS tumors | COG phase 1 incl. CNS tumors (NCT01231919) | Rash, hyperglycemia, fatigue, mucositis; anti-proliferative (cytostatic) not tumoricidal |
| **Voxtalisib (XL765/SAR245409)** | PI3K/mTOR | Modest | Glioma combos with TMZ/RT (recurrent + newly-dx malignant glioma) | LFT elevation, rash, fatigue, GI |
| **Everolimus / temsirolimus (rapalogs)** | mTORC1 | Everolimus modest (effective in TSC SEGA); **temsirolimus poor CNS** (negative GBM trials) | Everolimus widely studied in glioma combos; temsirolimus rGBM negative | Stomatitis, hyperglycemia, hyperlipidemia, immunosuppression/infection, **pneumonitis** |
| **PI3Kα mutant-selective (RLY-2608, STX-478, OKI-219, ETX-636)** | mutant PI3Kα | CNS **unproven** | FIH solid-tumor responses; matched to PIK3CA H1047R here | Far less hyperglycemia than alpelisib; GI, rash (early data) |
| **Alpelisib (reference, not recommended)** | PI3Kα | **Poor CNS** | — | Severe hyperglycemia, rash, diarrhea — listed to contrast with CNS-optimized options |

PI3K/mTOR **class toxicity signature** to expect across these: on-target **hyperglycemia** (PI3Kα), **stomatitis/mucositis**, **rash**, **fatigue**, **diarrhea**, **transaminitis**; mTOR adds **pneumonitis** and metabolic (hyperlipidemia) effects; buparlisib adds **neuropsychiatric** effects.

For this case specifically, **paxalisib remains the best-balanced brain-penetrant PI3K/mTOR backbone**; bimiralisib (CNS-by-design) and sapanisertib (mTORC1/2, bypasses AKT feedback) are the closest alternatives, and a PI3Kα-mutant-selective agent (matched to PIK3CA H1047R) is attractive for tolerability **if CNS exposure can be confirmed**.

## Combination regimens (brain-penetrant, mechanism-matched to this variant set)

Single-agent targeted therapy in DHG/pHGG almost uniformly fails to adaptive resistance and pathway feedback; the literature points to rational **combinations**. Ranked by strength of DHG-H3G34-specific evidence.

| Combination | Pathway rationale (this case) | Brain penetrance | Evidence | Overlapping toxicity / caution |
|---|---|---|---|---|
| **Niraparib + topotecan** (or **talazoparib + irinotecan/SN-38**) | DDR/ALT: H3G34R+ATRX-loss drives ALT → basal replication-stress → PARPi+TopoI **synergy**; absent p53/p21 response amplifies it | Niraparib brain-penetrant (topotecan/irinotecan less so but blood–tumor barrier leaky) | **Strongest** — DHG-H3G34R_ATRX models hypersensitive *and* a treated patient had significant tumor reduction (Voon/Schreck 2025, PMC11889718) | **Myelosuppression** (thrombocytopenia/neutropenia) is additive — main dose-limiter; **confirm ALT/ATRX first** (ATRX not detected in this CSF) |
| **Paxalisib + MEK inhibitor** (trametinib or brain-penetrant mirdametinib) | Vertical+parallel block of the convergent node: PIK3CA H1047R (PI3K) + PTPN11 S502P/RTK gains (MAPK); PDGFRA Y288C signals through PI3K+MEK (Ip 2018) | Both arms brain-penetrant (paxalisib purpose-built; mirdametinib CNS-optimized) | DIPG/pHGG MAPK-combination rationale (Mackay 2020, PMC7612484); PI3K/mTOR genetic dependency (JCI 2024, PMID 38319732) | Additive **rash, stomatitis, hyperglycemia, fatigue, diarrhea**; MEKi adds retinopathy/↓EF — needs cardiac/ophthalmic monitoring |
| **Paxalisib + metformin (± enzastaurin) + radiotherapy** | Manages the two main paxalisib **resistance/AE** drivers: insulin-feedback hyperglycemia (metformin) and adaptive calcium-PKC signaling (enzastaurin, brain-penetrant); RT backbone | All CNS-active | Survival benefit in orthotopic DIPG models; clinically translatable design (JCI 2024, PMID 38319732) | Generally tolerable; watch hyperglycemia, GI; enzastaurin QTc |
| **PARP inhibitor + temozolomide ± radiotherapy** | DDR: PARPi potentiates TMZ/RT DNA damage; rational where MGMT methylated (frequent in G34) | Niraparib/veliparib penetrant; pamiparib also CNS | Pediatric HGG: veliparib+RT+TMZ tolerable (COG ACNS1721, NCT03581292) — **did not beat historical controls**; olaparib radiosensitizes pHGG lines | **Myelosuppression** additive with TMZ — main limiter; efficacy bar not yet cleared |
| **PARP inhibitor + radiotherapy** | DDR radiosensitization in the ALT/replication-stress context | Niraparib brain-penetrant | Niraparib phase 0/2 'trigger' design pairs niraparib + fractionated RT (NCT05076513) | Thrombocytopenia; radiation-field marrow effects |
| **RTK inhibitor + PI3K/mTOR** (e.g., avapritinib + paxalisib) | If a PDGFRA-amplified (not just Y288C) subclone dominates, pair upstream RTK block with downstream PI3K/mTOR to blunt feedback reactivation | Both brain-penetrant | Mechanistic (RTK→PI3K convergence); avapritinib CNS-active in PDGFRA-altered HGG (Cancer Cell 2025) | Additive fatigue/edema/cytopenias; avapritinib intracranial-hemorrhage risk; Y288C-specific TKI resistance caveat |
| *(deprioritized)* PI3Kα-selective + CDK4/6 | RLY-2608 trial pairs with CDK4/6i | mixed | NCT05216432 design | **RB1 loss → CDK4/6i resistance** here; PI3Kα-selective CNS exposure unproven |

**Backbone for all:** maximal safe resection + focal radiotherapy ± temozolomide (confirm MGMT). Immunotherapy combinations are unsupported by TMB-low/MSS status.

## Practical synthesis

1. **Highest-conviction, brain-penetrant, mechanism-matched picks:** PARP-based DDR targeting (niraparib, ideally with a topoisomerase-I inhibitor) **if ALT/ATRX is confirmed**, and a brain-penetrant PI3K/mTOR inhibitor (paxalisib) covering the PIK3CA-H1047R + multi-RTK convergence onto PI3K. These two have both the best CNS exposure and the clearest DHG-H3G34 rationale.
2. **Allele-aware RTK targeting:** EGFR (BDTX-1535) and MET (capmatinib/vebreltinib) are brain-penetrant and report-matched, but the alterations here are copy gains rather than activating mutations/fusions, so expected yield is lower. For PDGFRA, avapritinib is brain-penetrant and active in PDGFRA-altered HGG, **but the specific extracellular Y288C neomorph is predicted TKI-resistant** — downstream PI3K/mTOR + MEK blockade is the more mechanistically sound route for that subclone.
3. **Combination logic over RTK monotherapy:** because PDGFRA/EGFR/MET/PIK3CA all funnel into PI3K and MAPK, a downstream node (PI3K/mTOR ± MEK such as mirdametinib) plausibly covers more of the subclonal RTK heterogeneity than any single upstream RTK inhibitor.
4. **Explicit deprioritizations:** MDM2/MDM4 inhibitors (need wild-type p53; defeated by clonal TP53 R273C) and CDK4/6 inhibitors (RB1 loss → resistance), despite some having good brain penetrance and report trial matches. Checkpoint-inhibitor monotherapy is unsupported by TMB-low/MSS status.
5. **Confirm before acting:** ATRX/ALT status (drives the PARP rationale), MGMT methylation (TMZ benefit), and germline TP53 (Li-Fraumeni) all materially change the plan and are not resolved by this single CSF ctDNA draw.

## References (added to index.tsv)

Paxalisib brain-penetrance/GBM (Xenobiotica 2024; NCT03522298); niraparib BBB superiority (PMC12480552) and GBM phase 0 'trigger' trial (NCT05076513); BDTX-1535/silevertinib GBM CNS trials (NCT06072586/NCT05256290); navtemadlin limited CNS PK (PMID 40591434) and rGBM window trial (PMID 39970230); brigimadlin GBM phase 0/1a (NCT05376800); capmatinib MET-fusion pHGG (Mol Cancer 2024, 10.1186/s12943-024-02027-6); type-Ib MET inhibitor CNS (Sci Rep 2025, 10.1038/s41598-025-85631-w); mirdametinib brain-penetrant MEK (SJ901, NCT04923126); CDK4/6i CNS PBPK (PMC7854954) and ribociclib rGBM PK (PMC6863163); RLY-2608 (PMC10850943) and STX-478 (PMC11134204) mutant-selective PI3Kα; avapritinib in PDGFRA-altered HGG (Cancer Cell 2025, 10.1016/j.ccell.2025.02.018).
