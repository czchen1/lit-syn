# ILDR2 target biology (what the antibodies bind)

Context for the antibody program: what ILDR2 is, where it is expressed, what it interacts with, and the two non-immune functions (tricellular tight junctions; β-cell/lipid metabolism) that defined the gene before its checkpoint role was known.

## 1. Domain architecture and family

- **Type I transmembrane protein, 639 aa** (human): signal peptide → extracellular **Ig V-set (IgV) domain (~167 aa)** → TM (~20 aa) → long intracellular tail (~433 aa) (PMID 34639059).
- Gene `ILDR2` / `C1orf32`, human **Chr1q23–25**; ~94% identity between human and mouse orthologs; ~24–36% homology of the ectodomain to other B7-family members (PMID 34639059).
- **Angulin family:** ILDR2 = **angulin-3**; paralogs **ILDR1 (angulin-2)** and **LSR (angulin-1, "LISCH7")** (PMID 23239027, 28785060). The single IgV domain is the shared structural unit and the antibody epitope surface.

## 2. Expression

- Protein detected on **CD56+ lymphocytes**, **monocyte-derived macrophages**, and **CD16+ monocyte subsets**; mRNA high in brain and ovary, low in intestine/heart/kidney (PMID 34639059).
- On **fibroblastic reticular cells (FRCs)** in the lymph-node T-cell zone (PMID 32312711) — relevant to where ILDR2 can gate T-cell priming.
- On a **CD206hi M2 macrophage subset in sublingual mucosa**, at the cell surface, expanding with repeated antigen exposure (PMID 39626366).
- In **kidney podocytes**, strongly co-localized with the podocyte-specific claudin **CLDN5** (PMID 39640577).
- Originally noted in **pancreatic islets / β-cells** and **liver** (PMID 18654634, 23826244).

## 3. Interactome and protein regulation

- **GRP78 (HSPA5) and PDIA1** — ER-resident chaperones identified as ILDR2-interacting proteins in MIN6 β-cells; **GRP78 stabilizes ILDR2 by inhibiting its ubiquitin–proteasome degradation**, and GRP78 rises with ER stress (PMID 33863978). This couples ILDR2 surface levels to the unfolded-protein response.
- **ZNF70** — an ILDR2-interacting zinc-finger protein that contributes to regulation of **HES1** gene expression (PMID 27353377).
- **CLDN5** — direct interaction in podocytes by co-immunoprecipitation (PMID 39640577).
- **Splicing factors (family-level):** the related angulins ILDR1 and LSR bind TRA2A/TRA2B/SRSF1 and modulate alternative pre-mRNA splicing, translocating to the nucleus when those factors are present — establishing a non-junctional nuclear role for the angulin family that may extend to ILDR2 (PMID 28785060).

## 4. Tricellular tight junction / angulin-3 function

- Angulins (LSR, ILDR1, ILDR2) localize to **tricellular contacts** and **recruit tricellulin** to build the tricellular tight junction (tTJ); this barrier function is implicated in **deafness pathogenesis** (PMID 23239027).
- Reviews of tTJ molecular organization and of tTJs in the **inner ear** place ILDR2/angulin-3 in the barrier-protein context (PMID 24790043, 27195292).
- Comparative physiology: angulin transcripts (incl. `ildr2`) track barrier development in **rainbow-trout gill epithelium** (PMID 29631364).
- **Structure / binding determinants:** alanine-scanning of **angubindin-1** (a *Clostridium perfringens* iota-toxin fragment that binds angulin-1/-3 to modulate tTJs) identifies the residues required for angulin binding — relevant to engineering tTJ-binding molecules and to the ILDR2/angulin-3 binding interface (PMID 40928054).
- **Kidney:** angulin-3/ILDR2 is confined at podocyte tricellular junctions, transiently relocates to bicellular junctions during foot-process maturation, and its **redistribution reports podocyte injury** (PMID 38311119); ILDR2 knockdown/role studies tie it to glomerular filtration and glomerulopathies (PMID 39640577).

## 5. Metabolic / diabetes origin of the gene

- **Positional cloning of "Lisch-Like"** (PMID 18654634): in B6.DBA congenic mice a distal-Chr1 QTL for diabetes phenotypes (blood glucose, HbA1c, islet histology) was refined to a 1.8-Mb interval; the implicated gene (later `Ildr2`) associated with **reduced β-cell replication and mass** and mild hypoinsulinemic hyperglycemia. This is the molecule's first functional identity.
- **ER-resident regulator of hepatic lipid homeostasis** (PMID 23826244): transient Ildr2 overexpression relieves hepatic steatosis in ob/ob mice.
- **Negative-control / walk-back** (PMID 29847571): Cre-mediated liver-specific Ildr2 knockout did **not** reproduce steatosis, indicating "a negligible role in hepatic steatosis" and that earlier shRNA phenotypes were likely off-target — a useful caution when interpreting ILDR2 loss-of-function.
- **Genetics context:** the diabesity-genetics review (PMID 24752583) situates Ildr2/Lisch-Like among polygenic obesity-T2D modifier loci.

## 6. Why this matters for the antibodies

- The **IgV ectodomain** is both the functional checkpoint module and the antibody epitope; ILDR2-Fc presents it, BAY 1905254 blocks it, and the tool mAbs detect it.
- **GRP78-dependent stabilization** (PMID 33863978) implies that ILDR2 surface density — and thus antibody target availability — may be **ER-stress-modulated**, a tumor-microenvironment-relevant variable.
- ILDR2's **dual life** (immune checkpoint *and* tight-junction/β-cell protein) flags potential **on-target, off-tumor** considerations (junctional epithelia, islets, podocytes) for systemic anti-ILDR2 therapy.
- The **counter-receptor on activated T cells remains unidentified** in this corpus — the key missing piece for mechanistic and biomarker work.
