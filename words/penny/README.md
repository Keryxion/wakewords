# Penny

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. Bare-name models: they answer to "Penny" on its own and miss "Hey Penny". The microWakeWord model is the one the training repository selects for Penny; the openWakeWord head is the published bare-name candidate, and `hey_penny` holds the selected openWakeWord head.

- openWakeWord evaluation (`penny-openwakeword`): Owner recordings: 5/12 wakes, 0/70 negatives; misses Hey/Okay Penny. Not selected (hey_penny-openwakeword is better).
- microWakeWord evaluation (`penny-microwakeword`): Selected Penny microWakeWord model on owner host replay (8/12 wakes, 3/70 negatives: Benny, Denny, pen); misses Hey/Okay Penny; below the 90% acceptance target; ESP32 device test pending.

Source: [models-2026-11-17 release](https://github.com/Keryxion/wakewords/releases/tag/models-2026-11-17). Built and first published in the training repository as [catalog-preservation-2026-11-12](https://github.com/Keryxion/wakeword-training/releases/tag/catalog-preservation-2026-11-12).
Origin: https://github.com/Keryxion/wakeword-training/pull/6
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: Training datasets include noncommercial/share-alike terms; retain attribution. See repository documentation.
