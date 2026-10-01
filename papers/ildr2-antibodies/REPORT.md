# Antibodies and Biologics Targeting ILDR2 — Consolidated Synthesis

A single-file synthesis of the published literature on **ILDR2 (immunoglobulin-like domain containing receptor 2)** as an antibody target, consolidating the topical notes in `notes/` over the 21-paper corpus in `index.tsv`.

## Executive summary

ILDR2 is a **B7-family immune-checkpoint protein** with a single extracellular Ig V-set domain that delivers an inhibitory signal to activated T cells (PMID 29431694). Because the axis is inhibitory, it has been drugged in **both directions**:

- **Engage it** with an **ILDR2-Fc fusion** to induce antigen-specific tolerance for **autoimmunity / transplantation** (PMID 29431694, 29431690).
- **Block it** with an **antagonist anti-ILDR2 monoclonal antibody, BAY 1905254 (Bayer)**, to relieve T-cell suppression for **cancer immunotherapy** (PMID 32312711).

Research/tool mAbs against mouse ILDR2 and against angulin-3/ILDR2 round out the antibody set (PMID 39626366, 38311119). The remaining literature is **target biology**: ILDR2 is simultaneously a **tricellular-tight-junction "angulin-3" protein** and a **pancreatic-β-cell / hepatic-lipid diabetes modifier**, and its surface level is stabilized by the ER chaperone **GRP78** (PMID 33863978).

## Corpus and methods

- 42 unique PubMed records from 17 alias/topic queries → **21 included** (7 core, 14 context) after removing LISCH7/LSR (different gene) and incidental gene-list hits.
- 12/21 PDFs archived; 9 paywalled or reCAPTCHA/Cloudflare-blocked (see `README.md`).
- Full identification strategy and the complete excluded list are below.

## Glossary

- **ILDR2 / C1orf32 / LISCH-like / angulin-3** — the same gene/protein under four names.
- **LISCH7 / LSR / angulin-1** — a *different*, paralogous gene (do not conflate).
- **B7 family** — immunomodulatory Ig-superfamily ligands (CD80/86, PD-L1/L2, B7-H3/H4, ICOS-L, …) to which ILDR2 was added.
- **ILDR2-Fc** — soluble ILDR2 ectodomain fused to Ig Fc; agonistic/tolerogenic.
- **BAY 1905254** — antagonist anti-ILDR2 hIgG2 mAb.
- **FRC** — fibroblastic reticular cell (lymph-node stroma).

---

## Part I — ILDR2 as an antibody target (target biology)

**Architecture.** Type I transmembrane, 639 aa: signal peptide → IgV ectodomain (~167 aa) → TM → ~433-aa cytoplasmic tail; gene at Chr1q23–25; ~94% mouse/human identity; ~24–36% B7-family ectodomain homology (PMID 34639059). Paralogs ILDR1 and LSR; together the **angulins** (PMID 23239027, 28785060).

**Expression relevant to dosing.** CD56+ lymphocytes, monocytes/macrophages (PMID 34639059); lymph-node **FRCs** in the T-cell zone (PMID 32312711); surface ILDR2 on **CD206hi sublingual macrophages** (PMID 39626366); **podocytes** complexed with **CLDN5** (PMID 39640577); islets/liver from the original genetics (PMID 18654634, 23826244).

**Regulation / interactome.** **GRP78 + PDIA1** bind ILDR2; **GRP78 stabilizes it by blocking ubiquitin–proteasome degradation**, ER-stress-responsive (PMID 33863978) — implying tunable surface target density. **ZNF70** links ILDR2 to **HES1** (PMID 27353377). Angulin family members bind splicing factors TRA2A/TRA2B/SRSF1 (PMID 28785060).

**Non-immune "day jobs"** (sources of potential on-target/off-tumor effects): tricellular tight-junction barrier / tricellulin recruitment, deafness, inner ear (PMID 23239027, 24790043, 27195292); podocyte filtration barrier and injury reporting (PMID 38311119, 39640577); β-cell mass / diabetes and hepatic lipid handling, with the steatosis claim later walked back (PMID 18654634, 23826244, 29847571). Structural insight into the angulin binding interface comes from angubindin-1 alanine scanning (PMID 40928054).

