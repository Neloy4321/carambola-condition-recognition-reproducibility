# Capture-proxy sensitivity experiment (exploratory)

Model: ResNet50V2. The saved experiment was run with provisional acquisition groups, not verified specimen/tree IDs. Test: 394 image-file records, 80.96% accuracy and 79.47% macro-F1. Validation: approximately 84.92% accuracy and 84.32% macro-F1. Consult the frozen protocol, run design, class-wise reports, confusion matrices and historical training traces in this folder.

**Critical limitation:** proxy groups are class-confounded and the original-split test is a different cohort (388 images vs 394). Thus 92.01% vs 80.96% is not a paired estimate of leakage or causal benefit from group splitting. No orchard-held-out biological validation is claimed. The class `Iron Deficiency` shows especially weak grouped performance, but visual symptoms are not field-confirmed nutrient diagnoses.

No original images, labels or signed reviewer files are distributed here. Raw weights reside outside the repository.
