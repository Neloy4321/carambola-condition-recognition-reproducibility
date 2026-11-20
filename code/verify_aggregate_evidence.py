#!/usr/bin/env python3
"""Public aggregate arithmetic verification only. No model training or biological validation."""
import csv
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]

def read(path):
    with (BASE / path).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

d = read("results/original_v2/T2_dataset_quality_counts.csv")
assert sum(int(x["original_count"]) for x in d) == 2644
assert sum(int(x["unique_count"]) for x in d) == 2583
assert sum(int(x["redundant_exact_copies"]) for x in d) == 61

orig = read("results/original_v2/T4_locked_test_overall_metrics.csv")
r = next(x for x in orig if x["model"] == "resnet50v2_s42" and x["split"] == "locked_test_provisional")
assert int(r["n"]) == 388 and abs(float(r["accuracy"]) - 357/388) < 1e-9

g = read("results/expert_aggregate/table_s2_stage3_concordance.csv")
assert (
    sum(int(x["PROVISIONAL_CONCORDANT"]) for x in g),
    sum(int(x["PROVISIONAL_DISCORDANT"]) for x in g),
    sum(int(x["NON_SINGLE_CATEGORY"]) for x in g)
) == (54, 9, 9)

ov = read("results/overlap_label_evidence/O0_old_vs_grouped_cohort_decomposition.csv")
od = {x["cohort"]: (int(x["n"]), int(x["correct"])) for x in ov}
assert od["Intersection: old model"] == (59, 52)
assert od["Intersection: grouped model"] == (59, 49)

cal = read("results/calibration_conformal/E1_calibration_comparison.csv")
cr = next(x for x in cal if x["cohort"] == "exploratory_test" and x["method"] == "raw")
ct = next(x for x in cal if x["cohort"] == "exploratory_test" and x["method"] == "temperature_fitted_on_validation")
assert int(cr["n"]) == 394 and abs(float(cr["accuracy"]) - 319/394) < 1e-9
assert float(ct["NLL"]) < float(cr["NLL"]) and float(ct["accuracy"]) == float(cr["accuracy"])

print("PASS: historical aggregate source values consistent")
print("WARNING: arithmetic checks are not independent data/label validation")