## Part II — The agonist arm: ILDR2-Fc (tolerance / autoimmunity)

ILDR2-Fc presents the inhibitory IgV ectodomain in *trans*, binding a **putative counter-receptor on activated T cells**. It inhibits early TCR signaling and CD4/CD8 activation **without inducing apoptosis** (PMID 29431694). Short-term dosing produces **durable, antigen-specific tolerance via Treg induction** across **CIA/RA, relapsing-remitting EAE, NOD type-1 diabetes, and minor-mismatch BMT** (PMID 29431694, 29431690). This is the Compugen-origin program; its claimed differentiator is combined immunomodulation + homeostasis restoration + tolerance, rather than blunt immunosuppression.

## Part III — The antagonist arm: BAY 1905254 (oncology)

**BAY 1905254** is a **human/mouse/monkey cross-reactive anti-ILDR2 hIgG2** mAb built to **block** ILDR2's immunosuppression (PMID 32312711). Cross-species reactivity enables syngeneic-model testing of a clinical-intent antibody. It:
- promotes T-cell activation in vitro and **antigen-specific proliferation/cytotoxicity in vivo**;
- is efficacious as monotherapy across **syngeneic tumor models, with response correlating with tumor mutational load**;
- shows **additive/synergistic** activity with **anti-PD-L1**, **docetaxel (immunogenic cell death)**, and **tumor-antigen immunization** (PMID 32312711, 34639059).

It is the mechanistic inverse of ILDR2-Fc and is positioned as a **combination-partner checkpoint** rather than a PD-(L)1 replacement.

## Part IV — Research / tool antibodies

- **Anti-mouse-ILDR2 mAb** — demonstrates surface ILDR2 on tolerogenic CD206hi sublingual macrophages that drive Foxp3+ Tregs (PMID 39626366).
- **Anti-angulin-3/ILDR2 mAb** — maps podocyte localization and detects injury by tricellular→bicellular redistribution (PMID 38311119).

## Part V — Cross-cutting analysis and open questions

1. **Unidentified counter-receptor.** Both therapeutic programs describe a *putative* ILDR2 receptor on activated T cells; no definitive co-receptor is reported in this corpus. This is the central mechanistic and biomarker gap.
2. **One epitope, two drugs.** All biologics act on the same IgV ectodomain; therapeutic direction is set by supplying (Fc) vs. removing (mAb) the signal.
3. **Target-density is regulated.** GRP78/ER-stress control of ILDR2 stability (PMID 33863978) suggests microenvironment-dependent target availability for antibody binding.
4. **On-target/off-tumor risk.** ILDR2's junctional roles in cochlea, kidney podocytes, and islets warrant attention for systemic antagonist dosing.
5. **Combination-first oncology positioning.** Mutational-load dependence and PD-L1/chemo/vaccine synergy define the likely clinical development path for ILDR2 blockade.
6. **Clinical-stage data are not in the indexed literature.** The corpus is preclinical/mechanistic; trial-readout papers for BAY 1905254 were not retrieved by these queries as of the corpus date and remain a watch item.

---

## Appendix A — Identification strategy

17 PubMed E-utils queries (gene symbol + all aliases + antibody/checkpoint/biology angles; see `README.md`) → 42 unique records → manual title/abstract filtering → 21 included. PMC/DOI resolved via NCBI ID Converter + Europe PMC; PDFs from Europe PMC OA, PLOS, Nature, MDPI (Europe PMC render).

## Appendix B — Excluded records

**LISCH7 / LSR (different gene):** PMID 11402317, 15731461, 17975147, 18456845, 32048750, 34238140.

**Incidental gene-list / omics mentions (ILDR2/C1orf32 not a subject):** PMID 24212375, 27034888, 28709640, 29494550, 32661289, 36147669, 36557314, 36530149, 37325559, 38437001, 40003915, 41285811, 41518986, 41865132, 42137783.
