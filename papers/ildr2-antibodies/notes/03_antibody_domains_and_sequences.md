# ILDR2 antibodies — the set, the domain(s) they target, and their exact sequences

This note answers three questions about the antibody/biologic programs in this collection:
1. **What is the set of antibodies?** (inventory)
2. **Which domain of ILDR2 does each target?** (epitope/domain mapping)
3. **What are the exact amino-acid sequences?** (variable domains + CDRs, with source attribution)

All sequences extracted here are written to [`../data/sequences/ildr2_antibody_sequences.fasta`](../data/sequences/ildr2_antibody_sequences.fasta).

---

## 0. The target: ILDR2 domain architecture (UniProt Q71H61, human, 639 aa)

ILDR2 is a **type I single-pass transmembrane protein**. There is exactly **one** folded module outside the cell, so every cell-surface-directed binder must engage it.

| Region | Residues | Length | Notes |
| --- | --- | --- | --- |
| Signal peptide | 1–20 | 20 | Cleaved; `MDRVLLRWISLFWLTAMVEG` |
| **Extracellular / lumenal** | **21–186** | **166** | The only ectodomain — contains the IgV module |
| ↳ **Ig-like V-type (IgV) domain** | **21–162** | 142 | The B7-family checkpoint module; the functional binding target |
| Transmembrane helix | 187–207 | 21 | `…WVFVGLVLLGVFLFFVLVGIC…` |
| **Cytoplasmic tail** | **208–639** | 432 | Very long, intrinsically disordered; signaling/tight-junction interactions |

**Key consequence for "which domain":** ILDR2 has a single IgV ectodomain (21–186). All therapeutic/surface antibodies — agonist Fc-fusion *and* antagonist mAbs — necessarily act on **this same IgV ectodomain**. There is no second extracellular domain to choose between. The large (432 aa) **cytoplasmic tail** is only accessible to antibodies used on permeabilized/denatured material (Western blot, some IHC), i.e. the tight-junction / "angulin-3" detection reagents.

---

## 1. The set of antibodies (inventory)

| # | Reagent / clone | Developer | Format | Direction | Target region | Sequence public? | Primary source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **ILDR2-Fc** (CGEN-15001-type) | Compugen | ILDR2 ectodomain–Ig Fc fusion | Agonist (engages inhibitory axis → tolerance) | Its **own** IgV ectodomain is the active moiety; binds a putative T-cell counter-receptor | Partial (construct = ectodomain + Fc) | PMID 29431694, 29431690; pat. EP3202415B1 / EP2769729B1 |
| 2 | **BAY 1905254** = clone **59-08.B02** | Bayer | Human **IgG2**, κ | Antagonist (blocks ILDR2 suppression) | IgV ectodomain (21–186) | **Yes — full VH/VL + 6 CDRs** | PMID 32312711; **US11655297B2** |
| 3 | Bayer clones **61-02.C05, 56-02.E08, 74.15.G09, 56.02.E10** | Bayer | Human IgG2, κ | Antagonist (siblings of BAY 1905254) | IgV ectodomain | **Yes — full VH/VL + 6 CDRs each** | **US11655297B2** |
| 4 | Compugen anti-C1orf32/ILDR2 mAbs (≥3 clones) | Compugen | Murine mAb (VH/VL disclosed) | Anti-ILDR2 (oncology/tool) | IgV ectodomain | **Yes — VH/VL + 6 CDRs (2 clones), VH (1 clone)** | **US9617336B2** |
| 5 | Academic anti-ILDR2 (murine + **humanized**) | Sichuan University | Murine then humanized IgG | Anti-ILDR2 | IgV ectodomain | **Yes — VH/VL** | CN118459591A, CN121471357A |
| 6 | anti-mouse-ILDR2 mAb | Sultana et al. 2025 | Mouse-reactive mAb (tool) | Detection (flow/surface) | Ecto (cell-surface ILDR2) | **No public sequence** | PMID 39626366 |
| 7 | anti-angulin-3 / ILDR2 mAb | Higashi et al. 2024 | Tool mAb (IHC/WB) | Detection | Likely cytoplasmic/full antigen | **No public sequence** | PMID 38311119 |

