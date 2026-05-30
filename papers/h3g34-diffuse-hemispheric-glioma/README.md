# H3.3 G34R/V diffuse hemispheric glioma literature synthesis

Organized papers and notes for H3.3 G34R/V diffuse hemispheric glioma (DHG-H3G34), with emphasis on scRNA-seq clustering, metaprograms, developmental trajectories, malignant cell state projection, tumor niches, subclones, and temporal evolution.

## Directory structure

- `index.tsv` — curated paper metadata, topic tags, and download status.
- `notes/h3g34_scrnaseq_analysis_report.md` — concise synthesis and concrete analysis recommendations.
- `pdfs/` — downloaded open-access PDFs.

## Scope notes

This collection prioritizes papers directly about H3.3 G34R/V / DHG-H3G34. Generic adult GBM and broader pediatric HGG papers are included only when they provide necessary methods/reference frameworks for scRNA-seq cell-state analysis or temporal evolution.

## Download note

PMC fronts every PDF download with a SHA-256 proof-of-work challenge (`cloudpmc-viewer-pow` cookie) that returns a "Preparing to download…" stub to plain `curl` / `wget`. `scripts/download_pmc_pdf.py` solves that handshake and is used to fetch every PMC-hosted row in `index.tsv`. The remaining `download_blocked; see URL` rows are on non-PMC hosts (JCI, BMC, Springer, Nature) that require a different access path.
