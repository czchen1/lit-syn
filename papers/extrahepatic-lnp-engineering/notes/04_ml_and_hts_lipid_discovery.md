# Machine learning and high-throughput screening for lipid discovery

## The bottleneck: chemical space is vast

An ionizable lipid has ~5 independent structural variables (headgroup, linker, tail length × 2, branching, unsaturation). With even modest combinatorial expansion (10 headgroups × 5 linkers × 20 tails²), the space exceeds 10⁵ candidates. Traditional one-at-a-time synthesis and in vitro screening is too slow.

## In vivo barcoded screening

The biggest methodological advance in the field (2020–present) is **DNA/mRNA barcoding** for massively parallel in vivo evaluation:

1. Each lipid formulation encapsulates a unique DNA or mRNA barcode.
2. All formulations are pooled and injected IV into one animal.
3. Organs are harvested; barcode abundance (by sequencing or qPCR) reports per-organ transfection efficiency.

Key platforms:
- **FIND (Formulation Identification via Nucleic acid Detection)** — mRNA barcodes + qPCR/sequencing (Dahlman lab).
- **b-DNA barcoding** — short DNA barcodes with unique primer pairs (Siegwart lab).
- **Cre-lox reporter mice** — barcoded LNPs deliver Cre mRNA; organ-specific reporter activation measures functional delivery.

Hamilton et al. (2026) report screening 100+ LNP formulations in a single mouse, identifying liver-, lung-, and spleen-targeting hits in one experiment.

## Machine learning approaches

### Bayesian optimization
- Li et al. (2024, PMID 38072809) use Bayesian optimization over a 4D lipid formulation space (ionizable lipid, helper lipid, cholesterol, PEG-lipid ratios) to find organ-selective optima in <50 experiments.
- Iterative Bayesian campaigns typically converge in 3–5 rounds, each requiring 10–20 formulations.

### Graph neural networks
- **AGILE** (Zhang et al. 2024, PMID 38770138): treats each ionizable lipid as a molecular graph; trained on 1,200 lipid-activity pairs; predicts top-10 liver-targeting candidates with 80% hit rate.
- **FALCON** (model from Heredero 2025 context): graph-based predictions of organ tropism from lipid structure + formulation parameters.

### Transformer / language models
- Molecular transformers fine-tuned on lipid SMILES → transfection efficiency prediction.
- Sela et al. (2025, PMID 40957853) use AI-validated brain-targeted LNPs — model predicts BBB-crossing formulations before synthesis.

### Generative models
- VAE (variational autoencoder) and diffusion models proposed for de novo ionizable lipid design in 2025–2026 preprints.
- Goal: generate lipids with specified organ-tropism profiles, then validate experimentally.

## Integrated workflows

The state-of-the-art pipeline (2025–2026):
1. **Generate** candidate lipids via multicomponent reaction or generative model.
2. **Predict** top candidates via ML model (graph NN or Bayesian).
3. **Synthesize** 50–200 candidates in parallel.
4. **Screen in vivo** via barcoded pooled injection.
5. **Update** ML model with new data → iterate.

This reduces the lipid-to-lead cycle from years to weeks.

## Papers (selected)

- Li B et al. (2024) PMID 38072809 — Bayesian optimization for mRNA delivery.
- Zhang Y et al. (2024) PMID 38770138 — AGILE graph neural network.
- Hamilton AG et al. (2026) — HT barcoded in vivo screening.
- Heredero J et al. (2025) PMID 40284454 — Predictive biodegradable IL library.
- Sela M et al. (2025) PMID 40957853 — AI-validated brain-targeted LNPs.
- Su LJ et al. (2026) — AI-guided LNP design for targeted delivery.
