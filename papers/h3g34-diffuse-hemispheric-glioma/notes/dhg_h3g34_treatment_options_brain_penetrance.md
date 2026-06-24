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

## Practical synthesis

1. **Highest-conviction, brain-penetrant, mechanism-matched picks:** PARP-based DDR targeting (niraparib, ideally with a topoisomerase-I inhibitor) **if ALT/ATRX is confirmed**, and a brain-penetrant PI3K/mTOR inhibitor (paxalisib) covering the PIK3CA-H1047R + multi-RTK convergence onto PI3K. These two have both the best CNS exposure and the clearest DHG-H3G34 rationale.
2. **Allele-aware RTK targeting:** EGFR (BDTX-1535) and MET (capmatinib/vebreltinib) are brain-penetrant and report-matched, but the alterations here are copy gains rather than activating mutations/fusions, so expected yield is lower. For PDGFRA, avapritinib is brain-penetrant and active in PDGFRA-altered HGG, **but the specific extracellular Y288C neomorph is predicted TKI-resistant** — downstream PI3K/mTOR + MEK blockade is the more mechanistically sound route for that subclone.
3. **Combination logic over RTK monotherapy:** because PDGFRA/EGFR/MET/PIK3CA all funnel into PI3K and MAPK, a downstream node (PI3K/mTOR ± MEK such as mirdametinib) plausibly covers more of the subclonal RTK heterogeneity than any single upstream RTK inhibitor.
4. **Explicit deprioritizations:** MDM2/MDM4 inhibitors (need wild-type p53; defeated by clonal TP53 R273C) and CDK4/6 inhibitors (RB1 loss → resistance), despite some having good brain penetrance and report trial matches. Checkpoint-inhibitor monotherapy is unsupported by TMB-low/MSS status.
5. **Confirm before acting:** ATRX/ALT status (drives the PARP rationale), MGMT methylation (TMZ benefit), and germline TP53 (Li-Fraumeni) all materially change the plan and are not resolved by this single CSF ctDNA draw.

## References (added to index.tsv)

Paxalisib brain-penetrance/GBM (Xenobiotica 2024; NCT03522298); niraparib BBB superiority (PMC12480552) and GBM phase 0 'trigger' trial (NCT05076513); BDTX-1535/silevertinib GBM CNS trials (NCT06072586/NCT05256290); navtemadlin limited CNS PK (PMID 40591434) and rGBM window trial (PMID 39970230); brigimadlin GBM phase 0/1a (NCT05376800); capmatinib MET-fusion pHGG (Mol Cancer 2024, 10.1186/s12943-024-02027-6); type-Ib MET inhibitor CNS (Sci Rep 2025, 10.1038/s41598-025-85631-w); mirdametinib brain-penetrant MEK (SJ901, NCT04923126); CDK4/6i CNS PBPK (PMC7854954) and ribociclib rGBM PK (PMC6863163); RLY-2608 (PMC10850943) and STX-478 (PMC11134204) mutant-selective PI3Kα; avapritinib in PDGFRA-altered HGG (Cancer Cell 2025, 10.1016/j.ccell.2025.02.018).
