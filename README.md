# Wake-word dictionary

A dictionary of installable wake words and phrases, organized like a skills
repository: one folder per phrase, a machine-readable manifest, and a README.
Training, evaluations, model binaries and historical candidates live in
[Keryxion/wakeword-training](https://github.com/Keryxion/wakeword-training).

| Phrase | Entry | Formats |
| --- | --- | --- |
| Hey Sakura | [words/hey_sakura](words/hey_sakura/) | microWakeWord, openWakeWord |
| Hey Penny | [words/hey_penny](words/hey_penny/) | microWakeWord, openWakeWord |
| Hey Hermie | [words/hey_hermie](words/hey_hermie/) | microWakeWord, openWakeWord |

Devices start with a bundled Hey Sakura model. A server reads this dictionary,
downloads a selected entry's files, verifies their hashes, caches them locally,
and commands the device to switch. The device downloads from the server and
keeps its previous wake word until the new model loads successfully.
This repository supplies data; runtime support is specified in
[hermes-converse PR #132](https://github.com/Keryxion/hermes-converse/pull/132).

## Dictionary index

Start with [`index.json`](index.json). It contains a format `version` and
an `entries` array with discovery metadata, for example:

```json
{
  "version": 1,
  "entries": [
    {
      "id": "hey_sakura",
      "phrase": "Hey Sakura",
      "description": "English Hey Sakura wake phrase for microWakeWord and openWakeWord. Published models with documented accuracy limitations.",
      "version": "1.0.0",
      "languages": [
        "en"
      ],
      "engines": [
        "micro_wake_word",
        "open_wake_word"
      ],
      "tags": [
        "assistant-name",
        "bundled-default"
      ],
      "status": "experimental",
      "manifest": "words/hey_sakura/wakeword.json",
      "readme": "words/hey_sakura/README.md"
    }
  ]
}
```

The listing supports browsing, searching by description or tags, and filtering
by language and engine before fetching a model manifest.

- `id` is the stable entry slug; `phrase` is its exact wake claim text.
- `description`, `languages` (language tags), and `tags` support discovery.
- `engines` lists the formats actually present in the manifest.
- Each entry's `version` is `major.minor.patch`; it is separate from the root
  index format version. Start entries at `1.0.0` and bump the entry version
  when its model artifacts or installation requirements change.
- `status` is `experimental` or `device_validated`. The latter requires linked
  target-device evidence in the entry README; host replay alone does not qualify.
- `manifest` and `readme` are repository-relative paths to the entry files.

Fetch the index and manifests from the same resolved commit; reject unsupported
index versions. Every phrase is listed exactly once. Validation checks that the
listing's ID, phrase, engines, and README agree with its manifest and directory.
Artifact URLs and hashes remain in the manifest.

## Entry format

Each manifest at `words/<slug>/wakeword.json` contains:

- `phrase`: the exact phrase sent in cooperative wake claims.
- `models`: formats available for that phrase, keyed by `micro_wake_word` or
  `open_wake_word`. Missing formats are unavailable.
- Each format's `url` and `sha256`: the primary artifact's pinned release URL
  and SHA-256. microWakeWord's primary file is its ESPHome JSON manifest;
  openWakeWord's is an ONNX head.
- microWakeWord's `files`: the referenced TFLite artifact, with its own `url`
  and `sha256`. Download beside the manifest using the release asset's name.

See [Hey Sakura's manifest](words/hey_sakura/wakeword.json) for a complete example.
Server-specific URLs and rewritten microWakeWord manifests belong in the local
cache, not this dictionary. Keep the source manifest and model hashes intact.

Resolve the dictionary to one commit before reading entries. Verify every
artifact before installing. Updating the dictionary does not silently update an
installed model. A phrase configuration alone is not an installable detector.

## Add or update a phrase

1. Publish the finished model files as versioned release assets in the training
   repository, with checksums, attribution and evaluation evidence.
2. Add or update `words/<slug>/wakeword.json`, its README, and `index.json`. Preserve the exact
   phrase, supported engines, pinned artifact URLs and verified hashes. Document
   evaluation limitations and license terms; do not infer device validation.
3. Verify downloaded bytes against every hash. Run `python3 tools/validate.py`
   and `git diff --check`, then submit a pull request.

The starter entries were checked against the release's SHA256SUMS. Their
READMEs preserve known accuracy limitations. They do not change client defaults.

Private release assets require the server's GitHub access. Credentials remain
on the server; devices use its existing authenticated download route.
