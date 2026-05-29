# ILDR2-targeting antibodies and antibody-derived biologics

This is the antibody-centric heart of the collection. Three modalities have been built against ILDR2; all exploit the same fact — that ILDR2 delivers an **inhibitory** signal to T cells through its extracellular IgV domain — but in opposite directions.

| Modality | Reagent | Direction | Intended indication | Lead refs |
| --- | --- | --- | --- | --- |
| Fc fusion (agonist/decoy) | **ILDR2-Fc** (ILDR2 ectodomain + Ig Fc) | *Engages* the inhibitory axis → suppresses T cells, induces tolerance | Autoimmunity, transplantation | PMID 29431694, 29431690 |
| Antagonist mAb | **BAY 1905254** (Bayer), human/mouse/monkey cross-reactive anti-ILDR2 **hIgG2** | *Blocks* ILDR2 → relieves T-cell suppression | Cancer immunotherapy | PMID 32312711 |
| Research / tool mAb | anti-mouse-ILDR2 mAb; anti-angulin-3/ILDR2 mAb | Detection / flow / IHC | Reagent | PMID 39626366, 38311119 |

---

## 1. ILDR2-Fc fusion protein (agonist / tolerogenic decoy)

**Construct.** A soluble fusion of the **ILDR2 extracellular (IgV) domain** to an **immunoglobulin Fc** fragment. It binds a putative ILDR2 counter-receptor on activated T cells and reproduces the inhibitory signal in *trans* (PMID 29431694).

**Mechanism (PMID 29431694, 29431690).**
- ILDR2-Fc inhibits early TCR signaling and **suppresses CD4+ and CD8+ T-cell activation** driven by anti-CD3/anti-CD28 in both mouse and human cells — **without increasing T-cell apoptosis** (it is anti-proliferative/anergizing, not deleting).
- It abrogates pro-inflammatory cytokine/chemokine production in autologous synovial-like macrophage + cytokine-stimulated-T-cell cocultures.
- Its durable benefit is driven by **regulatory T cell (Treg) induction** and re-establishment of **antigen-specific tolerance**, not just transient immunosuppression — short-term dosing yields long-term effects.

**Efficacy across autoimmune / transplant models.**
- **Collagen-induced arthritis (CIA / rheumatoid arthritis model)** — beneficial (PMID 29431694).
- **Relapsing-remitting experimental autoimmune encephalomyelitis (EAE / multiple sclerosis model)** — durable benefit from short-term treatment (PMID 29431690).
- **NOD type 1 diabetes** — durable benefit (PMID 29431690).
- **Minor-mismatch bone-marrow transplantation** — promotes engraftment (PMID 29431690).

**Provenance.** This program traces to **Compugen** (the predicted-protein-discovery group: Hecht, Toporik, Vaknin, Cojocaru et al.; PMID 29431694) with the tolerance pharmacology led by **Podojil & Miller** (PMID 29431690). The "unique mode of action" framing — combining immunomodulation, restoration of immune homeostasis, and antigen-specific tolerance via Tregs — is the program's central claim.

---

## 2. BAY 1905254 — antagonist anti-ILDR2 monoclonal antibody (oncology)

The single most important "ILDR2 antibody" in the corpus (PMID 32312711; main text paywalled, summarized here from the abstract and the B7-family review PMID 34639059).

**Antibody.** **BAY 1905254** is a **human/mouse/monkey cross-reactive anti-ILDR2 human IgG2 monoclonal antibody**, engineered by Bayer specifically to **block the immunosuppressive activity of ILDR2** for cancer immunotherapy. The cross-species reactivity is deliberate: it lets the same molecule be used in mouse efficacy studies and in primate tox/clinical development.

**Target-expression rationale.** Beyond the previously reported expression on immune and immune-privileged/inflamed tissues, the Bayer group found ILDR2 on **fibroblastic reticular cells (FRCs)** in the lymph-node stroma — the T-cell-zone cells responsible for recruiting naïve T cells and activated dendritic cells. This places ILDR2 at a site where it can gate T-cell priming.

**Pharmacology (PMID 32312711).**
- Promotes **T-cell activation in vitro**.
- Enhances **antigen-specific T-cell proliferation and cytotoxicity in vivo** in mice.
- Single-agent efficacy across **multiple syngeneic mouse tumor models**, with response **correlating with tumor mutational load** (consistent with a neoantigen-dependent, T-cell-mediated mechanism).
- **Additive-to-synergistic** combination effects with **anti-PD-L1**, with an **immunogenic-cell-death-inducing chemotherapeutic (docetaxel)**, and with **tumor-antigen immunization** (PMID 32312711, 34639059).

**Positioning.** BAY 1905254 is the inverse of ILDR2-Fc: where the Fc decoy *feeds* the inhibitory axis to calm autoimmunity, the antagonist mAb *cuts* it to unleash anti-tumor T cells — the canonical checkpoint-inhibitor logic, extended to a newer B7-family member.

---

## 3. Research / tool monoclonal antibodies against ILDR2

Two papers report newly generated mAbs used as **detection reagents** rather than therapeutics — useful both as off-the-shelf tools and as evidence of cell-surface ILDR2.

- **Anti-mouse-ILDR2 mAb (PMID 39626366).** A monoclonal specific to mouse ILDR2 was developed to show, by flow cytometry, that a **CD206hi macrophage** subset in the **sublingual mucosa** expresses **cell-surface ILDR2**. These CD206hiILDR2+ macrophages are M2-skewed, down-regulate pro-inflammatory genes, expand with repeated antigen exposure, and preferentially induce **Foxp3+ Tregs** — implicating macrophage-surface ILDR2 in mucosal/sublingual-immunotherapy tolerance. This is direct in-vivo confirmation that ILDR2 is presented at the cell surface on a defined tolerogenic myeloid population.
- **Anti-angulin-3/ILDR2 mAb (PMID 38311119).** A newly established monoclonal antibody against **angulin-3 (ILDR2)** was used to map its localization in podocytes: confined to tricellular junctions in primordial podocytes, then transiently bicellular as foot-process interdigitation develops. The mAb detects **podocyte injury** by its relocalization — a tissue-pathology readout rather than an immunotherapeutic.

---

## Cross-cutting observations

- **One IgV domain, two drug logics.** Every ILDR2 biologic acts on the same extracellular IgV checkpoint module; the therapeutic direction is set by whether you supply the ligand (Fc decoy) or remove it (antagonist mAb).
- **The counter-receptor is still "putative."** Both the Compugen and Bayer papers describe binding to a *putative* ILDR2 receptor on activated T cells; the corpus does not contain a definitive co-receptor identification. This is the main open question for the antibody program.
- **Cross-species engineering matters.** BAY 1905254's human/mouse/monkey cross-reactivity is what enabled syngeneic-model efficacy testing of a clinical-intent antibody — a recurring requirement for B7-family mAbs.
- **Tumor-mutational-load dependence** of BAY 1905254 efficacy, plus PD-L1/chemo/vaccine synergy, frames ILDR2 blockade as a *combination-partner* checkpoint rather than a standalone replacement for PD-(L)1.
