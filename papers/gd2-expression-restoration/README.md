# Restoring / upregulating GD2 expression for immunotherapy

Curated literature on how the disialoganglioside **GD2** is lost or downregulated on tumor cells, and on strategies to **restore or upregulate GD2 surface expression** — especially epigenetic approaches (EZH2 and HDAC inhibition) that de-repress GD2 biosynthetic enzymes to enable anti-GD2 antibody, ADC, and CAR-T targeting. Includes GD2-directed CAR-T work in H3-mutant CNS tumors, tying into the repository's DHG-H3G34 target-discovery focus (GD2 = `B4GALNT1` + `ST8SIA1`).

## Directory structure

- `index.tsv` — curated paper metadata, topic categories, and download status.
- `notes/gd2_restoration_synthesis.md` — synthesis of GD2 biosynthesis, loss mechanisms, and restoration strategies.
- `pdfs/` — downloaded open-access PDFs (see download note below).

## `index.tsv` columns

`category`, `authors`, `title`, `venue`, `year`, `doi`, `url`, `local_pdf`, `notes`.

## Category tags

- `epigenetic_restoration` — EZH2i / HDACi (and related) upregulation of GD2 for targeting. **Core of this collection.**
- `gd2_biosynthesis` — regulation of GD2/GD3 synthase (`B4GALNT1`, `ST8SIA1`) and ganglioside pathway.
- `gd2_loss_resistance` — mechanisms of GD2 downregulation / antigen escape driving immunotherapy resistance.
- `foundational_gd2` — GD2 as a therapeutic target; expression surveys and assay caveats.
- `gd2_car_cns` — GD2-directed CAR-T in H3-mutant / CNS tumors (direct relevance to DHG-H3G34).

## Key relationship to the EZH2 collection

The single most direct paper is **Kailayangiri et al. (`30879952`)**: EZH2 inhibition de-represses the GD2 synthase in Ewing sarcoma, **restoring surface GD2** to enable gene-modified T-cell targeting. This is the mechanistic bridge between the companion `ezh2-inhibitors` collection and GD2-directed immunotherapy. See also anti-GD2 ADC + EZH2i in osteosarcoma (`40533837`) and HDAC-inhibitor-based GD2 upregulation (`27471639`, `30670592`).

## Biosynthesis note (from repository target list)

GD2 is synthesized by the combined action of **`B4GALNT1`** (GM2/GD2 synthase) and **`ST8SIA1`** (GD3 synthase). "Restoring GD2" generally means de-repressing or inducing these enzymes (epigenetically or via differentiation), and/or reversing the mesenchymal/dedifferentiated states that silence them.

## Download note

Metadata is verified against PubMed (PMIDs in the `url` column). Open-access PDF retrieval was attempted; rows without a committed PDF are marked `no_open_pdf_added` or `download_blocked; see URL`. Access full text via the DOI/PubMed link.
