# γδ T cell biology and subsets

## Lineage and ontogeny

γδ T cells develop in the thymus from the same progenitors as αβ T cells, diverging at the β‑selection checkpoint when a productive γ and δ TCR rearrangement is made instead of (or before) a β chain. They are exported as comparatively "pre‑programmed" effectors and seed both the circulation and — heavily — epithelial and mucosal tissues (gut, skin, liver, lung, reproductive tract). In adult human blood they are usually 1–10% of T cells; in gut epithelium and liver they can be a much larger fraction.

A central organizing idea in the modern literature is that γδ T cells span a spectrum from **innate‑like** (rapid, TCR‑semi‑independent, NK‑receptor‑driven) to **adaptive‑like** (clonally focused, antigen‑experience‑shaped, memory‑forming). Subset usage maps loosely onto this axis.

## The δ‑chain framework

Human γδ cells are most usefully classified by their TCR **δ chain**:

### Vγ9Vδ2 (a.k.a. Vγ2Vδ2)
- The **dominant blood subset** (often 50–95% of circulating γδ cells in adults).
- **Innate‑like and phosphoantigen‑reactive**: activated by small pyrophosphate metabolites (microbial **HMBPP**; host **IPP** from the mevalonate pathway) sensed via BTN3A1/BTN2A1 (see `02_antigen_recognition.md`).
- Easily and selectively expanded ex vivo with **aminobisphosphonates + IL‑2** or synthetic phosphoantigens (BrHPP), which is why essentially all first‑generation γδ immunotherapy used this subset.
- Potent IFN‑γ producers and cytotoxic effectors; express NKG2D, DNAM‑1, and (when induced) CD16.

### Vδ1
- **Tissue‑resident / "adaptive‑like."** Enriched in epithelium, gut, liver, and within many solid tumors; expands and clonally focuses with age and chronic stimulation (notably CMV).
- Recognizes stress ligands and lipid/antigen contexts more than phosphoantigens; generally **NKG2D‑ and NKp30/NKp44‑driven**.
- Harder to expand selectively, but protocols now exist (**Delta One T / DOT cells**; OKT3 + cytokine combinations) — making Vδ1 the leading subset for **solid‑tumor‑oriented** and CAR‑Vδ1 products (e.g. ADI‑001).
- Recent work highlights Vδ1 features attractive for solid tumors: high **lactic‑acid resistance** and antitumor activity in the acidic tumor microenvironment (PMID 42106736), CXCR3‑dependent tumor recruitment in colorectal cancer (PMID 42208977), and KIR‑defined effector programs (PMID 42044172).

### Vδ3 (and Vδ1⁻Vδ2⁻)
- A minor population enriched in liver and in some leukemias; can recognize CD1d/annexin contexts and display both cytotoxic and regulatory/APC‑like behavior. Less therapeutically developed.

## Functional polarization

Like CD4 helper cells, γδ cells polarize into functional programs, and which program dominates is decisive for cancer:

- **γδ1 (IFN‑γ⁺, Tbet/Eomes):** the antitumor program — cytotoxic, Th1‑like.
- **γδ17 (IL‑17⁺, RORγt):** the protumor program in most cancer contexts — recruits MDSCs/neutrophils, promotes angiogenesis and metastasis (see `04_dual_role_and_protumor.md`).
- **γδ‑APC:** Vγ9Vδ2 cells can upregulate MHC‑II and costimulatory molecules and cross‑present antigen to αβ T cells (Brandes et al., *Science* 2005), a property being exploited to bridge innate and adaptive antitumor immunity.
- **Regulatory / exhausted states:** chronic antigen and tumor‑microenvironment signals (TGF‑β, lactate, BTN3A1 dysregulation) can drive PD‑1⁺/TIM‑3⁺ exhaustion or suppressive phenotypes.

## Why subset choice drives product design

The recurring strategic decision in the therapeutic literature is **Vγ9Vδ2 vs Vδ1**:

| | Vγ9Vδ2 | Vδ1 |
| --- | --- | --- |
| Source | Peripheral blood (abundant) | Blood (rare) + tissue/tumor |
| Expansion | Easy, selective (zoledronate/BrHPP + IL‑2) | Harder; DOT/feeder protocols |
| Recognition | Phosphoantigen (BTN2A1/BTN3A1), NKG2D | NKG2D/NKp30/NKp44, stress ligands |
| TME fitness | Can be exhausted; sensitive to mevalonate manipulation | Better lactate/hypoxia resistance; tissue‑adapted |
| Lead products | Autologous trials, ICT01 agonist, Vγ9Vδ2 engagers, some CAR‑γδ | DOT cells, ADI‑001 (CAR‑Vδ1), allogeneic off‑the‑shelf |

Both are actively pursued; the field has not converged, and several programs deliberately use **total/pan‑γδ** or **mixed** products.
