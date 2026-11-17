# Sakura

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. Bare-name models: they answer to "Sakura" on its own. Both are the models the training repository selects for Sakura.

- openWakeWord evaluation (`sakura-openwakeword`): Selected Sakura openWakeWord model on owner recordings (6/12 wakes, 0/110 negatives); misses Hey/Okay Sakura; below the 90% acceptance target.
- microWakeWord evaluation (`sakura-microwakeword`): Selected Sakura microWakeWord model on owner host replay (9/12 wakes, 2/110 negatives); misses Hey/Okay Sakura; below the 90% acceptance target; ESP32 device test pending.

Source: [models-2026-11-17.1 release](https://github.com/Keryxion/wakewords/releases/tag/models-2026-11-17.1). Built and first published in the training repository as [catalog-preservation-2026-11-12](https://github.com/Keryxion/wakeword-training/releases/tag/catalog-preservation-2026-11-12).
Origin: https://github.com/Keryxion/wakeword-training/pull/6
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: Training datasets include noncommercial/share-alike terms; retain attribution. See repository documentation.
