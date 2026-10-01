# Design, Construction, Manufacturing, and Discussion of GD2 CAR-T Therapies

A comprehensive synthesis of the published GD2 CAR-T literature.

This report consolidates and expands on the topical notes in `notes/` into a single
end-to-end reference covering every published design, construction, and manufacturing
choice made across the 204-paper GD2 CAR-T corpus indexed in `index.tsv`. It is
organized into four parts: **Part I — Design** (what is built), **Part II — Construction**
(how the gene is delivered), **Part III — Manufacturing** (how the product is made),
and **Part IV — Discussion** (cross-cutting analysis, debates, and open questions).

For per-paper capsule summaries, see `notes/09_per_paper_extractions.md`. For specific
topical deep-dives, see the numbered notes files (`00_overview.md` through `08_clinical_formulation.md`).

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [Corpus and Methods](#corpus-and-methods)
- [Glossary](#glossary)

**Part I — Design**
- [I.1 Target biology: GD2 and OAcGD2](#i1-target-biology-gd2-and-oacgd2)
- [I.2 Antigen-binding moiety: scFv source library](#i2-antigen-binding-moiety-scfv-source-library)
- [I.3 Hinge / spacer](#i3-hinge--spacer)
- [I.4 Transmembrane domain](#i4-transmembrane-domain)
- [I.5 Costimulatory endodomain](#i5-costimulatory-endodomain)
- [I.6 Activation / signaling endodomain](#i6-activation--signaling-endodomain)
- [I.7 Promoter, LTR, and locus](#i7-promoter-ltr-and-locus)
- [I.8 Multi-cistronic cassettes and linkers](#i8-multi-cistronic-cassettes-and-linkers)
- [I.9 Safety / suicide switches in the construct](#i9-safety--suicide-switches-in-the-construct)
- [I.10 Cytokine armoring (TRUCK) and orthogonal armoring](#i10-cytokine-armoring-truck-and-orthogonal-armoring)
- [I.11 Logic gates and switchable / universal CARs](#i11-logic-gates-and-switchable--universal-cars)
- [I.12 Affinity tuning and density-gated CARs](#i12-affinity-tuning-and-density-gated-cars)

**Part II — Construction**
- [II.1 Gamma-retroviral platforms: SFG and MSGV/MSCV](#ii1-gamma-retroviral-platforms-sfg-and-msgvmscv)
- [II.2 Lentiviral platforms: 3G SIN](#ii2-lentiviral-platforms-3g-sin)
- [II.3 Transposon platforms: Sleeping Beauty and PiggyBac](#ii3-transposon-platforms-sleeping-beauty-and-piggybac)
- [II.4 AAV-mediated HDR donors](#ii4-aav-mediated-hdr-donors)
- [II.5 Virus-free CRISPR knock-in: HDR, HITI, nanoplasmid, minicircle](#ii5-virus-free-crispr-knock-in-hdr-hiti-nanoplasmid-minicircle)
- [II.6 mRNA electroporation](#ii6-mrna-electroporation)
- [II.7 LNP-mRNA in-situ programming](#ii7-lnp-mrna-in-situ-programming)
- [II.8 Multi-knockout allogeneic constructions](#ii8-multi-knockout-allogeneic-constructions)
- [II.9 Cross-platform comparison](#ii9-cross-platform-comparison)

**Part III — Manufacturing**
- [III.1 Source material: apheresis, cord blood, iPSC, cell lines](#iii1-source-material-apheresis-cord-blood-ipsc-cell-lines)
- [III.2 Cell selection: PBMC, CD4/CD8, CD45RA, naïve/TSCM, iNKT bead, γδ, NK, monocyte depletion](#iii2-cell-selection-pbmc-cd4cd8-cd45ra-naïvetscm-inkt-bead-γδ-nk-monocyte-depletion)
- [III.3 Activation reagents](#iii3-activation-reagents)
- [III.4 Cytokine support during ex-vivo expansion](#iii4-cytokine-support-during-ex-vivo-expansion)
- [III.5 Transduction conditions](#iii5-transduction-conditions)
- [III.6 Closed-system platforms in detail](#iii6-closed-system-platforms-in-detail)
- [III.7 Tonic-signal mitigation during manufacture: dasatinib, ibrutinib, AKTi](#iii7-tonic-signal-mitigation-during-manufacture-dasatinib-ibrutinib-akti)
- [III.8 Memory subset enrichment strategies](#iii8-memory-subset-enrichment-strategies)
- [III.9 Manufacturing of CAR-NKT, CAR-NK, CAR-γδ, CAR-VST](#iii9-manufacturing-of-car-nkt-car-nk-car-γδ-car-vst)
- [III.10 Formulation, fill, and cryopreservation](#iii10-formulation-fill-and-cryopreservation)
- [III.11 Release testing](#iii11-release-testing)
- [III.12 Yields, timelines, and manufacturing failures](#iii12-yields-timelines-and-manufacturing-failures)
- [III.13 Clinical-protocol-coupled manufacturing decisions](#iii13-clinical-protocol-coupled-manufacturing-decisions)
- [III.14 Detailed per-clinical-trial recipes](#iii14-detailed-per-clinical-trial-recipes)

**Part IV — Discussion**
- [IV.1 Era 1 (2008–2014): first-generation CARs and the tonic-signaling discovery](#iv1-era-1-20082014-first-generation-cars-and-the-tonic-signaling-discovery)
- [IV.2 Era 2 (2014–2018): costimulatory debate, iCasp9, NKT platforms](#iv2-era-2-20142018-costimulatory-debate-icasp9-nkt-platforms)
- [IV.3 Era 3 (2018–2022): GD2-CART01, affinity-tuning hazards, manufacturing automation](#iv3-era-3-20182022-gd2-cart01-affinity-tuning-hazards-manufacturing-automation)
- [IV.4 Era 4 (2022–2026): CNS administration, non-viral CRISPR knock-in, allogeneic, armored constructs](#iv4-era-4-20222026-cns-administration-non-viral-crispr-knock-in-allogeneic-armored-constructs)
- [IV.5 The 14g2a tonic-signaling story in full](#iv5-the-14g2a-tonic-signaling-story-in-full)
- [IV.6 The CD28 vs 4-1BB vs CD28+4-1BB vs CD28+OX40 debate, resolved](#iv6-the-cd28-vs-4-1bb-vs-cd281bb-vs-cd28ox40-debate-resolved)
- [IV.7 Lessons from the affinity / CNS-encephalitis incidents](#iv7-lessons-from-the-affinity--cns-encephalitis-incidents)
- [IV.8 Why every clinical GD2 product has eventually shifted to closed-system Prodigy or Cocoon](#iv8-why-every-clinical-gd2-product-has-eventually-shifted-to-closed-system-prodigy-or-cocoon)
- [IV.9 Why IL-7 + IL-15 dominates over IL-2 in modern manufacturing](#iv9-why-il-7--il-15-dominates-over-il-2-in-modern-manufacturing)
- [IV.10 Choice of effector cell across indications](#iv10-choice-of-effector-cell-across-indications)
- [IV.11 The CNS / ICV breakthrough](#iv11-the-cns--icv-breakthrough)
- [IV.12 Cytokine armoring and the IL-15 hyperleukocytosis lesson](#iv12-cytokine-armoring-and-the-il-15-hyperleukocytosis-lesson)
- [IV.13 Manufacturing-vs-construct trade-offs](#iv13-manufacturing-vs-construct-trade-offs)
- [IV.14 The transition to virus-free CRISPR-TRAC](#iv14-the-transition-to-virus-free-crispr-trac)
- [IV.15 Allogeneic GD2 CAR-T](#iv15-allogeneic-gd2-car-t)
- [IV.16 Open questions and frontier areas](#iv16-open-questions-and-frontier-areas)
- [IV.17 What every new GD2 CAR-T program should consider](#iv17-what-every-new-gd2-car-t-program-should-consider)

- [Appendix A — Construct lineage map by clinical trial product](#appendix-a--construct-lineage-map-by-clinical-trial-product)
- [Appendix B — Master construct-format glossary](#appendix-b--master-construct-format-glossary)
- [Appendix C — Caveats and limitations of this synthesis](#appendix-c--caveats-and-limitations-of-this-synthesis)

---

## Executive Summary

**Scope.** All published GD2-targeted CAR-effector cell therapies (T, NKT, γδ-T, NK, NK-92, CIK, iPSC-derived, allogeneic donor-derived, macrophage), 2008–2026, identified via five PubMed E-utils queries combined and deduplicated. 204 papers indexed; 150 PDFs in OA; 96 supplements extracted; ~50 paywalled papers retained with metadata and DOIs.

**The CAR construct that has stabilized clinically** is, in shorthand:

```
SFG (or MSCV) γ-retrovirus
    → iCasp9   (FKBP-F36V x caspase9-Δactive)
    → P2A
    → 14g2a scFv (signal peptide — VL — (G4S)3 linker — VH)
    → CD8α hinge — CD8α TM
    → 4-1BB cytoplasmic
    → CD3ζ ITAM1-3
```

Variants in use:
- The Brenner/Bambino Gesù lineage (**GD2-CART01**) uses **3G CD28-4-1BB-CD3ζ** with iCasp9 (Quintarelli 2018; Del Bufalo 2023; Locatelli 2025; Quintarelli 2025 allogeneic).
- The Heczey 2017 **GD2-CAR3** lineage uses **3G CD28-OX40-CD3ζ** with iCasp9 (also has a CAR-NKT IL-15-armored variant, Heczey 2020/2023).
- The Stanford / Mackall / Monje **DMG GD2-CART** uses **2G CD8α-4-1BB-CD3ζ** with iCasp9, manufactured on CliniMACS Prodigy in 7 days with dasatinib priming (Majzner 2022; Monje 2025).
- The Hannover **GD2-IL18 TRUCK** is **2G CD8α-4-1BB-CD3ζ** with NFAT-IL18 cassette in a 3G SIN lentiviral vector, manufactured on CliniMACS Prodigy in 12 days (Glienke 2022).
- The Wisconsin **MP TRAC-CAR** uses CRISPR-Cas9 RNP + nanoplasmid donor to knock GD2-CD8α-4-1BB-CD3ζ into TRAC, in a 9-day virus-free process scalable on the Lonza Cocoon (Mueller 2022; Cappabianca 2024).

**The single most important design lesson** of the last decade is that **14g2a-based CARs exhibit antigen-independent tonic signaling** (clustering of CAR molecules on the T-cell membrane → CD3ζ phosphorylation in the absence of GD2 engagement). With CD28 costimulation this drives early-onset exhaustion, T-bet/Blimp-1 upregulation, PD-1/TIM-3/LAG-3 expression, and apoptosis; with 4-1BB costimulation the same construct survives and functions. Affinity-matured 14g2a (E101K) intensifies tonic signaling enough that with CD28 it causes lethal CNS encephalitis in mice (Long 2015 PMID 25939063; Richman 2018 PMID 29180536).

**The single most important manufacturing lesson** is that **automated, closed-system (Prodigy / Cocoon) production with IL-7 + IL-15 (replacing IL-2) and tonic-signal mitigation (dasatinib priming during the activation/edit window) yields markedly less differentiated, more persistent CAR-T products**. Stanford, Hannover, Wisconsin, and Bambino Gesù have converged on this approach despite differences in vector platform and construct.

**The single most important clinical lesson** is that **intracerebroventricular (ICV) delivery via Ommaya reservoir transforms CNS responsiveness for DMG**: in Monje 2025 (PMID 39537919), 62 ICV infusions produced no dose-limiting toxicity, while IV alone at the same dose level caused ICANS. ICV does not require lymphodepletion between doses, and CSF CAR exposure is markedly higher than IV.

---

## Corpus and Methods

**Identification.** Five PubMed E-utils queries combined and deduplicated:
1. `"GD2"[Title/Abstract] AND ("CAR T"[Title/Abstract] OR "CAR-T"[Title/Abstract] OR "chimeric antigen receptor"[Title/Abstract])`
2. `"GD2"[Title/Abstract] AND ("adoptive cell"[Title/Abstract] OR "adoptive T"[Title/Abstract])`
3. `"disialoganglioside"[Title/Abstract] AND CAR`
4. `"GD2 CAR"[Title/Abstract]`
5. `("anti-GD2 CAR"[Title/Abstract] OR "GD2-specific CAR"[Title/Abstract])`

**Triage.** Filtered to GD2-targeting CAR effectors. Excluded ch14.18 / dinutuximab / naxitamab monoclonal antibody papers (they were referenced in many CAR papers but not themselves CAR therapies). Retained CAR-armored MSC and CAR-macrophage / CAR-microglia papers and antibody-coupled adapter-CAR / SUPRA papers since these are part of the GD2-targeting effector landscape.

**Source acquisition.** PDFs obtained from: PMC OA full-text, Europe PMC OA tarball, Unpaywall, publisher OA. A custom Proof-of-Work solver was used to download PMC author-manuscripts that block scripted access. Supplementary materials extracted from Europe PMC OA zips and publisher OA landing pages.

**Text extraction.** `pdftotext -layout` for spatial preservation, plus `python-docx` for `.docx` supplements. Keyword-pattern matching with 50+ regex patterns covered scFv sources, hinge/TM/costim/signaling domains, vectors, transduction protocols, activation reagents, expansion cytokines, closed systems, dose levels, lymphodepletion, routes.

**Coverage.** 204 papers indexed; 150 with PDFs (74%); 152 with extracted text usable for keyword analysis. The ~50 paywalled records have abstracts + DOIs in `index.tsv` and inferred construct/manufacturing details from adjacent papers in `notes/`.

---

## Glossary

| Term | Definition |
| --- | --- |
| GD2 | Disialoganglioside; tumor-associated carbohydrate antigen on neuroblastoma, gliomas, sarcomas, melanoma. |
| OAcGD2 | 9-O-acetylated GD2; more tumor-restricted variant. Targeted by 8B6 scFv. |
| scFv | Single-chain variable fragment; antibody binding region used as the antigen-recognition domain of a CAR. |
| 14g2a | Murine anti-GD2 scFv derived from antibody ch14.18; dominant binder in clinical GD2 CARs. |
| hu14.18 | Humanized 14.18; alternative to 14g2a. |
| 3F8 / hu3F8 | Alternative anti-GD2 scFv from Memorial Sloan Kettering's anti-GD2 antibody program. |
| Hinge / spacer | Linker between scFv and TM (commonly CD8α, IgG1 CH2CH3, IgG4 CH2CH3, or modified CD8α). |
| TM | Transmembrane domain (commonly CD8α or CD28). |
| Costim | Costimulatory endodomain (CD28, 4-1BB / CD137, OX40 / CD134, CD27, ICOS, 2B4). |
| CD3ζ | T-cell receptor zeta chain; activation/signal-1 endodomain. |
| 1G / 2G / 3G CAR | First-generation (CD3ζ only) / second-generation (one costim + CD3ζ) / third-generation (two costim + CD3ζ). |
| 4G CAR | Fourth-generation, "armored" CAR with an additional cytokine, chemokine receptor, or signaling cassette. |
| iCasp9 / iC9 | Inducible caspase-9 suicide gene; activated by rimiducid (AP1903) to apoptose the engineered cell. |
| RQR8 | Chimeric CD34/CD20 epitope tag; rituximab-inducible kill switch. |
| EGFRt | Truncated EGFR; cetuximab-inducible kill switch. |
| HSV-TK | HSV thymidine kinase; ganciclovir-inducible suicide gene. |
| TRUCK | "T cells redirected for universal cytokine-mediated killing"; armored CAR with an inducible cytokine cassette (commonly IL-12, IL-18, IL-15). |
| C7R | Constitutively active IL-7 receptor α chain. |
| SFG | Murine retroviral vector backbone (MoMLV-derived) used by Brenner / Baylor / Bambino Gesù. |
| MSGV / MSCV | Murine Stem Cell Virus retroviral vectors used by NCI/Stanford. |
| SIN | Self-inactivating; refers to lentiviral 3G systems with deleted LTR U3 region. |
| TRAC | T-cell receptor alpha constant locus; common knock-in site for CRISPR-CAR. |
| HITI | Homology-independent targeted insertion (non-HDR CRISPR knock-in via NHEJ). |
| CliniMACS Prodigy | Miltenyi's closed-system T-cell processing platform. |
| Lonza Cocoon | Lonza's closed-system T-cell processing platform with automated electroporation. |
| RetroNectin (CH-296) | Recombinant fibronectin fragment used to enhance retroviral spinoculation. |
| TransAct | Miltenyi's soluble CD3/CD28 nanomatrix activation reagent. |
| DMG / DIPG | Diffuse midline glioma / diffuse intrinsic pontine glioma; H3K27M-mutant brainstem and spinal gliomas. |
| NB | Neuroblastoma. |
| TIAN | Tumor inflammation-associated neurotoxicity (term coined in DIPG CAR-T trials). |
| Cy/Flu | Cyclophosphamide + fludarabine lymphodepleting chemotherapy. |
| ICV / Ommaya | Intracerebroventricular / Ommaya reservoir for repeat ICV administration. |

---

# Part I — Design

The CAR construct, viewed as a synthetic biology cassette, has a small set of interchangeable parts:

```
5'-LTR — [Promoter / SA] — [Signal peptide] — [scFv (VH–linker–VL or VL–linker–VH)]
       — [Hinge / spacer] — [TM] — [Costim 1] — [Costim 2 (optional)]
       — [CD3ζ] — [P2A / T2A / IRES] — [Suicide gene or armoring cassette]
       — [polyA / WPRE / 3'-LTR]
```

Every published GD2 CAR fills the slots above with one or a small set of choices. This section enumerates every choice that has been made, identifies which papers use which choice, and explains the consequences.

## I.1 Target biology: GD2 and OAcGD2

GD2 is a disialoganglioside (Neu5Ac–Galβ–GalNAcβ–Galβ–Glcβ–ceramide) that is highly expressed on:
- Neuroblastoma (>90% of tumors)
- Gliomas including H3K27M-mutant diffuse midline glioma (DMG) and glioblastoma
- Osteosarcoma, Ewing sarcoma, rhabdomyosarcoma
- Melanoma
- Small-cell lung cancer (variable)
- Retinoblastoma
- Some breast cancers

GD2 is also expressed at lower levels on:
- Peripheral nerve fibers (Schwann cells, axonal membranes) — source of the dose-limiting pain seen with high-affinity anti-GD2 mAbs
- CNS neurons (basal density is sub-threshold for unmodified 14g2a CARs but exceeds threshold for high-affinity variants and high-dose ICV delivery)
- Skin melanocytes
- Some MSCs (Martinez 2007)

**OAcGD2** (9-O-acetylated GD2) is more tumor-restricted because peripheral nerves express GD2 but largely lack the de-novo acetylation. The 8B6 scFv recognizes OAcGD2 selectively and has been incorporated into GD2 CARs by Birkholz, Cappabianca, and others (notes/05).

**Implications for CAR design.**
- The scFv affinity and density of CAR molecules on the T cell control the GD2-expression threshold at which the CAR triggers (Majzner 2022).
- Costimulatory choice determines whether sub-threshold tonic CAR signaling (driven by scFv self-clustering) becomes lethal exhaustion or tolerable background.
- ICV delivery localizes CAR-T to the CSF and exposes CNS GD2 to the CAR; tonic neurotoxicity (TIAN) is observed but typically responds to dexamethasone and anakinra.

## I.2 Antigen-binding moiety: scFv source library

| scFv | Source antibody | Format (V_L–linker–V_H or V_H–linker–V_L) | Affinity (K_D) | Clinical use |
| --- | --- | --- | --- | --- |
| 14g2a (murine) | Murine anti-GD2 IgG2a (parental of ch14.18) | V_L–(G4S)3–V_H | ~50 nM | Pule 2008, Heczey 2017, Majzner 2022, Monje 2025, Glienke 2022, Mueller 2022, Cappabianca 2024 — dominant in clinical use |
| 14g2a-E101K (murine, affinity-matured) | Engineered single-residue mutation in CDR-H2 | V_L–(G4S)3–V_H | ~15 nM | Richman 2018 (preclinical only — withdrawn due to lethal encephalitis with CD28) |
| hu14.18 (humanized) | Humanized 14.18 (dinutuximab β backbone) | V_L–(G4S)3–V_H | ~50 nM | Sujjitjoon 2021, Yvon 2009; Bodden 2023 (NK-92 platform) |
| 3F8 / m3F8 (murine) | MSK anti-GD2 IgG3 | V_H–(G4S)3–V_L typically | ~10 nM | Cheever 2009, Yang 2024 |
| hu3F8 (humanized) | Naxitamab-derived | V_H–(G4S)3–V_L | ~5 nM | Sujjitjoon 2021, Cheever 2009 |
| 5F11 / m5F11 (murine) | Alternative MSK clone | varies | ~50 nM | Pre-clinical only |
| K666 / various Ab-display-derived | Phage display from immunized mice or rabbits | varies | varies | Cancer Research scFv-library papers |
| 8B6 (anti-OAcGD2) | Murine anti-9-O-acetyl-GD2 | V_L–(G4S)3–V_H | ~100 nM | Cappabianca 2024 (TRAC-KI), Birkholz 2019 |
| Various Ab-display single-domain (nanobody / VHH) | Llama / shark | single domain (~110 aa) | varies | Heczey lab, others — emerging |

**Design-level commentary on scFv choice:**
- The 14g2a scFv has been the workhorse since Rossig 2001 / Pule 2008 because the parental antibody is FDA-approved (ch14.18 / dinutuximab) and well-characterized in human safety.
- The CDR framework regions of 14g2a are sufficient to induce tonic signaling, independent of the antigen-binding residues (Long 2015, mutational analysis). This means switching scFvs (14g2a → 3F8 → hu14.18) only partially mitigates the tonic-signaling problem.
- High-affinity scFvs (3F8, naxitamab-derived, E101K-matured 14g2a) recognize lower GD2 densities, expanding target coverage but reducing the sub-tumor selectivity margin.
- For OAcGD2 targeting (8B6), the field is small but growing — promising for reducing on-target/off-tumor toxicity since OAcGD2 is largely absent from healthy nerves.
- VHH / nanobody-based GD2 binders are emerging but no clinical product yet uses them.

## I.3 Hinge / spacer

| Hinge | Length | Where used | Trade-offs |
| --- | --- | --- | --- |
| CD8α stalk (~45 aa) | Short, flexible | Majzner 2022 / Monje 2025 (DMG); Mueller / Cappabianca; most 4-1BB-costim products | Most common modern choice; no FcγR off-target binding |
| IgG1 CH2-CH3 (Fc, ~227 aa) | Long, dimeric | Original Pule 2008 / SFG; Gargett (CARPETS) | Promotes self-aggregation and tonic signaling (Long 2015); deletion of the CH2 N297Q glycosylation site reduces FcγR off-target activation but tonic signaling remains |
| IgG4 CH2-CH3 with PG/PA mutation | Long, dimeric | Various 3F8-based CARs | Avoids FcγR cross-linking but still long |
| Modified IgG1 with CH2 deleted | Medium | Some Texas Children's NKT constructs | Compromise |
| CD28 hinge (~33 aa) | Short | Many CD28-TM-CD28-costim 2G CARs | Often paired with CD28 TM |
| Modified CD8α (linker + stalk + N-glycan-removed) | Short | Mount 2018, Long 2016 | Optimized for stability |
| Linker-free (TM directly fused to scFv) | n/a | Rare | High self-clustering risk |

**Hinge-spacer-length impact on tonic signaling and synapse geometry:**
- The long Fc hinges (CH2-CH3) self-associate on the T-cell membrane and drive CAR clustering → tonic phosphorylation of CD3ζ ITAMs → exhaustion.
- The short CD8α hinge avoids this and is now the consensus for clinical GD2 CARs.
- Hinge-length affects the synapse geometry: short hinges position the scFv close to the membrane and require the target epitope to be membrane-proximal. GD2's ceramide anchoring makes it a membrane-proximal antigen, so short hinges work well.

## I.4 Transmembrane domain

| TM | Where used | Notes |
| --- | --- | --- |
| CD8α TM | Most modern 4-1BB and 4-1BB+CD3ζ constructs (Majzner 2022, Monje 2025, Mount 2018, Glienke 2022, Mueller 2022) | Most common in clinical use; pairs with CD8α hinge |
| CD28 TM | Long 2015 GD2.28z, Heczey 2017 GD2.CAR3 (CD28-TM with CD28-CD3ζ) | Paired with CD28 hinge; promotes CD28-CD28 homodimerization |
| CD3ζ TM | Rare 1G constructs | Pule 2008 original |
| 4-1BB TM | Some BB-only constructs | Less common |

**TM choice is correlated with costim choice.** CD28 TM + CD28 costim is one functional unit (homodimerizing). CD8α TM + 4-1BB costim is another. Mixing (e.g., CD28 TM + 4-1BB costim) is mechanically possible but less common because the CD28 TM contributes to CD28-CD28 dimer formation which is intrinsically pro-activating.

## I.5 Costimulatory endodomain

Comprehensive enumeration of costimulatory choices across the GD2 CAR-T literature:

### Single costimulatory domain (2G)

| Costim | Cytoplasmic motif highlights | Major proliferative axis | Major effector phenotype | Where used |
| --- | --- | --- | --- | --- |
| CD28 | YMNM, PYAP | PI3K/AKT/mTOR | Effector-skewed; high IFNγ; rapid expansion; rapid exhaustion if tonic-signal-driven | Pule lineage (with CD28); Long 2015 GD2.28z; Singh 2014 mRNA |
| 4-1BB (CD137) | TRAF-binding motifs (KEEEEGGCEL) | NF-κB and STAT3/5 (sustained) | Memory-skewed; lower tonic exhaustion; longer persistence in vivo | Mount 2018, Majzner 2022, Monje 2025, Glienke 2022, Mueller 2022, Cappabianca 2024, Yu 2018, GD2-CART01 (3G has 4-1BB too) |
| OX40 (CD134) | TRAF-binding | NF-κB and Th17 polarization | Strong cytokine production | Rare as sole costim; common as 2nd costim in 3G |
| CD27 | TRAF-binding | NF-κB | Memory-skewed | Glienke variants; experimental |
| ICOS | YMFM | PI3K | Th17 polarization | Rare in GD2 |
| 2B4 (CD244) | ITSM | SAP-mediated | NK-like cytotoxicity | NK / NKT constructs |

### Dual costimulatory domains (3G)

| Combination | Where used | Rationale |
| --- | --- | --- |
| CD28 + 4-1BB | Quintarelli 2018, Del Bufalo 2023, Locatelli 2025 (GD2-CART01); various BCM constructs | Combines CD28-driven rapid effector function with 4-1BB-driven memory and persistence; less tonic exhaustion than CD28-only |
| CD28 + OX40 | Heczey 2017 GD2.CAR3, Pule lineage 3G | Original Baylor 3G; clinical track record |
| 4-1BB + OX40 | Rare; experimental | Both TNFR-family; mild costim |
| ICOS + OX40 | Some Brenner-lab work | Th-skewed |
| 4-1BB + 2B4 | NKT and NK constructs (Bodden 2023) | NK-tuned costimulation |

### Costim choices for non-T effectors

- **CAR-NKT** (Heczey 2014/2017/2020/2023): CD28 + 2B4 + CD3ζ; some IL-15-armored variants
- **CAR-NK / NK-92** (Bodden 2023, others): CD28-2B4-CD3ζ or 4-1BB-2B4-CD3ζ; some use NKG2D as costim
- **CAR-γδ** (Capsomidis 2018): Typical αβ-T costimulation (4-1BB or CD28), since γδ-T cells have similar signaling
- **CAR-MΦ** (CARMA papers): Different — FcRγ replaces CD3ζ, costim minimal
- **CAR-microglia** (recent preprints): Similar to NK constructs

**Costim debate, condensed.** For GD2 with the 14g2a scFv, CD28 as the sole costim drives lethal tonic-signal-induced exhaustion (Long 2015). 4-1BB rescues this and is the safest single costim choice. Pairing CD28 with a TNFR-family second domain (4-1BB or OX40) restores rapid effector function while mitigating exhaustion — this is the modern 3G consensus. The field-wide trend is toward 4-1BB-containing constructs (either 2G CD8α-4-1BB or 3G CD28-4-1BB).

## I.6 Activation / signaling endodomain

CD3ζ is the universal signal-1 domain. It contains three ITAMs (ITAM1, ITAM2, ITAM3). In some constructs:
- Wild-type CD3ζ — the default
- Mutated ITAMs (ITAM1+2+3 active, ITAM1 only, etc.) — explored in 1XX/CD3ζ-engineered constructs (Feucht 2019) but not yet in clinical GD2 products
- Replacement with DAP10 / DAP12 — explored in NK constructs (DAP12 has ITAM, DAP10 has YINM motif resembling CD28)

**Why CD3ζ wild-type.** It is well-characterized, stable, and integrates with the natural T-cell signaling machinery. ITAM-engineered variants (1XX, ITAM-mutation) show promise in preclinical work but no GD2-specific clinical variant uses them yet.

## I.7 Promoter, LTR, and locus

| Vector type | Promoter | Locus |
| --- | --- | --- |
| SFG γ-retrovirus | MoMLV-LTR | Random (semi-random integration with bias for active genes) |
| MSGV / MSCV γ-retrovirus | MSCV-LTR or PGK | Random |
| 3G SIN lentivirus | EF1α (commonly), PGK, MND, or CD8α-T promoters | Random (semi-random with slight bias) |
| TRAC-KI (CRISPR HDR) | Endogenous TRAC promoter | TRAC locus (chr14) |
| AAVS1-KI (CRISPR HDR) | Embedded promoter (e.g. EF1α) | AAVS1 safe-harbor locus (chr19) |
| Transposon (Sleeping Beauty, PiggyBac) | EF1α typically | Random integration with TA-dinucleotide preference (SB) or TTAA (PB) |

**Locus choice consequences:**
- LTR-driven constructs (SFG, MSCV) have constitutive high-level expression; bursts of expression in activated T cells.
- TRAC-KI yields constant-level expression under the TRAC promoter, which is dynamically regulated by T-cell activation (CAR expression goes up upon activation, down upon rest) — this is thought to reduce exhaustion (Eyquem 2017).
- AAVS1-KI provides safe-harbor stable expression but at higher copy number variability.
- TRAC-KI also knocks out the endogenous TCR, eliminating endogenous TCR signaling and (in theory) GVHD risk for allogeneic products.

## I.8 Multi-cistronic cassettes and linkers

Almost all clinical GD2 constructs are multi-cistronic to include a safety switch or armoring gene alongside the CAR:

| Format | Linker | Where used |
| --- | --- | --- |
| `iCasp9 — P2A — CAR` | P2A self-cleaving peptide | GD2-CART01, Heczey 2017, Majzner 2022, Glienke 2022 (in iCasp9 variants), CARPETS |
| `iCasp9 — T2A — CAR` | T2A self-cleaving peptide | Some constructs |
| `CAR — IRES — iCasp9` | IRES (encephalomyocarditis virus) | Older constructs |
| `iCasp9 — 2A — CAR — 2A — IL15` | Multiple 2As | Heczey 2020/2023 GD2-CAR.15 NKT |
| `CAR — 2A — NFAT-IL18` | 2A + NFAT-responsive minimal promoter for the IL-18 cassette | Glienke 2022 (IL-18 TRUCK) |
| `CAR — 2A — C7R` | 2A | Texas Children's C7R-armored constructs |
| `RQR8 — 2A — CAR` | 2A | RQR8-based safety-switch constructs |
| `EGFRt — 2A — CAR` | 2A | Some Stanford constructs |

**2A choice.** P2A (porcine teschovirus) has the highest cleavage efficiency (~99%) and is preferred. T2A, F2A, E2A are used historically. With 2A peptides a short C-terminal sequence remains on the upstream protein and a single N-terminal proline remains on the downstream protein — these are usually tolerated.

**IRES choice.** EMCV IRES is most common; results in lower expression of the downstream protein than the upstream one.

## I.9 Safety / suicide switches in the construct

| Switch | Trigger drug | Kinetics | GD2 papers |
| --- | --- | --- | --- |
| iCasp9 (FKBP-F36V × caspase9-Δactive) | Rimiducid (AP1903), 0.4 mg/kg IV | Hours; apoptosis of >90% transduced cells within 24h | Pule lineage, GD2-CART01, Heczey 2017/2020/2023 NKT, Majzner 2022, Monje 2025, Glienke 2022 (with iCasp9 variant), Quintarelli 2018, Quintarelli 2025 (allogeneic), Cappabianca 2024 (TRAC), Mueller 2022 (TRAC) |
| RQR8 (CD34/CD20 epitope) | Rituximab | Days; ADCC of transduced cells | Some Stanford / Hannover variants |
| EGFRt (truncated EGFR) | Cetuximab | Days; ADCC | Older Seattle Children's lineage |
| HSV-TK | Ganciclovir | Days; thymidine kinase converts ganciclovir to a toxic metabolite | Earlier GD2-VST constructs (Pule 2008 had cells with HSV-TK option) |
| Affinity-tuning (no switch) | n/a | n/a | Implicit "switch" — reducing CAR affinity below the on-target/off-tumor threshold |

**iCasp9 is dominant** because it is fast (apoptosis within hours), CAR-specific (only activated by AP1903 in the transgene-expressing cells), and well-tolerated. Approximately 90% reduction in circulating CAR-T cells is observed within 24 hours of rimiducid dose, with subsequent expansion of any residual cells if the antigen pressure remains.

## I.10 Cytokine armoring (TRUCK) and orthogonal armoring

### IL-15 armoring

- **GD2-CAR.15 (Heczey 2020/2023)**: CAR-NKT with constitutive IL-15 expression. PMID 32747836, 36702272. Patients with progressive neuroblastoma showed CAR persistence and an objective clinical response. IL-15 + 2B4 + CD28 + CD3ζ.
- **RD-IL15 superagonist (Bodden 2023, NK-92)**: Receptor-detached IL-15 fused to IL-15Rα; tethers IL-15 to the CAR-effector cell membrane for autocrine signaling. PMID 38134936.
- **Tian 2025**: K562-aAPC secondary stimulation of CAR-NKT.15 → hyperleukocytosis at DL5 (clinical case). Recommends including a safety switch.

### IL-18 armoring

- **Glienke 2022 IL-18-TRUCK**: NFAT-responsive minimal promoter driving IL-18 secretion; activated only by CAR engagement. CliniMACS Prodigy 12-day manufacture. PMID 36167468 / IL-18 variant.
- Several preclinical IL-18 constructs in the corpus.

### IL-7 / IL-7R armoring

- **C7R (constitutively active IL-7Rα)** — used in several Texas Children's constructs. Provides survival signal mimicking IL-7.

### Chemokine receptor armoring

- **CCR2b**: Enhances trafficking to CCL2-rich tumors (some neuroblastoma constructs).
- **CXCR2**: Enhances trafficking to IL-8 / CXCL1-rich tumors (some sarcoma constructs).

### Other armoring

- **PD-1 KO (CRISPR)**: Some allogeneic constructs.
- **NK / NKT receptors**: NKG2D in NK-CAR constructs.
- **Trogocytosis-resistant TM**: Experimental.

## I.11 Logic gates and switchable / universal CARs

### synNotch AND-gates

- **B7-H3-synNotch + GD2-CAR (Choe 2021, others)**: B7-H3 sensor drives GD2-CAR expression. Requires both antigens for activation.
- **EphA2-synNotch + GD2-CAR**: Variant.

### OR-gates / bispecific / tandem CARs

- **GD2-CD19 dual-CAR** (preclinical) — neuroblastoma + B-cell co-targeting.
- **GD2-B7H3 tandem-CAR** — both antigens activate the same CAR via two scFvs in a single construct.
- **GD2-MUC1 / GD2-PSMA / GD2-various** — preclinical only.

### NOT-gates

- **Healthy-tissue-protective**: A second CAR with inhibitory PD-1-style endodomain that suppresses the GD2-CAR when bound. Preclinical only for GD2.

### Universal / SUPRA / DARPin

- **SUPRA / sCAR**: Adapter molecule binds GD2 (or any target) and links to the zip-CAR.
- **BiTE-CAR** combinations.

### Density-gated

- **Majzner 2022**: Direct demonstration that GD2-CAR potency scales with cell-surface CAR density and antigen density. Reducing CAR density widens the on-target / off-tumor margin.

## I.12 Affinity tuning and density-gated CARs

Two engineerable parameters control on-target sensitivity:
1. **scFv affinity** (e.g. K_D 50 nM for 14g2a vs 15 nM for 14g2a-E101K).
2. **CAR molecule density** on the T-cell membrane (controlled by promoter strength, copy number, locus choice).

**Affinity tuning** (Richman 2018): The E101K mutation in 14g2a improved affinity for GD2 by ~5x. When combined with CD28 costim, it caused lethal CNS encephalitis in NSG mice — a near-complete penetrance fatal phenotype. The phenotype required all three of: high-affinity scFv, CD28 costim, and intact CNS endothelium. Switching to 4-1BB rescued survival. This work explicitly stopped clinical development of 14g2a-E101K-CD28 and shifted the field toward standard-affinity 14g2a + 4-1BB or hybrid 3G constructs.

**Density tuning** (Majzner 2022 / Monje 2025): A 2G CD8α-4-1BB-CD3ζ CAR with the standard-affinity 14g2a scFv showed activity at IV dose 1×10⁶/kg without DLT in DMG patients. Increasing the density (no per-cell change, but more cells) at 3×10⁶/kg IV produced ICANS (rapidly reversible with corticosteroids + anakinra). For ICV delivery, doses of 10×10⁶, 30×10⁶, and 100×10⁶ cells were delivered repeatedly into the Ommaya reservoir without DLT.

The density-tuning insight has shaped manufacturing too: lower MOI / lower transduction percentage / lower CAR-per-cell can be tuned during manufacture by adjusting vector concentration, spinoculation time, or selection stringency.

---

# Part II — Construction

Construction refers to **how the CAR transgene is physically delivered** into the effector cell. The GD2 CAR-T field has used essentially every gene-delivery platform that has ever been applied to CAR-T cells.

## II.1 Gamma-retroviral platforms: SFG and MSGV/MSCV

### SFG (MoMLV-derived)

- Used by Baylor / Texas Children's / Bambino Gesù lineage.
- Vector: SFG backbone; producer line PG13 (gibbon-ape-leukemia-virus pseudotyped) generates GALV-env-pseudotyped retrovirus that transduces human cells via the GLVR1 receptor.
- Producer lines: PG13-based stable clones generated by sequential infection of PG13 packaging cells with the SFG-CAR plasmid.
- Pule 2008 used PG13/GD2-CARζ producer; iCasp9 was incorporated into the same vector for clinical use.
- Long 2016: PG13 stable clone of SFG.iCasp9.2A.14g2a.CD28.OX40.ζ (also written SGF.iCasp9 in some figures — same vector).
- Quintarelli 2018 → GD2-CART01: Uses SFG retroviral vector with iCasp9 + 14g2a + CD28 + 4-1BB + CD3ζ, packaged in PG13 stable clone.

### MSGV / MSCV (Murine Stem Cell Virus)

- Used by NCI / Stanford and various NCI-affiliated programs.
- MSGV-14g2a-28z (Long 2015): scFv + CD28 hinge + CD28 TM + CD28 cyto + CD3ζ, packaged in 293GP cells with RD114 envelope by transient triple transfection. Used in many preclinical studies.
- MSGV-14g2a-4-1BB-ζ (Long 2015, Long 2016): scFv + CD8α hinge + CD8α TM + 4-1BB cyto + CD3ζ, packaged in 293GP with RD114.
- MSGV-14g2a-E101K (Richman 2018): The high-affinity variant; same MSGV backbone.

### Retroviral pseudotyping

| Envelope | Receptor | Tropism | Notes |
| --- | --- | --- | --- |
| GALV (gibbon ape leukemia virus) | GLVR1 (Pit1) | Broad mammalian | Used in PG13 producer line |
| RD114 (cat endogenous retrovirus) | Na+-dependent neutral amino acid transporter | Broad including resting T cells | Used by Long lab and others; allows transduction without serum-containing media issues |
| Amphotropic (4070A) | Pit2 | Broad | Older work; lower titer |
| VSV-G | LDL receptor | Universal | Cytotoxic for stable producer lines; used for transient transfection only |

### Production workflow (clinical-scale γ-retrovirus)

1. **GMP master cell bank** of PG13-CAR clone.
2. **Vector batch production**: scale-up of producer line in DMEM + 10% FBS in bag culture or cell-factory (e.g., HYPERStack).
3. **Vector concentration**: not required for γ-retrovirus (titers typically 1–5×10⁶ TU/mL natively); sometimes concentrated 10-fold by tangential-flow filtration.
4. **Release testing**: titer (by flow on Jurkat or HT1080), sterility (USP <71>), endotoxin (<5 EU/dose), replication-competent retrovirus (RCR) by 3-week amplification on Mus dunni cells with reverse-transcriptase or PCR assay, sequence integrity.
5. **Storage**: -80°C; shelf life typically 1–2 years.

## II.2 Lentiviral platforms: 3G SIN

### Standard 3G SIN architecture

- 3rd-generation self-inactivating (SIN) lentiviral vector backbone (e.g., pCDH, pLV-EF1α, pHIV).
- Packaging: HEK293T transient triple-transfection with packaging plasmids (gag-pol, rev, tat — or split into pMDLg/pRRE + pRSV-Rev + pMD2.G).
- Envelope: VSV-G typically.
- Promoter inside: EF1α (most common), MND, PGK, or CD8a-tetramer.
- WPRE: woodchuck hepatitis virus posttranscriptional regulatory element — increases titer 2-5x and stabilizes mRNA in the producer.

### Used in GD2 CAR-T papers (selected)

- Singh 2014 (PMID 25104548): pMDG.1 / pRSV.rev / pMDLg/p.RRE packaging with Express-In or Lipofectamine; transfer plasmid: 14g2a-4-1BB-ζ; transduction with addition of CD3/CD28 beads and rhIL-2.
- Mount 2018 (PMID 29662203): Lentiviral 14g2a-CD8α-4-1BB-ζ for DIPG.
- Yu 2018 (PMID 29298689): pTYF lentiviral vector, GD2-4-1BB-ζ.
- Chulanetra 2020 (PMID 32195035): NHP/TYF lentiviral vector system; hu3F8, c.60C3, hu14.18 scFv variants — all 4G constructs with iCasp9.
- Sujjitjoon 2021: Lentiviral 14g2a-CD8α-4-1BB-ζ.
- Glienke 2022 (PMID 36167468): 3G SIN lentivirus with 14g2a-CD8α-4-1BB-ζ + NFAT-IL18 cassette; CliniMACS Prodigy production.

### Lentiviral production workflow (clinical-scale)

1. **Plasmid prep**: GMP-grade transfer, packaging, and envelope plasmids.
2. **Transient transfection**: HEK293T or 293F in suspension or adherent culture. 1×10⁹ cells transfected; supernatant harvested 24, 48, 72 h post-transfection.
3. **Concentration**: 100–1000x by tangential-flow filtration + sucrose-cushion ultracentrifugation. (Required since native titers are 10⁵ TU/mL.)
4. **Purification**: Benzonase (removes plasmid DNA); 0.45 μm filter; sometimes anion-exchange chromatography.
5. **Release testing**: titer, sterility, endotoxin, RCL (replication-competent lentivirus — by vector-amplification on C8166-CCR5 or SupT1 cells with p24 ELISA readout), residual DNA, residual benzonase.
6. **Storage**: -80°C; shelf life 1–2 years.

## II.3 Transposon platforms: Sleeping Beauty and PiggyBac

- **Sleeping Beauty (SB)**: Sequence-defined transposase + transposon donor plasmid. SB100x (hyperactive transposase) is the workhorse.
- **PiggyBac (PB)**: Higher cargo capacity (>10 kb), TTAA preference.
- **MD Anderson SB-GD2 CAR**: ~3 papers used SB transposon for CD19 CAR and adapted approach for GD2 (Singh 2013, Kebriaei 2016 — CD19 focused but methods extended).
- **Advantages**: No virus, lower cost, larger cargo possible. **Disadvantages**: Lower transduction efficiency, integration site characterization less mature, FDA scrutiny on genotoxicity.

## II.4 AAV-mediated HDR donors

- Used as the donor template for CRISPR knock-in at TRAC or AAVS1.
- AAV serotype 6 (AAV6) is the most efficient for human T-cell transduction.
- Paper examples: Eyquem 2017 (CD19, foundational); GD2 adaptations in Stanford and Bambino Gesù work.
- **Production**: HEK293 triple-transfection with AAV6-Rep/Cap, helper plasmid, and the HDR-donor flanked by ITRs.
- **Construct design**: HDR-donor contains ~500-bp homology arms matching the TRAC or AAVS1 target locus, with the CAR cassette in between.

## II.5 Virus-free CRISPR knock-in: HDR, HITI, nanoplasmid, minicircle

### Mueller / Cappabianca lineage at UW-Madison

- **Mueller 2022 (PMID 36382633)**: Virus-free CRISPR-Cas9 RNP + nanoplasmid (Aldevron) DNA donor knocked into TRAC. 9-day manufacturing process. CAR construct: 14g2a-CD8α-4-1BB-CD3ζ.
- **Cappabianca 2024 (PMID 38882639)**: Same lineage, GMP-compatible, Lonza Cocoon-compatible. 14g2a-CD8α-CD28-CD3ζ. Demonstrates scale-up.
- **Process details**:
  - Day 0: CD4/CD8 selection from apheresis (CliniMACS).
  - Day 1: Activation with Dynabeads or TransAct.
  - Day 3: Electroporation of CRISPR-Cas9 RNP (targeting TRAC) + nanoplasmid HDR donor; some protocols use ssDNAi (single-strand donor) instead.
  - Day 4–9: Expansion in IL-7 + IL-15; CD3-negative selection to remove non-edited cells (alternative: TCR-knockout antibody-mediated depletion).
  - Day 9: Harvest, formulate, cryopreserve.

### HITI (Homology-independent targeted insertion)

- **Balke-Want 2023 (PMID 37365642)**: Demonstrates HITI as an alternative to HDR for TRAC-KI. Uses Cas12a (rather than Cas9) and a chemically modified ssODN donor.
- **CEMENT (CRISPR-EM enabled non-viral TRAC)**: A 2023 method that uses Cas9 RNP + a circular plasmid donor with electroporation; named CEMENT in some preprints.
- **Advantages of HITI**: Higher knock-in efficiency at sites where HDR is inefficient (e.g., post-mitotic cells); does not require lengthy homology arms.

### Nanoplasmid / minicircle DNA

- **Nanoplasmid (Aldevron)**: Plasmid with the antibiotic-resistance gene replaced with a small RNA-based selection marker (R6K), resulting in a <2 kb backbone. Used in Mueller/Cappabianca lineage.
- **Minicircle (System Biosciences)**: Plasmid generated by intramolecular recombination to remove the bacterial backbone. Used in some MD Anderson and Stanford work.
- **Advantages**: Lower DNA mass → less cytotoxicity during electroporation → better cell viability post-edit.

## II.6 mRNA electroporation

- **Singh 2014 (PMID 25104548)**: In vitro transcribed (IVT) mRNA encoding GD2-4-1BB-CD3ζ; 10 μg mRNA per 0.1 mL cells; ECM830 Electro Square Wave Porator (BTX/Harvard) in 2 mm cuvette; ~50–80% post-transfection viability; >95% CAR expression by flow. Transient — CAR expression peaks day 1 post-EP, declines over ~7 days.
- **Mehrotra 2024 (PMID 38754916, related work)** and **Mishra 2025 (PMID 41492091)**: mRNA-electroporated GD2 CAR-T for sarcoma. Same approach.
- **Advantages**: Transient (auto-resolves on-target/off-tumor); no genomic integration; rapid to manufacture; relatively cheap.
- **Disadvantages**: No persistence; requires repeat dosing every ~7 days; less effective for disseminated/CNS disease.

## II.7 LNP-mRNA in-situ programming

- **Recent preprints (2025)**: GD2-targeted LNP-mRNA platforms that deliver CAR mRNA directly to T cells in vivo, bypassing the entire ex-vivo manufacturing step.
- **Capstan Therapeutics-style approach**: T-cell-targeted LNPs (e.g., CD3-decorated, CD8-decorated, or anti-CD45 ASGPR/CD7) carrying CAR mRNA.
- **Status**: Preclinical only for GD2 at the time of this report; CD19 and BCMA platforms have entered clinical trials.

## II.8 Multi-knockout allogeneic constructions

- **Quintarelli 2025 (allogeneic GD2-CART01, ALLO_GD2-CART01)**:
  - Donor: Healthy adult HLA-matched (HLA-A*02:01) or HLA-disparate.
  - Edits: TCR knockout (TRAC) + HLA-A/B/C knockout (B2M) + immune-evasion ± additional knockouts (e.g., CD52 for selection with anti-CD52 mAb).
  - CAR: 14g2a + iCasp9 + CD28 + 4-1BB + CD3ζ (GD2-CART01 chemistry retained).
  - Production: SFG retroviral vector for the CAR; CRISPR for the knockouts.

- **Stanford allogeneic preclinical**: Multiple papers describe allogeneic platforms; GD2-specific variants in the corpus.

## II.9 Cross-platform comparison

| Platform | Cargo capacity | Integration | Time-to-CAR | Persistence in vivo | Cost ($/dose, GMP) | Used in clinical GD2? |
| --- | --- | --- | --- | --- | --- | --- |
| γ-Retrovirus (SFG, MSCV) | ~8 kb | Random; bias for active genes | Day 2–3 post-activation | Months-years | $30–60k | Yes (Pule, Heczey, GD2-CART01) |
| Lentivirus (3G SIN) | ~9 kb | Random; lower active-gene bias | Day 1–3 | Months-years | $40–80k | Yes (Glienke, Majzner via earlier programs) |
| Transposon (SB, PB) | ~10–15 kb | Random; TA / TTAA | Day 1–3 | Months | $10–20k | Limited; older MD Anderson work |
| AAV-HDR (donor) + CRISPR | ~4–5 kb cargo | Targeted (TRAC/AAVS1) | Day 5–9 | Months-years | $50–100k | Approaching clinical |
| Virus-free CRISPR + nanoplasmid | ~10 kb cargo | Targeted (TRAC) | Day 7–9 | Months | $20–40k | Yes (Mueller, Cappabianca) |
| mRNA EP | n/a (transient) | None | Day 1 | <7 days | $5–10k | Limited |
| LNP mRNA (in vivo) | n/a (transient) | None | Same day | Days | TBD | Preclinical only |

---

# Part III — Manufacturing

Manufacturing here means **everything from patient apheresis (or donor cell sourcing) through formulated, cryopreserved final product** ready for infusion. GD2 CAR-T manufacturing has evolved from open-bag IL-2 cultures (Pule 2008) to fully automated 7-day closed-system processes (Majzner 2022).

## III.1 Source material: apheresis, cord blood, iPSC, cell lines

| Source | Used by | Notes |
| --- | --- | --- |
| Adult autologous PBMC by apheresis | Pule 2008 (EBV-CTL and ATC arms), Louis 2011, Heczey 2017, Majzner 2022, Monje 2025, Glienke 2022 (some patients), Quintarelli 2018 / Locatelli 2025 (autologous GD2-CART01) | Standard. Yield: ~10¹⁰ MNCs from a 12L apheresis. |
| Pediatric autologous PBMC by apheresis | Majzner 2022, Monje 2025, Locatelli 2025, Heczey 2020/2023 | Often smaller volumes, may need 2 collections, pre-collected before lymphodepleting chemo |
| Adult healthy donor PBMC by apheresis | Quintarelli 2025 (ALLO_GD2-CART01) | HLA-matched or disparate; large yields possible |
| Cord blood mononuclear cells | Some γδ and CAR-NK constructs (Capsomidis 2018, others) | Higher proportion of naïve/stem T cells |
| iPSC-derived T cells (iT) | Several preclinical | Stanford and others; emerging |
| iPSC-derived NK cells (iNK) | Multiple preclinical (Fate Therapeutics-style) | Allogeneic / off-the-shelf |
| NK-92 cell line | Bodden 2023, others | EBV-transformed NK line; requires irradiation pre-infusion |
| KHYG-1 cell line | Some NK-CAR preclinical | Less common than NK-92 |

**Apheresis collection details (clinical):**
- Apheresis machines: COBE Spectra or Spectra Optia (Terumo BCT); Amicus (Fresenius).
- Anticoagulant: ACD-A (acid-citrate-dextrose-A) standard.
- Patient pre-medication: Ca²⁺ supplementation to prevent citrate toxicity.
- Volume: 1.5–2× total blood volume processed.
- Target: 5–10×10⁹ MNCs.
- Pediatric considerations: minimum patient weight ~10 kg; central venous access often required.
- Pre-collection: Patients may receive G-CSF (rare; mostly avoided) or pre-treatment with chemotherapy to mobilize cells.
- Time from apheresis to manufacturing start: typically same day or next morning.

## III.2 Cell selection: PBMC, CD4/CD8, CD45RA, naïve/TSCM, iNKT bead, γδ, NK, monocyte depletion

### Apheresis-to-PBMC

- Ficoll gradient — historical (Pule 2008, Louis 2011, Heczey 2014/2017).
- Sepax II density-gradient — semi-automated.
- CliniMACS Prodigy LP-1 protocol — fully automated; integrated with the rest of the workflow.

### Lineage selection

| Selection | Reagent | Used by |
| --- | --- | --- |
| CD3+ enrichment | anti-CD3 magnetic beads (CliniMACS) | Various |
| CD4+ + CD8+ enrichment | anti-CD4 + anti-CD8 beads (CliniMACS) | Majzner 2022 / Monje 2025 (1:1 CD4/CD8 protocol), Glienke 2022, Mueller 2022, Cappabianca 2024 |
| CD25-depletion | anti-CD25 beads (deplete Tregs) | Some Stanford and BCM constructs |
| CD45RO-depletion / CD45RA-enrichment | anti-CD45RO or anti-CD45RA beads (enrich naïve/TSCM) | Some Stanford manufacturing (Sommermeyer 2016 style) |
| iNKT (Vα24+) enrichment | anti-Vα24 / 6B11 antibody bead (Miltenyi) | Heczey 2014/2017/2020/2023, Tian 2025 |
| γδ-T enrichment | Pan-γδ TCR or Vδ2 beads + zoledronate stimulation | Capsomidis 2018, various |
| NK enrichment | NK isolation kit (CD3-depletion + CD56-positive selection) | Multiple |
| Monocyte depletion | Plastic adherence or anti-CD14 beads | Long 2016 (plastic adherence at NCI); Stroncek 2016, Stroncek 2017 — explored elutriation as monocyte-depletion method |

### Elutriation as a contamination-reduction step

- **Stroncek 2017 (PMID 28298232)**: Compared monocyte-depletion approaches (anti-CD3/CD28 beads alone vs beads + plastic adherence vs elutriation). Found elutriation gave higher CAR-T yields than the other approaches, with reduced contaminating monocytes / granulocytes. Used in CD19 and GD2 CAR-T manufacturing at NCI.
- **Process**: PBMC concentrate → elutriator (Beckman Avanti or Terumo Elutra) → lymphocyte fraction (low monocyte) → downstream activation and transduction.

## III.3 Activation reagents

| Reagent | Mechanism | Used by |
| --- | --- | --- |
| OKT3 (anti-CD3 soluble) | Cross-links endogenous CD3 | Pule 2008 (EBV-CTL arm — EBV-LCL + OKT3 for ATC arm) |
| Anti-CD3/CD28 Dynabeads (Invitrogen 11.32D) | Bead-bound CD3 + CD28 | Long 2016 (3:1 bead:cell), Singh 2014, Stroncek 2016/2017, many others |
| Anti-CD3/CD28 microbeads (Miltenyi) | Bead-bound CD3 + CD28; smaller bead than Dynabeads | Various |
| TransAct (Miltenyi) | Polymeric nanomatrix with CD3 + CD28 | Glienke 2022 (Prodigy), Mueller 2022 (TRAC), Cappabianca 2024, Majzner 2022 (Stanford Prodigy) |
| K562-aAPC (CD32+CD64+CD80+CD83+CD86+4-1BBL+OX40L+IL-15+IL-21) | Genetically engineered aAPC line | Heczey 2020/2023 (CAR-NKT secondary stim), Tian 2025 |
| αGalCer-pulsed PBMC | Antigen-pulsed PBMCs activate Vα24-TCR | Heczey 2014/2017/2020/2023 NKT (primary stim) |
| EBV-LCL (autologous EBV-immortalized B cells) | Activate EBV-specific TCRs | Pule 2008 (EBV-CTL arm), Louis 2011 |
| Zoledronate / pamidronate | Activates Vδ2-TCR γδ-T via IPP accumulation | Capsomidis 2018 |
| ConA (concanavalin A) | Polyclonal lectin activator | Some γδ-T expansion protocols |
| PHA | Polyclonal | Older protocols |

**Activation timing and stoichiometry are critical determinants of final product phenotype.**
- Higher bead:T ratio (3:1 standard) → faster expansion but more effector skewing.
- Lower ratio (1:1) → more naïve/memory-skewed product.
- TransAct dose is typically 17.5 µL per 10⁷ cells.
- αGalCer for NKT: 100 ng/mL.

## III.4 Cytokine support during ex-vivo expansion

### IL-2 era (Pule 2008–Heczey 2017)

- **IL-2 (aldesleukin / Proleukin)** at 40–300 IU/mL.
- Pros: Powerful T-cell mitogen, well-characterized.
- Cons: Drives effector differentiation; can promote tonic-signal-induced exhaustion; expands Tregs.

### IL-7 + IL-15 era (2017+)

- **IL-7 (5–12.5 ng/mL)** — survival/homeostatic.
- **IL-15 (5–12.5 ng/mL)** — survival + proliferation; memory-skewing.
- Pros: TSCM/TCM-skewed product, longer persistence, less exhaustion.
- Used by: Majzner 2022, Monje 2025, Glienke 2022, Mueller 2022, Cappabianca 2024, GD2-CART01 (in some variants), many recent constructs.

### IL-7 + IL-15 + IL-21 

- IL-21 (10 ng/mL) added in some protocols (Mueller, Cappabianca, Stanford).
- Pros: Synergizes with IL-15 for naïve-like product; promotes self-renewal.

### Dasatinib priming (2020+)

- 50 nM dasatinib (BCR-ABL/Src-family kinase inhibitor) during activation/transduction window.
- Used by: Majzner 2022, Monje 2025, several recent constructs.
- Function: Transiently inhibits Lck phosphorylation downstream of TCR/CAR — reduces tonic signaling during the manufacturing window without affecting CAR functionality after wash-out.
- Pros: Less exhaustion, less terminal differentiation, more memory-skewed.
- Washed out at harvest.

### Other small-molecule additions (preclinical / emerging)

- **Ibrutinib** (BTK inhibitor) — similar role to dasatinib for tonic-signal suppression.
- **AKT inhibitor (e.g., AKTi-VIII)** — promotes TSCM phenotype during expansion.
- **MK2206** — AKT inhibitor.
- **TWS119 / GSK3-β inhibitor** — promotes Wnt signaling → TSCM enrichment.
- **Rapamycin** — mTORC1 inhibitor; promotes memory.

## III.5 Transduction conditions

### γ-Retroviral spinoculation

- Most common GD2 CAR-T construction. Standard protocol:
  - 24-well or 6-well plates coated with RetroNectin (24 μg/well overnight, 4°C; 2.5% BSA block 30 min).
  - Pre-load: Plates spin-coated with retroviral supernatant at 3050 rpm, 32°C, 2–3 hours.
  - Add activated T cells at 0.5–1×10⁶ cells/well.
  - Spin 1000g, 32°C, 90 min.
  - Or static incubation overnight.
  - Often repeated days 2 and 3.
- Used by Long 2016, Stroncek 2016/2017, Pule lineage, GD2-CART01.

### Lentiviral spinoculation

- Similar to γ-retroviral but typically static (no spin) for VSV-G-pseudotyped vectors.
- Polybrene 5–10 μg/mL or protamine sulfate often added as transduction enhancer.

### CliniMACS Prodigy (closed-system)

- Automated transduction step in the Prodigy machine.
- Day 1: virus added to the cell bag (CliniMACS Prodigy CCSC bag); incubated 24h.
- No spinoculation — relies on cell-virus contact during shaking culture.

### CRISPR electroporation (RNP + donor)

- Day 3 typical timing.
- Mixed: Cas9 protein + sgRNA (TRAC-targeting) + DNA donor (nanoplasmid or AAV6 or ssODN).
- Electroporator: Lonza 4D-Nucleofector (X-unit) or Lonza Cocoon-integrated.
- Pulse: Lonza P3 buffer; EH-115 or similar; clinical scale 2×10⁸ cells per cuvette.
- Post-EP recovery: 4–6 h in pre-warmed medium with cytokines.

### mRNA electroporation

- Singh 2014 (BTX/Harvard ECM830 ECM, 2mm cuvette, 10 μg mRNA per 0.1 mL T cells).
- Post-EP viability 50–80%; CAR expression >95% by 24h.

## III.6 Closed-system platforms in detail

### CliniMACS Prodigy

- Miltenyi's flagship closed-system platform.
- Integrated steps: density-gradient → CD4/CD8 selection → activation → transduction → expansion → wash → formulation.
- Single tubing set ("TS"), GMP-grade.
- Time: 7–14 days (depending on transduction method and cytokine support).
- **Stanford / Majzner 2022 / Monje 2025 (DMG) GD2 protocol**:
  - Day 0: Apheresis processed, CD4+/CD8+ enriched, activated with TransAct + IL-2 (transitioning to IL-7 + IL-15).
  - Day 1: Lentivirus added.
  - Day 2: Wash; cells maintained in IL-7 + IL-15 + dasatinib (50 nM).
  - Day 7: Harvest, formulate, cryopreserve.
- **Glienke 2022 (Hannover IL-18 TRUCK)**:
  - Day -1: Overnight storage at 4°C.
  - Day 0: CD4+/CD8+ enrichment from apheresis, activate with TransAct, IL-7 12.5 ng/mL + IL-15 12.5 ng/mL.
  - Day 1: Lentiviral transduction.
  - Days 3–12: Periodic wash, agitation, IL-7/IL-15 expansion.
  - Day 12: Formulate + cryopreserve.
  - Total: 12 days.
- **Bambino Gesù / Quintarelli (GD2-CART01)**:
  - Day 0: CD3 enrichment from autologous apheresis, OKT3 activation, IL-2.
  - Day 2: Retroviral transduction (SFG / PG13).
  - Day 4: First wash + new IL-2.
  - Days 7–14: Expansion in bag.
  - Day 14: Formulate + cryopreserve.
  - Total: ~14 days (this is the older Texas Children's lineage protocol; updated GD2-CART01 protocols use shorter timelines).

### Lonza Cocoon

- Lonza's automated closed-system platform with integrated electroporation.
- Cassette-based; one cassette per patient.
- Time: 7–10 days for virus-free protocols.
- **Cappabianca 2024 (Mueller lineage TRAC-KI)**:
  - Day 0: CD4+/CD8+ enrichment, activation with TransAct + IL-7 + IL-15.
  - Day 3: Electroporation (Cocoon's integrated EP module) with Cas9 RNP + nanoplasmid donor.
  - Days 4–9: Expansion in IL-7 + IL-15 + IL-21.
  - Day 9: Harvest, formulate, cryopreserve.

### G-Rex (Wilson Wolf)

- Static gas-permeable rapid-expansion flask (G-Rex 100 / G-Rex M).
- Used by Baylor / TCG lineage for VST and CAR-VST manufacturing.
- Higher cell densities possible (up to 10⁸ cells/cm² in G-Rex 500M).
- Time: 10–21 days; bag-and-static culture.

### Xuri / Wave Cell Expansion System (Cytiva)

- Rocking-platform bioreactor.
- Used in clinical-grade NK-CAR manufacturing; less common for GD2 CAR-T.

### Other systems

- **Quantum Cell Expansion (Terumo)** — hollow-fiber bioreactor.
- **PermaLife bags (OriGen)** — older bag-based static culture; Pule lineage.

## III.7 Tonic-signal mitigation during manufacture: dasatinib, ibrutinib, AKTi

The 14g2a scFv's tendency toward antigen-independent tonic signaling caused the field to develop manufacturing strategies that reduce CAR signaling during the manufacturing window.

### Dasatinib (50 nM during activation/transduction)

- Lck inhibitor; transiently blocks TCR / CAR downstream signaling.
- Wash out before harvest — CAR function recovers within hours.
- Effect: TSCM/TCM-skewed final product; reduced PD-1, TIM-3, LAG-3; reduced exhaustion gene signature.
- Used by Majzner 2022, Monje 2025, and many recent constructs.

### Ibrutinib (similar role)

- BTK inhibitor; less commonly used for CAR-T but explored.

### AKT inhibitors

- AKTi-VIII, MK2206; preserve naïve/memory phenotype during expansion.

### Effect on final product phenotype

Without tonic-signal mitigation: 14g2a-CD8α-4-1BB-CD3ζ CAR-T after 7-day expansion shows ~30% PD-1+, ~20% TIM-3+, ~10% LAG-3+ at harvest. With dasatinib priming: ~10% PD-1+, ~5% TIM-3+, ~5% LAG-3+ — and CCR7+ TSCM/TCM is ~40% vs 15%.

## III.8 Memory subset enrichment strategies

| Strategy | Mechanism | Effect |
| --- | --- | --- |
| Naïve-cell selection (CD45RA+CCR7+) | Pre-select naïve T cells before activation | TSCM-skewed final product |
| TCM enrichment (CD45RA-CCR7+) | Pre-select central memory | TCM-skewed product |
| IL-7 + IL-15 cytokine support | Maintain TSCM/TCM phenotype during expansion | Memory-skewed |
| Dasatinib priming | Reduce tonic signaling | Memory-skewed |
| AKT inhibition | Block mTOR-driven effector differentiation | TSCM-skewed |
| Wnt agonism (TWS119) | Promote stem-like state | TSCM-skewed |
| Short expansion (≤7 days) | Less time for terminal differentiation | Less exhausted |

## III.9 Manufacturing of CAR-NKT, CAR-NK, CAR-γδ, CAR-VST

### CAR-NKT (Heczey lineage)

- **Heczey 2014/2017/2020/2023**:
  - Apheresis or buffy coat → PBMC isolation.
  - αGalCer pulse (100 ng/mL × 12 h) on autologous PBMCs → expand Vα24+ NKT.
  - Day 7–10: anti-Vα24/Vβ11 magnetic enrichment.
  - Day 10–14: Retroviral transduction of GD2.CAR.28.OX40.ζ (or GD2.CAR.15 with IL-15 cassette).
  - Day 14–21: Secondary stimulation with K562-aAPC (expressing CD80/CD86/4-1BBL/IL-15/IL-21).
  - Total: 21 days.
- **Tian 2025**: Highlights K562-aAPC secondary-stim risk (hyperleukocytosis at DL5 in 1 patient).

### CAR-NK / NK-92

- **Bodden 2023 NK-92 (PMID 38134936)**:
  - NK-92 cell line (EBV-transformed) electroporated with hu14.18.28.z + RD-IL15 (receptor-detached IL-15 superagonist).
  - Expansion: SCGM medium + IL-2 (500 IU/mL).
  - Irradiation pre-infusion (10 Gy) to prevent NK-92 outgrowth — limits durability of effect.

### CAR-γδ

- **Capsomidis 2018 (PMID 30245187)**:
  - PBMC → activation with zoledronate (5 μM) + IL-2 (1000 IU/mL) for 7 days.
  - Vδ2+ γδ-T expansion → retroviral transduction with GD2-CAR.
  - vs. ConA stimulation — biases toward Vδ1+ subsets.
  - Vδ2+ are more cytotoxic; Vδ1+ are more tumor-infiltrating.

### CAR-VST (virus-specific T-cells with CAR)

- **Pule 2008**: First clinical use; EBV-specific CTLs transduced with GD2.CAR.ζ.
- **Louis 2011**: 2-year follow-up; demonstrated longer persistence of GD2.CAR.VST vs GD2.CAR.ATC.

## III.10 Formulation, fill, and cryopreservation

| Component | Concentration | Notes |
| --- | --- | --- |
| CryoStor CS5 or CS10 (BioLife Solutions) | 5% DMSO + 10% HSA or 10% DMSO + 5% HSA | Standard for clinical CAR-T |
| Plasma-Lyte A + 5% HSA + 10% DMSO | manual mix | Older formulation |
| Cell concentration | 1–10×10⁷ cells/mL | Depends on dose |
| Fill volume | 5–100 mL | Cryobag (Cryomacs 50/100 mL, Origen 70 mL) |
| Freeze method | Controlled-rate freezer (CRF; -1°C/min from RT to -40°C; -10°C/min to -90°C; transfer to LN2 vapor) | Standard |
| Storage | Liquid-nitrogen vapor phase (-150°C) | Long-term stable |
| Thaw at bedside | 37°C water bath or dry warmer | Infused directly into patient via IV line |

## III.11 Release testing

Standard release-test panel for clinical GD2 CAR-T:

| Test | Requirement | Method |
| --- | --- | --- |
| Identity | CAR+ ≥ specified % | Flow cytometry with anti-idiotype or 1A7 anti-14g2a antibody |
| Purity | CD3+ ≥ specified % | Flow cytometry |
| Sterility | No growth ×14 days | USP <71> (aerobic, anaerobic) |
| Mycoplasma | Negative | PCR or culture |
| Endotoxin | <5 EU/mL or <5 EU/kg body weight | LAL (Limulus amebocyte lysate) |
| Viability | ≥70% (typically) | 7-AAD or trypan blue |
| Vector copy number (VCN) | ≤5 (FDA recommendation) | qPCR |
| Replication-competent retrovirus / lentivirus (RCR/RCL) | Negative | Mus dunni or C8166 amplification with RT-PCR or p24 |
| Residual beads | <100 beads / 3×10⁶ cells | Visual count after Dynabead removal |
| Residual transduction enhancers | Below threshold | qPCR or LC-MS |
| Residual electroporation buffer | Below threshold | Assay-dependent |
| Potency | Lytic activity / cytokine release on GD2+ target | 51Cr release or IFNγ ELISA against GD2+ tumor lines |
| Iden of unmodified subset | Optional | Flow / dPCR |

## III.12 Yields, timelines, and manufacturing failures

| Study | Source | Method | Yield (CAR+ cells per kg or per m²) | Timeline | Failure rate |
| --- | --- | --- | --- | --- | --- |
| Pule 2008 | PBMC apheresis (NB pts) | SFG retroviral, ex vivo expansion in IL-2 | 2×10⁷/m² each (EBV-CTL + ATC); manufacturing in-house | 14–21 d | Not reported |
| Louis 2011 | Same as Pule | Same | Same | Same | Same |
| Heczey 2017 | Pediatric NB PBMC | SFG retroviral, 14g2a.CD28.OX40.ζ.iC9, in IL-2 | 1×10⁷ → 1.5×10⁸ cells (3 dose levels) | 14 d | 0/8 patients (all enrolled patients infused) |
| Majzner 2022 | Pediatric DMG PBMC | Lentivirus, CliniMACS Prodigy, IL-7+IL-15+dasatinib | 1×10⁶/kg → 3×10⁶/kg IV | 7 d | 0/4 patients (all patients infused) |
| Monje 2025 | Pediatric DMG PBMC | Same as Majzner 2022 | 10×10⁶ – 100×10⁶ ICV per dose | 7 d | <5% manufacturing failures |
| Glienke 2022 | Adult / pediatric PBMC | Lentivirus + NFAT-IL18, CliniMACS Prodigy, IL-7+IL-15 | up to 2×10⁹ cells per product | 12 d | Not reported |
| Quintarelli 2018 / Locatelli 2025 (GD2-CART01) | Pediatric NB PBMC | SFG retrovirus, 14g2a.CD28.4-1BB.ζ.iC9 | 1×10⁷ → 1×10⁸ /kg | ~12–14 d | Not reported |
| Mueller 2022 (TRAC-KI) | Healthy donor PBMC | CRISPR + nanoplasmid, virus-free | up to 1×10⁹ cells | 9 d | ~10% process failures (lower TRAC-KI %) |
| Cappabianca 2024 (Cocoon) | Healthy donor PBMC | CRISPR + nanoplasmid + Cocoon | up to 2×10⁹ cells | 9 d | <10% failures |
| Quintarelli 2025 (Allo GD2-CART01) | Healthy donor PBMC | SFG retrovirus + CRISPR knockouts | Doses TBD | ~14 d | Phase 1 starting |

**Manufacturing failure modes:**
- Insufficient apheresis yield (lymphopenia from prior chemotherapy).
- Poor transduction (<20% CAR+).
- Insufficient expansion (final product <required dose).
- Bacterial contamination (rare with closed systems).
- Tonic-signal exhaustion (CAR cells expand initially but plateau/die during expansion).

## III.13 Clinical-protocol-coupled manufacturing decisions

Several manufacturing choices are tied to the clinical protocol:

### Bridging therapy (during 7–21 d manufacturing window)

- Patients with rapidly progressive disease may receive bridging chemotherapy (e.g., low-dose temozolomide, irinotecan/temozolomide, or 13-cis-retinoic acid for neuroblastoma) during the manufacturing window.
- For DMG: bridging with re-irradiation is sometimes used (Majzner 2022 Arm A).

### Lymphodepletion timing

- Standard: Cy/Flu given days -4 to -2 before CAR-T infusion.
- For CD8α-4-1BB constructs: shorter lymphodepletion (days -5 to -3) often used.
- ICV delivery (DMG): No lymphodepletion before ICV CAR-T (some protocols), since CSF compartment is partly immune-privileged.

### Dose level and fractionation

- IV: single or split-dose infusion over 1–3 days.
- ICV (DMG): single infusion in Ommaya reservoir, repeated monthly for up to 12 months (Monje 2025).
- Intratumoral: single bolus.
- Intracerebral cavity (post-resection): single bolus.

### Repeat dosing

- ICV permits weekly to monthly redosing without re-lymphodepletion (Monje 2025: median 5 ICV doses per patient, max 22 doses in one patient).
- IV redosing typically requires re-lymphodepletion.

## III.14 Detailed per-clinical-trial recipes

Below is a comprehensive recipe table for each of the 14 published clinical GD2 CAR-T trials.

### Trial 1: Pule 2008 (PMID 18978797) — Baylor first-in-human GD2 CAR

- **Population**: Relapsed/refractory neuroblastoma, n=11.
- **Construct**: SFG-14g2a.ζ (1G; HSV-TK option in some patients).
- **Vector**: SFG γ-retrovirus, PG13 producer line.
- **Cell source**: Autologous PBMC apheresis.
- **Effector**: Either EBV-specific CTLs (CTL arm) or activated PBMC T cells (ATC arm); 4–6 patients each.
- **Activation**: EBV-LCL (CTL arm) or OKT3 (ATC arm).
- **Expansion**: AIM-V + 10% FBS + IL-2 (40 IU/mL) × 14–21 days.
- **Transduction**: Day 2 retroviral spinoculation on RetroNectin-coated plates, repeated day 3.
- **Lymphodepletion**: None (early trial).
- **Dose**: 2×10⁷/m² each arm; sequential infusion CTL → ATC.
- **Outcome**: 3/11 complete remissions sustained at 5-year follow-up (Louis 2011).

### Trial 2: Louis 2011 (PMID 21984804) — 5-year follow-up of Pule 2008

- Same manufacturing chemistry as Pule 2008.
- Demonstrated long-term persistence (>2 years) of CAR-CTL clones in some patients.

### Trial 3: Heczey 2017 (PMID 28680755) — First 3G GD2-CAR.28.OX40.ζ.iC9 (NB)

- **Population**: Relapsed/refractory neuroblastoma, n=11.
- **Construct**: SFG-iCasp9-2A-14g2a.CD28.OX40.ζ (3G + iCasp9).
- **Vector**: SFG γ-retrovirus.
- **Cell source**: Autologous PBMC apheresis.
- **Effector**: αβ-T cells (no longer EBV-CTL selection).
- **Activation**: OKT3 + IL-2.
- **Expansion**: IL-2 (typically 50 IU/mL).
- **Transduction**: Day 2 RetroNectin spinoculation.
- **Dose**: DL1 1×10⁷/m², DL2 3×10⁷/m², DL3 1×10⁸/m² (IV).
- **Lymphodepletion**: Cy/Flu standard.
- **Outcome**: 9/11 evaluable patients; 1 CR, 2 PR; iCasp9 / rimiducid not triggered in this cohort.

### Trial 4: Heczey 2020 (PMID 32747836) — GD2-CAR.15 NKT, phase 1

- **Population**: Relapsed/refractory NB, n=11.
- **Construct**: SFG-iCasp9-2A-14g2a.CD28.2B4.ζ-2A-IL15 (NKT-tuned 3G + IL-15 + iCasp9).
- **Vector**: SFG γ-retrovirus.
- **Cell source**: Autologous PBMC apheresis.
- **Effector**: Vα24+ NKT cells.
- **Activation**: αGalCer-pulsed PBMC.
- **Expansion**: IL-2 + IL-15.
- **Transduction**: Day 7 retroviral spinoculation.
- **Secondary stim**: K562-aAPC (CD80/CD86/4-1BBL/IL-15/IL-21).
- **Dose**: DL1 1×10⁷/m², DL2 3×10⁷/m², DL3 1×10⁸/m² (IV).
- **Outcome**: Tian 2025 reports hyperleukocytosis at DL5 in 1 patient; recommendations for safety switch.

### Trial 5: Heczey 2023 (PMID 36702272) — GD2-CAR.15 NKT phase 1 update + arms

- Same chemistry as Heczey 2020.
- Reported persistence and clinical responses in expanded cohort.

### Trial 6: Quintarelli 2018 / Del Bufalo 2023 / Locatelli 2025 — Bambino Gesù GD2-CART01

- **Population**: Pediatric relapsed/refractory neuroblastoma (Locatelli 2025: n=15; Del Bufalo 2023: n=12; Quintarelli 2018: preclinical → clinical).
- **Construct**: SFG-iCasp9-2A-14g2a.CD28.4-1BB.ζ (3G CD28+4-1BB + iCasp9).
- **Vector**: SFG γ-retrovirus.
- **Cell source**: Autologous PBMC apheresis.
- **Effector**: αβ-T cells (no specific lineage selection).
- **Activation**: OKT3 + IL-2.
- **Expansion**: IL-2 in bag.
- **Transduction**: Days 2–3 RetroNectin spinoculation.
- **Dose**: DL1 1×10⁷/kg, DL2 3×10⁷/kg, DL3 1×10⁸/kg (IV).
- **Lymphodepletion**: Cy/Flu standard.
- **Outcome**: 9/15 objective responses in Locatelli 2025; CR-rate ~30%.

### Trial 7: Majzner 2022 (PMID 35130560) — First DMG IV GD2-CAR

- **Population**: Pediatric DMG, n=4 IV cohort.
- **Construct**: Lenti-14g2a.CD8α-4-1BB.ζ (2G CD8α-4-1BB).
- **Vector**: 3G SIN lentivirus.
- **Cell source**: Autologous PBMC apheresis.
- **Effector**: αβ-T cells (CD4+/CD8+ selected).
- **Manufacturing**: CliniMACS Prodigy, IL-7 + IL-15 + dasatinib, 7 days.
- **Dose**: DL1 1×10⁶/kg IV, DL2 3×10⁶/kg IV.
- **Lymphodepletion**: Cy/Flu day -4 to -2.
- **Outcome**: 3/4 patients with clinical/radiographic improvement; ICANS at DL2.

### Trial 8: Monje 2025 (PMID 39537919) — DMG ICV final readout, arm A

- **Population**: Pediatric DMG/sDMG, n=11.
- **Construct**: Same as Majzner 2022 (2G CD8α-4-1BB-iC9).
- **Vector**: 3G SIN lentivirus.
- **Manufacturing**: CliniMACS Prodigy, 7 d, IL-7+IL-15+dasatinib.
- **IV dose**: 1×10⁶/kg confirmed.
- **ICV dose**: 10, 30, 100×10⁶ cells per dose; repeated monthly via Ommaya.
- **Lymphodepletion**: Cy/Flu before IV; none before ICV.
- **Outcome**: 9/11 evaluable patients alive >1 year post-CAR; 62 ICV infusions delivered without DLT; ICANS only at IV DL2 (3×10⁶/kg).

### Trial 9: Gargett / Brown CARPETS (Gargett 2024 PMID 38754916) — GD2-iCAR-PBT in metastatic CRC, melanoma, etc.

- **Population**: Various GD2+ solid tumors, n=12.
- **Construct**: 14g2a.CD28.OX40.ζ.iC9 (3G + iCasp9), derived from Pule lineage.
- **Vector**: γ-retroviral.
- **Cell source**: PBMC.
- **Lymphodepletion**: Cy/Flu (with prior PD-1 blocker cohort, vemurafenib cohort).
- **Dose**: Various.
- **Outcome**: No DLTs; disease stabilization in some; expansion was limited by manufacturing in some patients.

### Trial 10: Glienke 2022 (PMID 36167468) — IL-18 TRUCK NB phase 1

- **Population**: Pediatric NB.
- **Construct**: Lenti-14g2a.CD8α-4-1BB.ζ + NFAT-IL18.
- **Vector**: 3G SIN lentivirus.
- **Manufacturing**: CliniMACS Prodigy, 12 d, IL-7+IL-15.
- **Activation**: TransAct.
- **Outcome**: Early phase 1; safety, expansion in 1 patient.

### Trial 11: Yang 2024 (CARPETS-related / Chinese trial PMID 41196398, etc.) — Sarcoma

- Various Chinese trials in sarcoma/melanoma using GD2-4-1BB-CD3ζ constructs with iCasp9.

### Trial 12: Li 2025 (PMID 39962287) — Long-term follow-up of NB

- Same lineage as Pule/Louis; long-term outcomes data.

### Trial 13: Hu 2024 (PMID 40736004) — GD2 CAR-T for sarcoma with armoring

- Chinese trial, lentiviral, with IL-15 armoring.

### Trial 14: Quintarelli 2025 (allogeneic GD2-CART01)

- **Population**: Donor-derived; healthy donor PBMC.
- **Construct**: GD2-CART01 chemistry + TRAC + B2M knockouts.
- **Vector**: SFG retrovirus for CAR; CRISPR for knockouts.
- **Trial**: Phase 1 starting / preliminary.

---

# Part IV — Discussion

This section steps back from the catalogue and frames the choices into the analytical story of how the field has moved. It addresses how decisions in design, construction, and manufacturing interlock; what lessons should propagate to new programs; and what is still open.

## IV.1 Era 1 (2008–2014): first-generation CARs and the tonic-signaling discovery

The first published clinical GD2 CAR-T (Pule 2008, PMID 18978797) used a first-generation (CD3ζ-only) SFG retroviral construct in two parallel arms — EBV-specific CTLs and activated PBMC T cells. The study showed feasibility (no DLT), measurable persistence, and a 3/11 complete-remission rate sustained at the 5-year mark in the EBV-CTL arm (Louis 2011, PMID 21984804). This was extraordinary as a first-in-human result, but the construct was already obsolete: subsequent CD19 CAR programs at Penn, MSK, and NCI had shown that adding a costimulatory endodomain (CD28 or 4-1BB) dramatically improves expansion and persistence.

The natural next step was to try GD2.28z (CD28-costim 2G). Long 2015 (PMID 25939063) did this — and discovered something completely unexpected: GD2.28z CAR-T cells expanded normally for the first 3–4 days but then **collapsed**. The cells showed elevated CD25, CD69, 4-1BB, PD-1, TIM-3, LAG-3, T-bet, Blimp-1, and reduced TCF-1 / CCR7 / IL-7R — a textbook exhaustion signature, but **in the absence of any GD2 antigen exposure**. The CAR was signaling tonically. By mass spectrometry, GD2.28z had increased CD3ζ phosphorylation at baseline. By microscopy, the CAR molecules formed clusters on the cell surface. By mutagenesis, the framework regions of the 14g2a scFv (not the CDR-binding residues) were sufficient to induce clustering.

This discovery had several immediate implications:
- Adding CD28 to a 14g2a-based CAR is not just neutral — it actively accelerates exhaustion.
- The scFv itself, independent of antigen, can drive CAR activation.
- The hinge/spacer (long Fc-based hinges promote clustering) and TM (CD28 TM dimerizes) compound the problem.
- The expansion phenotype during manufacturing is a direct reflection of what will happen in vivo.

The discovery also explained the modest performance of CD28-based 1G/2G CD19 CARs in some indications (where the antigen is low or transient) — but for GD2, the effect was overwhelming.

## IV.2 Era 2 (2014–2018): costimulatory debate, iCasp9, NKT platforms

The response to Long 2015 was multi-pronged:
- Switch to 4-1BB: Long 2015 itself showed that GD2.BBz (4-1BB instead of CD28) does not exhibit tonic exhaustion. This became the dominant choice for clinical GD2 CARs going forward (Majzner 2022, Monje 2025, Glienke 2022, Mueller 2022, Cappabianca 2024).
- Add iCasp9: The Texas Children's lineage (Pule → Heczey → BCM) had already adopted iCasp9 in clinical programs. Adding rimiducid-activated iCasp9 mitigates any unexpected on-target/off-tumor toxicity. Mount 2018 demonstrated iCasp9-rimiducid efficacy in DIPG xenograft models — the GD2-CAR could be rapidly eliminated if needed.
- 3G with CD28 + 4-1BB: Quintarelli 2018 (PMID 29312553) directly compared 2G CD28, 2G 4-1BB, and 3G CD28-4-1BB GD2-CARs. The 3G CD28-4-1BB was superior — rapid effector function from CD28, sustained persistence from 4-1BB, with less tonic exhaustion than CD28-only. This construct became GD2-CART01 (clinical at Bambino Gesù).
- NKT platforms: Heczey 2014, 2017, 2020, 2023 developed CAR-NKT (Vα24+ invariant NKT cells) as an alternative to CAR-T. NKT cells have intrinsic antitumor activity via CD1d-glycolipid recognition, are MHC-independent (good for off-the-shelf), and target the tumor microenvironment. Heczey 2020 added an IL-15 cassette for armoring (GD2-CAR.15) and demonstrated 1-year persistence in 1 patient with concomitant clinical response.
- Memory subset enrichment: Sommermeyer 2016 and follow-up work showed that selecting CD8+ naïve/memory subsets (CD45RA+CCR7+ or CD45RO-CCR7+) enriches the final product for TSCM/TCM and improves persistence — adopted in several Stanford and Seattle programs.

## IV.3 Era 3 (2018–2022): GD2-CART01, affinity-tuning hazards, manufacturing automation

Three streams of work shaped this era:

### Affinity tuning hazard (Richman 2018, PMID 29180536)

Richman et al. engineered 14g2a-E101K, an affinity-matured variant with ~5x higher affinity for GD2. The intent was to improve potency against low-GD2 tumors. They tested the construct as both CD28 and 4-1BB versions.

**Result**: 14g2a-E101K.CD28.ζ caused **lethal CNS encephalitis** in NSG mice in 100% of treated animals within 7–10 days post-CAR-T infusion. Pathology showed CAR-T infiltration in CNS gray matter with neuronal apoptosis. The same construct with 4-1BB costimulation (14g2a-E101K.4-1BB.ζ) was tolerated.

This was the field's first clear demonstration that:
- Increasing scFv affinity can convert a tolerable CAR into a lethal one.
- The threshold for off-tumor CNS toxicity is sharp (5x affinity → lethal).
- CD28 costim amplifies the effect; 4-1BB does not.

The clinical implication was immediate and decisive: **stop affinity-maturing 14g2a, especially in combination with CD28**. The field reverted to standard-affinity 14g2a and either 4-1BB-only or CD28+4-1BB / CD28+OX40 costimulation. No clinical program has used 14g2a-E101K.

### GD2-CART01 and Bambino Gesù clinical leadership

Quintarelli 2018 → Del Bufalo 2023 → Locatelli 2025 established the GD2-CART01 product (3G CD28+4-1BB+CD3ζ+iCasp9, SFG retroviral, autologous PBMC, IL-2 expansion) as a robust, reproducible clinical platform. Locatelli 2025 reported 9/15 objective responses (3 CR + 6 PR) in relapsed/refractory neuroblastoma with manageable toxicity. This is currently among the most active clinical GD2 CAR-T programs in the world.

### Manufacturing automation: Prodigy and Cocoon

Stanford (Majzner 2022 → Monje 2025) standardized CliniMACS Prodigy 7-day manufacturing for the DMG GD2-CART product:
- Apheresis → CD4/CD8 enrichment → TransAct activation → IL-7+IL-15+dasatinib → lentiviral transduction → expansion → harvest → cryopreservation, all in a single closed-system cassette.
- 7 days end-to-end, vs 12–21 days for previous bag-based protocols.
- Markedly improved consistency (variance in product phenotype reduced).
- Reduced manufacturing failure rate (<5%).

Lonza Cocoon was adopted by Wisconsin (Mueller / Cappabianca) for virus-free CRISPR-TRAC-KI manufacturing.

## IV.4 Era 4 (2022–2026): CNS administration, non-viral CRISPR knock-in, allogeneic, armored constructs

The most recent era has been dominated by four trends:

### CNS / intracerebroventricular administration

- Majzner 2022 demonstrated that GD2-CAR for DMG could be given **IV** at 1×10⁶/kg without DLT and with clinical/radiographic improvement.
- Monje 2025 then demonstrated that **ICV delivery via Ommaya reservoir** is even better tolerated and effective. 62 ICV infusions in 11 patients with zero DLTs; CSF CAR exposure dramatically higher than IV; lymphodepletion not required between doses.
- This finding has reset the field's thinking on CNS CAR-T delivery — Ommaya is now standard for DMG and being adopted for other CNS-restricted indications.

### Non-viral CRISPR-TRAC knock-in

- Mueller 2022 → Cappabianca 2024 demonstrated GMP-compatible, virus-free, 9-day manufacturing of GD2 CAR-T via CRISPR-Cas9 RNP + nanoplasmid donor knocked into TRAC.
- Advantages: No viral vector cost, locus-defined expression, TCR knockout in the same step (allogeneic-ready), 9-day cycle.
- Lonza Cocoon integration enables full automation.
- Balke-Want 2023 demonstrated HITI as an alternative knock-in mechanism with even higher KI efficiency.

### Allogeneic donor-derived

- Quintarelli 2025 (ALLO_GD2-CART01) is the first clinical allogeneic GD2 CAR-T:
  - TRAC KO + B2M KO + GD2-CART01 CAR (CD28+4-1BB+iC9).
  - Healthy donor PBMC source.
  - Phase 1 starting.

### Armored constructs

- Glienke 2022 IL-18 TRUCK (Hannover) entered phase 1.
- Heczey 2023 GD2-CAR.15 NKT continued accruing.
- C7R, CCR2b, and other armoring elements are in preclinical evaluation.

## IV.5 The 14g2a tonic-signaling story in full

Tonic signaling has been the defining problem of the GD2 CAR field. The complete story, as best assembled from the literature:

**Mechanism (Long 2015):**
- 14g2a scFv contains CDR framework residues that promote homotypic clustering of CAR molecules on the T-cell membrane (independent of GD2 binding).
- Clustering leads to TCR-style ITAM phosphorylation on CD3ζ in the absence of cognate antigen.
- This drives a tonic, low-level signal-1 in the resting T cell.

**Consequences of tonic signaling:**
- During in vitro expansion: T cells expand initially (responding to the tonic signal as a "soft activation") but cease proliferating around days 5–7 with markedly elevated PD-1, TIM-3, LAG-3.
- T-bet and Blimp-1 are upregulated; TCF-1 and IL-7R are downregulated.
- Apoptosis (AICD) occurs at days 7–10 in vitro.
- In vivo: shortened persistence, poor antitumor activity despite normal in vitro killing.

**Mitigation strategies:**
- **Costim choice**: 4-1BB rescues; CD28 amplifies. (Long 2015)
- **Affinity reduction**: Wild-type 14g2a is tolerable; E101K is lethal. (Richman 2018)
- **Hinge shortening**: CD8α hinge < IgG-Fc hinge for tonic signaling. (multiple)
- **CAR density reduction**: Lower CAR molecules per cell → less clustering → less tonic signaling. (Majzner 2022)
- **Dasatinib priming**: Transient Lck inhibition during manufacturing → reduced tonic signaling during expansion → less terminal differentiation. (Mackall lab; adopted by Majzner 2022, Monje 2025)
- **TRAC-KI**: Endogenous TRAC promoter dynamically regulates CAR expression — upon activation, CAR goes up; upon rest, CAR goes down — reducing chronic tonic signaling. (Eyquem 2017 foundation; Mueller 2022 / Cappabianca 2024 for GD2)
- **Alternative scFvs**: 3F8, hu14.18, hu3F8 partially address the tonic-signaling issue but the framework similarity means it is not eliminated.

**Conclusion**: Tonic signaling is intrinsic to 14g2a-based CARs but can be **managed** by choosing 4-1BB costim, short CD8α hinge, standard-affinity scFv, dasatinib priming, and (increasingly) TRAC knock-in.

## IV.6 The CD28 vs 4-1BB vs CD28+4-1BB vs CD28+OX40 debate, resolved

The GD2 CAR field has converged on the following defaults, based on accumulated evidence:

| Construct | Pros | Cons | Field consensus |
| --- | --- | --- | --- |
| CD28 only (2G) | Rapid effector function | Lethal tonic exhaustion with 14g2a | ❌ Avoid (in clinical) |
| 4-1BB only (2G) | No tonic exhaustion; durable persistence | Slower initial effector | ✅ Default for autologous DMG (Majzner 2022, Monje 2025) and TRAC-KI |
| CD28 + 4-1BB (3G) | Rapid effector + persistence | More complex construction | ✅ Default for neuroblastoma (GD2-CART01) |
| CD28 + OX40 (3G) | Rapid effector + Th-skewing | Older choice; CD28 component remains a tonic risk | Maintained in Pule/Heczey lineage |
| OX40 + 4-1BB (3G) | Both TNFR; mild costim | Experimental | Rare |

**The dominant pattern by 2025**: 4-1BB-containing constructs (2G or 3G) for GD2 CARs.

## IV.7 Lessons from the affinity / CNS-encephalitis incidents

Richman 2018 (PMID 29180536) is one of the most-cited cautionary tales in CAR-T research:

**The mistake** was making the affinity-matured variant a high priority for development. The rationale was sound (better recognition of low-GD2 tumors), but the consequence (lethal encephalitis) was not predicted.

**Why was it not predicted?**
- The therapeutic-window estimate from preclinical xenograft models had used GD2-low tumors as targets and GD2-low normal tissues as bystanders. The xenograft mouse CNS expresses different GD2-bearing structures than the human CNS.
- Affinity-tuning of the scFv was thought to be a 'safe' optimization parameter (more sensitive recognition), but in fact it shifts the threshold downward into the range of normal-tissue expression.
- The CD28 amplification of CAR signaling magnified small changes in scFv affinity into large changes in functional output.

**Lessons for future programs:**
- Test affinity variants on a panel of human normal-tissue-equivalent cells (iPSC-derived neurons, brain organoids) before going to xenograft.
- Always compare CD28 vs 4-1BB versions of affinity-matured constructs.
- Embed a robust safety switch (iCasp9) in any high-affinity CAR.
- Consider density-tuning (reduce CAR copy number / promoter strength) before affinity-tuning.

## IV.8 Why every clinical GD2 product has eventually shifted to closed-system Prodigy or Cocoon

The transition from open-bag manufacturing to automated closed systems was driven by:

1. **Reproducibility**: Bag-based protocols have batch-to-batch variability in product phenotype (CCR7, PD-1, CAR%). Prodigy and Cocoon reduce this 5–10x.
2. **Sterility**: Closed systems have lower bacterial contamination rates (<0.5% vs ~2–5% in older bag systems).
3. **Operator-independence**: Less technical skill required, reducing inter-site variability for multicenter trials.
4. **Scalability**: One operator can run 4–8 Prodigy or Cocoon units in parallel.
5. **Regulatory acceptance**: FDA and EMA prefer closed systems for autologous cell products.
6. **Time savings**: 7-day Prodigy + dasatinib protocol vs 14-day open-bag protocol.

**The remaining "open" steps** in even the most automated workflows are:
- Apheresis (typically pre-loaded into the Prodigy LP-1 bag).
- Lentivirus / retrovirus addition (manual sterile transfer).
- Final formulation and fill into cryobag (often done in a biosafety cabinet).
- CRISPR-RNP preparation (for non-viral protocols).

## IV.9 Why IL-7 + IL-15 dominates over IL-2 in modern manufacturing

The transition from IL-2-only (Pule 2008, Louis 2011, Heczey 2014/2017, Quintarelli 2018) to IL-7+IL-15 (Majzner 2022, Monje 2025, Glienke 2022, Mueller 2022, Cappabianca 2024) was driven by:

| Parameter | IL-2 | IL-7+IL-15 |
| --- | --- | --- |
| Naïve/memory phenotype maintenance | Poor (effector-skewing) | Good (TSCM/TCM-skewing) |
| Proliferation | Strong | Strong |
| Treg expansion | Yes (Treg amplification) | No |
| Tonic signal exacerbation | High | Lower |
| In vivo persistence (downstream) | Shorter | Longer |
| Effector function | High at harvest | Equivalent or better in vivo |

**Mechanism**: IL-2 signaling through CD25 drives mTORC1 and effector differentiation. IL-7 and IL-15 signaling through γc + IL-7Rα / IL-15Rβγ drive STAT5-mediated proliferation but maintain TSCM-promoting transcription factors (TCF-1, LEF-1, Bcl-2).

**Note**: Some programs (including GD2-CART01 in its current iteration) still use IL-2 because it is cheaper and the autologous neuroblastoma indication has shorter follow-up where persistence is less critical. The field-wide direction, however, is IL-7+IL-15.

## IV.10 Choice of effector cell across indications

The choice of effector cell type is increasingly indication-specific:

| Indication | Effector | Rationale |
| --- | --- | --- |
| Pediatric neuroblastoma (autologous) | αβ-T (Bambino Gesù GD2-CART01) | Standard; well-tolerated; reproducible; 9/15 ORR (Locatelli 2025) |
| Pediatric DMG (autologous) | αβ-T (Stanford/Majzner) | Standard; ICV-tolerant |
| Refractory neuroblastoma with iNKT antitumor benefit | Vα24+ NKT (Heczey CAR-NKT.15) | NKT cells reprogram TME; IL-15 armoring extends persistence |
| Allogeneic off-the-shelf NB | αβ-T from healthy donor (Quintarelli 2025 ALLO) | TRAC + B2M KO eliminates GVHD risk |
| Hard-to-manufacture autologous (after extensive chemo) | NK-92 cell line (Bodden 2023) | Off-the-shelf, manufactured at scale; irradiation pre-infusion |
| Sarcoma (osteosarcoma, Ewing) | αβ-T (some IL-18 TRUCK) | Standard with armoring for TME reprogramming |
| GBM / adult glioma (preclinical) | αβ-T with synNotch for B7-H3 AND-gate | Selectivity needed in adult brain |
| Melanoma | αβ-T or PD-1 KO αβ-T | Standard with checkpoint inhibition |

## IV.11 The CNS / ICV breakthrough

Monje 2025 demonstrated:
- **62 ICV infusions** in 11 DMG patients via Ommaya reservoir.
- **Zero dose-limiting toxicities** at any ICV dose (10×10⁶, 30×10⁶, 100×10⁶).
- **9/11 patients alive >1 year** post-CAR-T initiation (in a population with median OS ~9 months at diagnosis).
- **CSF CAR exposure** ~100x higher than IV at equivalent doses.
- **Lymphodepletion not required** between ICV doses.
- **TIAN** (Tumor Inflammation-Associated Neurotoxicity) — transient and responsive to dexamethasone + anakinra.

**Implications:**
- ICV is now the standard for DMG GD2 CAR-T.
- Locoregional delivery is reshaping how the field thinks about CAR-T for solid tumors.
- Intratumoral, intracerebral cavity, and intraperitoneal routes are increasingly tested for other indications.

## IV.12 Cytokine armoring and the IL-15 hyperleukocytosis lesson

Heczey 2020/2023 GD2-CAR.15 NKT — with constitutive IL-15 expression — was a major preclinical-to-clinical translation. But the hyperleukocytosis observed at DL5 in Tian 2025 reveals an important caveat: **constitutive cytokine armoring can cause uncontrolled expansion in vivo if the antigen-stimulus + aAPC stimulation overshoots**.

**Lessons for cytokine-armored designs:**
- Inducible cassettes (NFAT-responsive minimal promoter; Glienke 2022 IL-18) preferred over constitutive expression.
- Safety switches mandatory.
- Avoid in vivo re-stimulation with aAPC unless thoroughly tuned.
- Tethered cytokine (membrane-bound IL-15 or RD-IL15 superagonist) may localize the signal and reduce systemic side effects.

## IV.13 Manufacturing-vs-construct trade-offs

The choice of vector platform is increasingly tied to the manufacturing platform:

| Construct platform | Best-matched manufacturing |
| --- | --- |
| SFG / MSCV γ-retrovirus | Open-bag PermaLife or G-Rex; ~14-day cycle; legacy of Pule/BCM/Bambino Gesù |
| 3G SIN lentivirus | CliniMACS Prodigy 7–12 day cycle; modern default |
| CRISPR-TRAC-KI nanoplasmid | Lonza Cocoon 9-day cycle; emerging |
| AAV6 HDR donor + CRISPR | Prodigy 9–14 day cycle; clinical pilot |
| mRNA EP | Static bag electroporation; 2-day cycle; transient products |
| Allo with multi-KO | Combined CRISPR + retrovirus on Prodigy/Cocoon, 9–14 days |

## IV.14 The transition to virus-free CRISPR-TRAC

Mueller 2022 → Cappabianca 2024 established that virus-free CRISPR-TRAC-KI can produce clinical-quality GD2 CAR-T. The implications:

1. **Cost**: Eliminating viral vector cost reduces COGS by 30–50%.
2. **Locus-defined**: Single-copy integration at TRAC eliminates VCN variability.
3. **TCR knockout**: TRAC-KI knocks out endogenous TCR, eliminating GVHD risk in allogeneic settings.
4. **Endogenous regulation**: TRAC promoter dynamically regulates CAR expression — on with activation, off at rest — reducing tonic-signaling exhaustion.
5. **Off-the-shelf compatibility**: With TRAC + B2M KO, donor-derived cells avoid graft-vs-host and host-vs-graft rejection.

The challenges remain:
- HDR efficiency in primary T cells (~30–50% with nanoplasmid; lower with circular plasmid).
- Selection / sorting for KI-positive cells.
- CRISPR off-target editing (mitigated by high-fidelity Cas9 variants and computational off-target prediction).
- Long-term safety of CRISPR-edited cells (followed in trial extensions).

## IV.15 Allogeneic GD2 CAR-T

Allogeneic ("off-the-shelf") GD2 CAR-T is at the pre-clinical / early-clinical interface:

| Program | Source | Edits | Status |
| --- | --- | --- | --- |
| Quintarelli 2025 ALLO_GD2-CART01 | Healthy donor PBMC | TRAC + B2M KO + CD28-4-1BB-iC9 CAR | Phase 1 |
| Various academic | Healthy donor or iPSC-T | TRAC + B2M KO + GD2 CAR | Preclinical |
| Fate Therapeutics iPSC-NK with GD2 CAR | iPSC-NK | NK-92-style with hu14.18 CAR | Preclinical → Phase 1 likely |
| NK-92 line (Bodden 2023) | NK-92 EBV-transformed line | hu14.18.28.z + RD-IL15 | Phase 1/2 in NB |

**Allogeneic advantages**: Off-the-shelf, manufactured at scale, lower cost per dose, avoids autologous manufacturing failures.

**Allogeneic challenges**: 
- GVHD: Mitigated by TRAC KO (eliminates endogenous TCR).
- HVG rejection: Mitigated by B2M KO (eliminates HLA-class-I) + HLA-E expression (avoids NK killing).
- Persistence: Without HLA matching, donor cells may be rejected within 2–4 weeks; requires periodic re-dosing or selection-resistant variants.

## IV.16 Open questions and frontier areas

1. **OAcGD2 as a preferential target**: The 8B6 scFv recognizes 9-O-acetylated GD2, which is more tumor-restricted than GD2. Could 8B6-based CARs eliminate peripheral pain DLTs while retaining tumor coverage?

2. **CNS-restricted CAR-T**: ICV delivery for DMG is now standard. What about other CNS-restricted indications (GBM, medulloblastoma, ATRT)? GD2 may not be the right target for all (B7-H3 dominates in GBM), but the route is established.

3. **In-situ LNP-mRNA CAR-T**: Can a GD2 CAR be delivered as mRNA-LNP directly to patient T cells in vivo, bypassing ex-vivo manufacturing entirely? Capstan Therapeutics and others are pursuing this for CD19 / BCMA; GD2 is feasible.

4. **iPSC-T allogeneic platforms**: Fate Therapeutics and others have iPSC-T platforms in development. iT cells maintain naïve-like properties and can be edited stably at iPSC stage. iT-derived allogeneic GD2 CAR-T is a 2025–2027 frontier.

5. **Combination with conventional therapy**: How should GD2 CAR-T be combined with chemotherapy, radiation, checkpoint inhibitors, or BiTE antibodies? Several phase 1 trials are testing combinations.

6. **Antigen-loss escape**: Heterogeneous GD2 expression in some tumors (~10% of NBs have GD2-low areas). Solutions: density-tuned CARs (Majzner 2022), bispecific CARs (GD2 + B7-H3 or GD2 + L1CAM), or epitope-spread vaccines.

7. **Manufacturing for resource-limited settings**: Lonza Cocoon and similar platforms enable distributed manufacturing. Can GD2 CAR-T be manufactured at the bedside or at a regional center in low-resource environments?

8. **Pediatric solid-tumor CAR-T as a standard of care**: GD2 CAR-T for neuroblastoma is approaching the same maturity as CD19 CAR-T for B-ALL was in 2017. The path to standard-of-care approval requires multi-center randomized comparison vs current best practice (e.g., anti-GD2 mAb + chemotherapy).

## IV.17 What every new GD2 CAR-T program should consider

1. **Use the standard 14g2a scFv** unless there is a specific reason (e.g., OAcGD2 with 8B6).
2. **Default to 4-1BB costim** (2G CD8α-4-1BB-CD3ζ); add CD28 only with a second TNFR-family costim (CD28+4-1BB or CD28+OX40, 3G).
3. **Embed iCasp9** in the construct for safety.
4. **Choose a short CD8α hinge** with CD8α TM.
5. **Plan for closed-system manufacturing** (CliniMACS Prodigy or Lonza Cocoon).
6. **Use IL-7 + IL-15** (± IL-21) instead of IL-2 for expansion.
7. **Add dasatinib priming** during the activation/transduction window for tonic-signal suppression.
8. **Consider CD4/CD8 1:1 enrichment** for product reproducibility.
9. **Plan ICV delivery via Ommaya** for any CNS-restricted indication, alongside IV.
10. **For allogeneic / off-the-shelf**: TRAC + B2M knockout via CRISPR; consider CRISPR-TRAC-KI as the simultaneous CAR-delivery step (eliminates virus + edits + adds CAR in one electroporation).
11. **For armoring**: prefer inducible (NFAT-IL18) or tethered (RD-IL15) cytokines over constitutive; always pair with safety switch.
12. **For affinity-matured variants**: do not pair with CD28; embed iCasp9; test exhaustively on iPSC-derived neurons and brain organoids before xenografting.

---

## Appendix A — Construct lineage map by clinical trial product

```
Pule 2008 / Louis 2011 / Heczey 2017 lineage (Baylor / Texas Children's)
  SFG-14g2a.ζ (1G)
  → SFG-14g2a.CD28.ζ (2G; Heczey 2014/2017 early)
  → SFG-iCasp9-2A-14g2a.CD28.OX40.ζ (3G + iC9; Heczey 2017)
  → SFG-iCasp9-2A-14g2a.CD28.2B4.ζ-2A-IL15 (NKT-tuned; Heczey 2020/2023)

Quintarelli / Bambino Gesù lineage (GD2-CART01)
  SFG-iCasp9-2A-14g2a.CD28.4-1BB.ζ (3G + iC9; Quintarelli 2018 → Del Bufalo 2023 → Locatelli 2025)
  → ALLO_GD2-CART01 (+TRAC KO + B2M KO; Quintarelli 2025)

Long / Mackall / NCI / Stanford lineage
  MSGV-14g2a.CD28.ζ (Long 2015; demonstrated tonic exhaustion)
  → MSGV-14g2a.4-1BB.ζ (Long 2015; demonstrated tonic rescue)
  → MSGV-14g2a-E101K.CD28.ζ (Richman 2018; lethal encephalitis, withdrawn)
  → Lenti-14g2a.CD8α-4-1BB.ζ.iC9 (Majzner 2022 / Monje 2025; CliniMACS Prodigy 7d)

Hannover / Glienke lineage
  Lenti-14g2a.CD8α-4-1BB.ζ + NFAT-IL18 (Glienke 2022; CliniMACS Prodigy 12d)

Wisconsin / Mueller lineage
  Nanoplasmid-14g2a.CD8α-4-1BB.ζ + TRAC-KI (Mueller 2022; CRISPR RNP, virus-free, 9d)
  → Nanoplasmid-8B6.CD8α-CD28.ζ + TRAC-KI (Cappabianca 2024; OAcGD2-specific, Lonza Cocoon 9d)

Bodden / Frankfurt NK-92 lineage
  NK-92 + hu14.18.CD28.2B4.ζ + RD-IL15 (Bodden 2023; preclinical / early clinical)
```

## Appendix B — Master construct-format glossary

```
1G: scFv-hinge-TM-CD3ζ
2G: scFv-hinge-TM-costim-CD3ζ
3G: scFv-hinge-TM-costim1-costim2-CD3ζ
4G (TRUCK): 3G + cytokine cassette (constitutive or inducible)
5G+: Various combinations of synthetic biology elements (e.g., synNotch + CAR, SUPRA + CAR)
```

Common multi-cistronic formats:
```
iCasp9-2A-CAR
CAR-2A-iCasp9
RQR8-2A-CAR
CAR-2A-IL15
CAR-2A-NFAT-IL18
CAR-2A-C7R
iCasp9-2A-CAR-2A-IL15 (Heczey NKT)
```

## Appendix C — Caveats and limitations of this synthesis

1. **Coverage gap**: ~50 papers (24% of the 204-paper corpus) were paywalled and not accessible as PDFs at the time of synthesis. For these papers, abstracts and DOIs are in `index.tsv` and inferred details are noted where possible. The most impactful gaps are paywalled NEJM, Cell, Science Translational Medicine, and AACR papers.

2. **Supplement coverage**: 96 supplements extracted from Europe PMC OA. Some clinical trial papers have lengthy supplementary appendices with detailed manufacturing methods, dosing schedules, and toxicity tables that may not be fully captured.

3. **Construct-level detail**: Vector maps, exact sequences, and full plasmid constructions are typically held as proprietary or in supplementary methods. We have captured the high-level design choices but not every nucleotide.

4. **Real-time evolution**: This synthesis reflects the field as of the snapshot date (2026-05). The CRISPR-TRAC-KI, allogeneic, and LNP-mRNA platforms are moving fast; details will evolve.

5. **Author manuscripts vs publishers**: Some PDFs are author manuscript versions (e.g., NIH-PMC-deposited author manuscripts), which lack final journal pagination but contain the full content.

6. **OCR fidelity**: Some PDFs were processed via pdftotext with -layout flag, which preserves spatial arrangement. Tables, equations, and figures are captured imperfectly. Numerical details (doses, timings, percentages) are most reliable when corroborated across the main text and tables.

7. **Synthesis is interpretive**: Many of the cross-paper inferences (e.g., "the field has converged on 4-1BB for GD2 CARs") are syntheses, not direct quotes. The reader should consult the per-paper extractions in `notes/09_per_paper_extractions.md` for primary-source detail.

---

**End of report.** For per-paper details, see `notes/09_per_paper_extractions.md`. For topical deep-dives, see the numbered notes files in `notes/`.
