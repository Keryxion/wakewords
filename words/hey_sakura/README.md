# Hey Sakura

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. These entries preserve the published 2026-11-09 versions, not an automatic
selection of the newest training candidate.

- openWakeWord evaluation: Owner recordings: 4/12 wakes, 0/110 negatives; misses bare Sakura. Not selected (sakura-openwakeword is better).
- microWakeWord evaluation: Owner host replay: 4/12 wakes, 3/110 negatives; misses bare Sakura. Not selected (sakura-microwakeword is better).

Source: [models-2026-11-17 release](https://github.com/Keryxion/wakewords/releases/tag/models-2026-11-17). Built and first published in the training repository as [wake-models-2026-11-09](https://github.com/Keryxion/wakeword-training/releases/tag/wake-models-2026-11-09).
Evaluation and detector settings: [training catalog](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: Training datasets include noncommercial/share-alike terms; retain attribution. See repository documentation.
