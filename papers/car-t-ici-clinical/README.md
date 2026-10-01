# CAR-T + immune checkpoint inhibitors (ICI) — clinical evidence collection

Scope: **what has actually been observed in patients** when CAR-T cell therapy is
combined with, or sequenced around, checkpoint blockade — efficacy, safety, and
how strong (or weak) the underlying study designs are.

Five distinct questions are kept separate throughout, because the literature
conflates them and they do not support each other:

| Bucket | Question it answers | Index category |
|---|---|---|
| ICI as part of the CAR-T regimen | Does adding ICI to CAR-T improve response? | `heme_concurrent_combination`, `heme_cd30_hodgkin`, `solid_tumor_combination` |
| ICI maintenance/consolidation | Does ICI after a CAR-T response deepen/prolong it? | `heme_pd1_maintenance` |
| ICI salvage | Can ICI rescue patients after CAR-T failure? | `post_cart_checkpoint_salvage` |
| ICI before CAR-T / timing | Does prior or pre-infusion ICI help or harm? | `ici_before_cart_sequencing` |
| CAR-T with built-in checkpoint blockade | PD-1 knockout / PD1-locus / secreted anti-PD-1 — *not* systemic ICI | `engineered_checkpoint_resistance` |

Preclinical work is included only as rationale and is tagged `tier:preclinical`;
it is not evidence of clinical benefit.

## Contents

- `notes/00_overview.md` — the narrative review (read this first): per-trial
  efficacy/safety numbers, historical-benchmark comparisons, safety synthesis,
  evidence-quality assessment, open questions.
- `index.tsv` — curated index (`category`, identifiers, `topics`, `status`).
  `topics` carries `tier:` (evidence type), `selection:` (`pinned` = core paper
  the review is built on, `auto` = breadth from the query sweep) and `setting:`.
- `REPORT.md` — auto-generated listings grouped by evidence category.
- `fulltext/` — open-access full-text XML mirrored from Europe PMC.
- `raw_harvest.json` — raw Europe PMC provenance (every record + the query that
  returned it).

## Reproduce

```bash
python3 harvest.py          # Europe PMC sweep (9 topic groups + pinned title lookups) -> raw_harvest.json
python3 curate.py           # pinned + auto selection, tiering -> index.tsv
python3 fetch_fulltext.py   # mirror OA full text -> fulltext/, fills local_fulltext
python3 gen_report.py       # -> REPORT.md
```

## Caveats on this collection

- No randomized trial has compared CAR-T + ICI against CAR-T alone. Every
  efficacy comparison in the notes is against historical/non-randomized
  controls and is therefore hypothesis-generating only.
- Several widely cited combination cohorts (e.g. CD30 CAR-T + nivolumab, some
  solid-tumor trials) exist only as conference abstracts; these are flagged in
  the notes and deliberately not treated as peer-reviewed outcome data.
- Registry entries for ongoing trials are not outcome data and are not indexed
  as such.
- Auto-selected rows are title/abstract-screened by keyword, not read in full.
