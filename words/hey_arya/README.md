# Hey Arya

Available as an openWakeWord ONNX head only. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. The openWakeWord head is the model the training repository selects for Hey Arya. The selected microWakeWord model (`hey_arya-microwakeword`, the ESP32 default) is not listed yet: its published ESPHome manifest names the model file `hey_arya.tflite`, which does not match the release asset `hey_arya-microwakeword.tflite`, so it cannot be installed from the pinned release as published.

- openWakeWord evaluation (`hey_arya`): Selected Arya openWakeWord model: 24/31 owner Arya utterances (22/22 Hey Arya, 2/5 bare Arya), 2/111 negatives. Pair with arya-openwakeword for bare Arya (together 27/31, 2/111).
  Noisy-bar session `bar-all-20261110-quick`: 10/10 intended wakes detected, 3/39 negatives fired.

Source: versioned model release [voice-regression-2026-11-10](https://github.com/Keryxion/wakeword-training/releases/tag/voice-regression-2026-11-10).
Origin: https://github.com/Keryxion/arya-macos/blob/337463a422157211688bd7f5077965dac75fbb04/models/README.md
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: See source attribution; Arya custom heads use noncommercial/share-alike negative features.
