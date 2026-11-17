# Arya

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. Bare-name models: they answer to "Arya" on its own. The openWakeWord head is recommended only as a companion to `hey_arya`; the microWakeWord model is weak and not selected.

- openWakeWord evaluation (`arya-openwakeword`): Standalone "Arya." 5/5 with 0/111 negatives on owner recordings, but 0/26 Hey/Okay/sentence forms (5/31 overall). Recommended as a companion head with hey_arya: together 27/31 wakes, 2/111 negatives.
- microWakeWord evaluation (`arya-microwakeword`): Owner host replay: 5/31 wakes, 3/111 negatives. Weak; not selected (hey_arya-microwakeword, the ESP32 firmware model, is better).

Source: [models-2026-11-17 release](https://github.com/Keryxion/wakewords/releases/tag/models-2026-11-17). Built and first published in the training repository as [arya-2026-11-13](https://github.com/Keryxion/wakeword-training/releases/tag/arya-2026-11-13).
Origin: https://github.com/Keryxion/wakeword-training/blob/main/configs/words/arya.yml
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: Training datasets include noncommercial/share-alike terms; retain attribution. See repository documentation.
