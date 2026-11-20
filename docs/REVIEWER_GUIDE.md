# Editor and reviewer navigation

This is a curated evidence repository. The full research archive is separately maintained. **No biological group independence or public image redistribution permission is asserted.**

## Audit path
1. Read README.md for cohort definitions and historical results.
2. Inspect results/original_v2/T2_dataset_quality_counts.csv and T4_locked_test_overall_metrics.csv for 2,644 source images, 2,583 MD5-unique images and provisional original ResNet50V2 test accuracy.
3. Inspect results/capture_proxy/frozen_proxy_protocol.json, run_design.json, test_metrics.json, test_classification_report.csv and confusion matrix for the exploratory group-proxy run.
4. Inspect results/expert_aggregate/table_s2_stage3_concordance.csv and results/overlap_label_evidence/S1_stage3_fe_discordance_sensitivity.csv for selected one-reviewer label-quality analysis.
5. Inspect results/overlap_label_evidence/O0_old_vs_grouped_cohort_decomposition.csv for the 59-image intersection of different historical test cohorts.
6. Inspect results/overlap_label_evidence/O3_historical_label_sensitivity_NOT_CORRECTED_TEST.csv only as **hypothetical label sensitivity**; it is NOT a new corrected test result.
7. Inspect results/calibration_conformal/E1_calibration_comparison.csv and E3_conformal_classwise_90pct.csv for retrospective prediction uncertainty.
8. Inspect results/small_pilot/pilot_seed_metrics.csv for the small hand-crafted-feature pilot. It showed **no consistent improvement**. Full three-seed CNN training intervention is **unexecuted**.

## Reproducibility tiers
- Public: compare aggregate source tables and run code/verify_aggregate_evidence.py (standard-library Python).
- Restricted: image-level manifests, expert reconciliation and original predictions; provide only through authorized editorial access.
- Full GPU replication: raw photographs, authorized original Kaggle notebooks, model weights and controlled credentials, not distributed here.

For double-blind review, an author-identifying GitHub profile may compromise anonymity; follow journal policy. Do not send unredacted reviewer signatures, private images or credentials via public Issues.
