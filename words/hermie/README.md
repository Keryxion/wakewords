# Hermie

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. Bare-name models: they answer to "Hermie" on its own. Both are the best Hermie candidates in the training repository; neither meets its acceptance target.

- openWakeWord evaluation (`hermie-openwakeword`): Best Hermie openWakeWord candidate on owner recordings (6/12 wakes, 0/50 negatives); detects name-first Hermie, misses Hey/Okay Hermie; below the 90% acceptance target.
- microWakeWord evaluation (`hermie-microwakeword`): Best Hermie microWakeWord candidate on owner host replay (8/12 wakes, 2/50 negatives); detects name-first Hermie, misses Hey/Okay Hermie; below the 90% acceptance target; ESP32 device test pending.

Source: versioned model release [hermie-2026-11-13](https://github.com/Keryxion/wakeword-training/releases/tag/hermie-2026-11-13).
Origin: https://github.com/Keryxion/wakeword-training/pull/27
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: Training datasets include noncommercial/share-alike terms; retain attribution. See repository documentation.
