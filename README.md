# Carambola leaf and fruit condition recognition — reproducibility evidence

**Research evidence and audit trail; not an independently validated diagnostic tool.**

This repository documents a historical six-class *Averrhoa carambola* image-classification study and later exploratory reliability analyses (updated through **20 November 2026**). It is intended to help editors and reviewers inspect experimental methods, aggregate evidence, limitations, and reproducibility.

## Historical evidence at a glance

| Evidence | Recorded result | Important qualification |
|---|---:|---|
| Original dataset | 2,644 JPEG files | Files, not independent biological specimens |
| MD5-unique images | 2,583 | Exact hash deduplication only |
| Original-split ResNet50V2 test | 92.01% (n=388) | Previously inspected evaluation |
| Capture-proxy ResNet50V2 test | 80.96% (n=394) | Exploratory; not tree/orchard-independent |
| Two partial-class external datasets | 15.52%, 28.70% | Poor generalization; label alignment limitations |
| Expert review stages 1–2 | 231 image-file records | Enriched for model errors |
| Blinded expert review stage 3 | 72 selected training images | One reviewer, no independent plant diagnosis |
| Stage-3 descriptive original-label concordance | 54 direct, 9 different, 9 uncertain/overlapping | Not a whole-dataset mislabel-rate estimate |
| Overlap between original and grouped test cohorts | 59 image IDs | Full test cohorts and training conditions differ |
| Retrospective grouped-model temperature scaling | NLL 0.5562 to 0.5226 | No model accuracy increase |
| Strict training-label corrections identified | 3 | Full three-seed CNN intervention **not executed** |

## Key interpretation and warnings

- **No claim of verified tree, specimen, acquisition-session, or orchard independence.** Capture-proxy grouping is only a sensitivity analysis.
- **No confirmed nutrient diagnosis:** historical `Iron Deficiency` labels mean visual appearances; leaf/soil assays were not available.
- External and previous test sets were inspected and cannot be reclassified as prospective independent holdouts.
- The original and grouped results were obtained under different splits. The 92.01% to 80.96% difference **is not itself proof of leakage**.
- The 72-image blind review was selected by class and provisional proxy groups; prior expert review was enriched for errors. It is not representative of all images.
- Any labels or model rankings modified in retrospective sensitivity experiments are **hypothetical**. No corrected-label confirmatory test is claimed.
- Dataset ownership, image release rights, signed-reviewer disclosure, funding and authorship statements require formal verification before journal deposit.

## Evidence organization

- `results/`: original model, dataset-quality, expert-aggregate, grouped-robustness and external-evaluation tables.
- `code/`: reproducing aggregate checks and retrospective analyses where sufficient input data are available.
- `docs/`: reviewer guide, research limitations, source rights and distinctions between observed and planned analyses.
- `notebooks/`: original training notebooks, if and when cleared and committed.
- `figures/`: publication figures, where available and cleared.

**Public vs restricted evidence.** Raw photographs, image-level manifest/labels, model weights, reviewer signatures, credentials, and potentially identifying expert material are excluded from this public repository. Authorized editors may request a separately managed restricted evidence package subject to authorship, consent and editorial policies.

This repository is **not a peer-reviewed publication**. No reuse license has yet been granted. Public visibility does not itself authorize downstream redistribution of underlying image data.
