# Extrahepatic / organ-targeted LNP engineering — Cross-cutting synthesis

## Executive summary

This collection captures **189 papers** (2013–2026; 78% from 2024–2026) on the enabling science behind non-liver-directed lipid nanoparticle delivery. The field has undergone a phase transition in ~3 years: from "we can only target the liver" to "we can systematically engineer organ selectivity via lipid chemistry, protein-corona shaping, and AI-guided design." The central organizing principle is that **the ionizable lipid's headgroup pKa, combined with the overall LNP surface charge and helper-lipid composition, determines which serum proteins adsorb (the corona), and the corona determines which organ internalizes the particle.**

## Five key findings

### 1. SORT is the foundational framework, but the field has moved beyond it

The SORT (Selective ORgan Targeting) principle — add a fifth charged lipid to redirect LNPs from liver to lung (cationic) or spleen (anionic) — was the 2020 breakthrough (Cheng et al., PMID 32251383). By 2025–2026, multiple groups achieve organ selectivity without a SORT additive, using:
- Ionizable lipids whose intrinsic headgroup pKa encodes organ preference.
- Combinatorial tail/linker modifications that alter cone geometry and membrane interactions.
- Zwitterionic polymer-lipid hybrids.
- Peptide surface codes that can be swapped modularly.

### 2. Machine learning has compressed the lipid-discovery cycle from years to weeks

The chemical space of ionizable lipids is vast (>10⁵ candidates with modest combinatorial expansion). Three ML approaches now dominate:
- **Bayesian optimization** over formulation parameters (converges in 3–5 rounds of 10–20 experiments).
- **Graph neural networks** (e.g. AGILE) that predict transfection from molecular structure (80% hit rate for top-10 liver candidates).
- **In vivo barcoded screening** (FIND, b-DNA) enables 100+ formulations to be evaluated in a single animal.

Together these create a design–predict–synthesize–screen–update loop that can identify organ-selective leads in weeks.

### 3. Lung targeting is the most mature extrahepatic application, but brain is the frontier

- **Lung**: Achievable by both systemic (IV + SORT/charge-tuned) and inhalation routes. Formulation challenges for inhalation (nebulization shear, mucus barrier, surfactant interaction) are being solved by PEG density optimization, NAC surface remodeling, and freeze-dried dry-powder formats.
- **Spleen/immune cells**: Anionic or high-pKa formulations reach spleen; cell-type specificity (DC vs macrophage vs T cell) requires active targeting (antibody/peptide conjugation) on top.
- **Brain**: Remains the hardest target. Even the best BBB-crossing LNPs deliver <1% of injected dose. AI-predicted formulations (Sela et al. 2025) and berberine-inspired ionizable lipids show promise but absolute delivery is still low.

### 4. Endosomal escape is organ-dependent and the biggest efficiency bottleneck

Only 1–4% of endocytosed RNA escapes to the cytoplasm. Critically, a lipid optimized for escape in hepatocytes may fail in lung epithelial cells, DCs, or neurons — the endosomal pH dynamics, membrane composition, and escape mechanism differ between cell types. This means organ-targeted LNP development must re-optimize escape in each new cellular context, not just redirect biodistribution.

### 5. The protein corona is the particle's true biological identity

The corona — the layer of adsorbed serum proteins — determines receptor recognition and cellular uptake, not the synthetic LNP surface. This has two implications:
- **Corona engineering** (via surface charge, PEG density, helper lipid) is the mechanistic lever for passive targeting.
- **In vitro results are unreliable** for predicting in vivo organ tropism because cell-culture media have different protein compositions than blood.

## Unresolved questions

1. **Repeated dosing**: anti-PEG antibodies develop after 2–3 doses, accelerating clearance. No consensus solution exists.
2. **Manufacturing consistency**: organ tropism is exquisitely sensitive to lipid ratios — how to ensure batch-to-batch reproducibility at scale?
3. **Safety of charged LNPs**: cationic (lung-targeting) formulations activate complement; anionic (spleen-targeting) have unknown long-term toxicity profiles.
4. **Combination with active targeting**: when passive targeting (formulation) gives organ selectivity and active targeting (ligand) gives cell-type selectivity, how to optimally combine them?
5. **Translation gap**: nearly all work is in mice; primate biodistribution data are scarce and may differ significantly due to species-specific corona proteins.

## Connection to lnp-cancer-payloads

The extrahepatic LNP engineering corpus is the **enabling platform** for the therapeutic payloads in the companion `lnp-cancer-payloads` collection:
- In vivo CAR needs T cell or spleen targeting.
- Cytokine mRNA (IL-12) needs tumor or spleen targeting.
- Tumor-suppressor restoration (p53, PTEN) needs tumor targeting.
- Gene editing needs cell-type-specific delivery + efficient endosomal escape.
- Brain tumors (GBM) need BBB-crossing formulations.

The payloads are ready; the delivery is the bottleneck these 189 papers are solving.