> C1orf32 is the original gene name for ILDR2, so the Compugen "C1ORF32 antibodies" patent (US9617336B2) is an anti-ILDR2 patent.

---

## 2. Domain / epitope targeting — what the literature actually pins down

- **All four therapeutic/surface programs (ILDR2-Fc, BAY 1905254 + siblings, Compugen mAbs, Sichuan mAbs) target the IgV ectodomain (21–186)** — this is forced by the architecture (only one extracellular domain) and confirmed by the functional read-outs (they modulate the T-cell-suppressive checkpoint signal that lives in the ectodomain).
- **No paper or patent in the corpus reports a fine-mapped epitope** (no alanine scan, no co-crystal residues) for any of these antibodies. "Which domain" therefore resolves to the IgV domain for every functional binder; sub-domain epitopes are **not disclosed**.
- **The counter-receptor / ligand on T cells remains "putative"** — ILDR2-Fc's mechanism is described as engaging an unidentified partner; this is unresolved in the corpus.
- **BAY 1905254 is deliberately human/mouse/monkey cross-reactive**, which implies its epitope lies in a region of the IgV domain conserved across those species.
- The **angulin-3 / tight-junction detection mAb** (Higashi 2024) is the one reagent that may recognize a non-IgV region (the cytoplasmic tail or full denatured antigen), consistent with its use as a histology/blot reagent rather than a surface blocker.

---

## 3. Exact sequences

### 3.1 ILDR2 antigen (the thing all of them bind) — UniProt Q71H61
- **Mature ectodomain (residues 21–186)** — the antibody/Fc target:
```
LQVTVPDKKKVAMLFQPTVLRCHFSTSSHQPAVVQWKFKSYCQDRMGESLGMSSTRAQSL
SKRNLEWDPYLDCLDSRRTVRVVASKQGSTVTLGDFYRGREITIVHDADLQIGKLMWGDS
GLYYCIITTPDDLEGKNEDSVELLVLGRTGLLADLLPSFAVEIMPE
```
- Full 639-aa precursor and the IgV domain (21–162) are in the FASTA.

### 3.2 BAY 1905254 — Bayer anti-ILDR2 hIgG2/κ (clone **59-08.B02**)
Source: **US11655297B2** ("ILDR2 antagonists and combinations thereof"; family also WO2019105972A1 / EP3717007B1; CN111655287A). Isotype confirmed human **IgG2** by the constant region (IgG2 hinge `…CCVECPPCPAPP…`) and human **κ** light chain.

**CDRs (Kabat-style, as named in the patent):**

| | HCDR1 | HCDR2 | HCDR3 | LCDR1 | LCDR2 | LCDR3 |
| --- | --- | --- | --- | --- | --- | --- |
| **59-08.B02 / BAY 1905254** | SYAIS | GIIPILGIANYAQKFQG | ARGRLPYGDFWDS | RSSQSLLYSNGYNYLD | LGSNRAS | MQALQTPLT |

**VH (SEQ ID NO:7):**
```
QVQLVQSGAEVKKPGSSVKVSCKASGGTFSSYAISWVRQAPGQGLEWMGGIIPILGIANY
AQKFQGRVTITADKSTSTAYMELSSLRSEDTAVYYCARGRLPYGDFWDSWGQGTLVTVSS
```
**VL (SEQ ID NO:8):**
```
DIVMTQSPLSLPVTPGEPASISCRSSQSLLYSNGYNYLDWYLQKPGQSPQLLIYLGSNRA
SGVPDRFSGSGSGTDFTLKISRVEAEDVGVYYCMQALQTPLTFGGGTKLEIR
```
Full-length heavy chain (VH + human IgG2 constant, SEQ ID NO:42) and light chain (VL + human κ constant, SEQ ID NO:43) are reproduced in the FASTA. *Caveat:* the full-length chains are transcribed from the Google-Patents rendering and contain a few OCR artifacts in the **constant region only** (e.g. `VFPLAP`→`VEPLAP`, `VLQSSG`→`VLOSSG`); the **variable domains and CDRs above are clean**. Verify the formal sequence listing of US11655297B2 before any wet-lab use.

### 3.3 Other Bayer anti-ILDR2 clones (same patent, same hIgG2/κ scaffold)

