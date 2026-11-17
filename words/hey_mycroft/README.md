# Hey Mycroft

Available as an openWakeWord ONNX head only. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. The upstream openWakeWord v0.5.1 release model, mirrored unchanged. No microWakeWord model is published for this phrase.

- openWakeWord evaluation (`hey_mycroft_v0.1`): Human microphone host replay; see scoped recommendation and noisy-bar summary. Target-device validation is separate.
  Noisy-bar session `bar-all-20261110-quick`: 1/1 intended wakes detected, 0/48 negatives fired.

Source: versioned model release [catalog-preservation-2026-11-12](https://github.com/Keryxion/wakeword-training/releases/tag/catalog-preservation-2026-11-12).
Origin: https://github.com/Keryxion/arya-macos/blob/337463a422157211688bd7f5077965dac75fbb04/models/README.md
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: See source attribution; Arya custom heads use noncommercial/share-alike negative features.
