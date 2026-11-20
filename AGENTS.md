# Repository instructions

This repository is an install dictionary. Keep one phrase per words/<slug>/
folder with wakeword.json and README.md, listed once in the root index.json with accurate discovery metadata. Publish installable model
files as this repository's release assets, never in Git. Keep training and
evaluation tooling in Keryxion/wakeword-training.

Use versioned release URLs and verify SHA-256 for every file, including both
microWakeWord's manifest and its referenced model. Preserve license attribution
and evaluation limitations. Listing a model does not establish device validation
or authorize changing client defaults. Do not commit credentials or binaries.

Use a feature branch and PR for subsequent changes. Run python3 tools/validate.py
and git diff --check. Verify downloaded bytes before publishing new artifact pins.

## Shared with other repos

These files have copies or dependents in other Keryxion repositories; a change here also belongs there.

- Entries pin Keryxion/wakeword-training release assets, and the Arya clients' `models/downloads/*.json` and `docs/wakeword-recommendations.md` follow this index: a change here is incomplete until both sides agree.