| Clone | HCDR3 | LCDR3 | VH SEQ ID | VL SEQ ID |
| --- | --- | --- | --- | --- |
| 61-02.C05 | DFVGVLPDAFDI | QQYHIPPPS | 9 | 10 |
| 56-02.E08 | AIGEPFDY | MQALQTPLT | 11 | 12 |
| 74.15.G09 | AKESPSVGLGSYYDFWSGLYGMDV | QQYDDSGIT | 13 | 14 |
| 56.02.E10 | EGIAAPGSGYYYGMDV | CSYTGTTVI | (HC 50) | — |

Full VH/VL sequences for each are in the FASTA.

### 3.4 Compugen anti-C1orf32/ILDR2 mAbs (murine) — US9617336B2
Variable regions are rendered **with their leader peptides**; CDRs below are the bolded patent CDRs.

| Clone | HCDR1 | HCDR2 | HCDR3 | LCDR1 | LCDR2 | LCDR3 |
| --- | --- | --- | --- | --- | --- | --- |
| A (SEQ 40/42) | AYTFTDYSMH | WINTETGEPTYAGDFKG | AGYYDYFDY | KASQDVVTAVA | WASNRHT | QQYSSYPLT |
| B (SEQ 56/58) | GFTFSDYYMY | YISNGGGSTYYPDTVKG | QGYYYGSSPFAY | KASQDVSTAVA | SASYRYT | QQHYSTPYT |
| C (SEQ 72, VH only) | GFSLSSSYMGVG | HIWWDDVKRYNPALKS | (GR)IDRHYFDY | — | — | — |

Full VH/VL sequences in the FASTA.

### 3.5 Academic anti-ILDR2 (Sichuan University) — CN118459591A (murine), CN121471357A (humanized)
The humanized antibody and its murine parent share the same CDRs; representative humanized variable domains:
- **Humanized VH:** `QVQLVQSGAEVKKPGASVKVSCKASGYTFTSYTIHWVRQAPGQGLEWMGFINPSSEYTEYNQNFKDRVTMTRDTSTSTVYMELSSLRSEDTAVYYCARSTTVAFDYWGQGTLVTVSS` (HCDR3 = ARSTTVAFDY)
- **Humanized VL:** `DIQMTQSPSSLSASVGDRVTITCRASGNIHNYLAWYQQKPGKAPKLLIYNAKTLADGVPSRFSGSGSGTDFTLTISSLQPEDFATYYCQHFWSTVTFGGGTKVEIK`

### 3.6 ILDR2-Fc fusion (Compugen) — EP3202415B1 / EP2769729B1
This is **not an antibody**; it is the **ILDR2 ectodomain fused to an immunoglobulin Fc**. The "active" sequence is therefore the ILDR2 ectodomain in §3.1, fused N-terminally to an Fc (the patents describe the C1orf32 ectodomain variant `H19011_1_P8`, SEQ ID NO:4, joined to Fc). The exact published junction/linker and Fc isotype of the specific therapeutic lot are **not cleanly disclosed** as a single sequence in the open literature; for practical purposes the molecule = `ILDR2(21–186) + (linker) + Ig Fc`.

### 3.7 Tool mAbs with no public sequence
- **anti-mouse-ILDR2 mAb** (Sultana et al. 2025, PMID 39626366) — newly raised; **no VH/VL deposited**.
- **anti-angulin-3/ILDR2 mAb** (Higashi et al. 2024, PMID 38311119) — detection reagent; **no VH/VL deposited**.

---

## 4. Bottom line

- **Domain question:** there is only one ILDR2 ectodomain (the IgV module, residues 21–186), and **every functional ILDR2 antibody/biologic in the corpus targets it**; no finer epitope is disclosed. Only denaturing detection reagents could touch the 432-aa cytoplasmic tail.
- **Sequence question:** exact, usable variable-domain + CDR sequences **are public** for **BAY 1905254 and four sibling Bayer clones** (US11655297B2), for **two-to-three Compugen murine clones** (US9617336B2), and for a **humanized academic antibody** (Sichuan University). The **ILDR2-Fc** sequence is defined by the ILDR2 ectodomain + Fc but the precise therapeutic construct is only partially disclosed. The two **tool mAbs** (Sultana 2025, Higashi 2024) have **no public sequences**.
