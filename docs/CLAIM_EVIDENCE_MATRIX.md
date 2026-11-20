# Claim-to-evidence register

| Reported claim | Primary repository evidence | Caution |
|---|---|---|
| Original inventory / MD5 dedup | results/original_v2/T2_dataset_quality_counts.csv | hash distinct != biological distinct |
| Historical ResNet50V2 92.01% | results/original_v2/T4_locked_test_overall_metrics.csv | inspected provisional split |
| Capture-proxy ResNet50V2 80.96% | results/capture_proxy/test_metrics.json | exploratory n=394 |
| Strong grouped class failures | results/capture_proxy/test_classification_report.csv; results/expert_aggregate/table_s7_capture_proxy_confusions.csv | class-proxy confounding |
| Two poor external evaluations | results/original_v2/T8b_online_external_partial_summary.csv | partial label alignment; inspected |
| Stage-3 54/9/9 | results/expert_aggregate/table_s2_stage3_concordance.csv | selected training images, one reviewer |
| Iron pattern discrepancy | results/overlap_label_evidence/S1_stage3_fe_discordance_sensitivity.csv | descriptive and capture-dependent |
| 59 shared test IDs | results/overlap_label_evidence/O0_old_vs_grouped_cohort_decomposition.csv | different training/cohort |
| Advisory model-rank change | results/overlap_label_evidence/O3_historical_label_sensitivity_NOT_CORRECTED_TEST.csv | strictly hypothetical |
| Temperature NLL decrease | results/calibration_conformal/E1_calibration_comparison.csv | retrospective, accuracy unchanged |
| Conformal Fe class undercoverage | results/calibration_conformal/E3_conformal_classwise_90pct.csv | not field validated |
| Correction pilot | results/small_pilot/pilot_seed_metrics.csv | negative pilot, not CNN |
| Full matched corrected-label CNN benefit | **No completed evidence** | planned only; no performance claim |
