# Reproducing the available evidence

Run the public-only arithmetic checker with Python 3 (standard library):

    python3 code/verify_aggregate_evidence.py

The verifier checks saved aggregate CSV consistency. It does NOT rerun CNN training or establish reviewer identity, photo source rights, independence or field diagnosis. The available results are historical, and many test sets have already been inspected.

Full reproduction needs private per-image manifests and original images, official author permission, original Kaggle training notebooks and hardware/dependency specification. These were deliberately not committed to this public repository. The repository's pre-existing 20 November 2026 curated **93-file package**, held by the researchers, contains additional scripts, notebooks and source tracing; this GitHub mirror currently contains a documented subset of that archive.

Never treat the proposed corrected-label three-seed full-CNN experiment as completed or present reviewer-selected image-feature pilot numbers as CNN accuracy.
