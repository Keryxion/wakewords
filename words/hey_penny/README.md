# Hey Penny

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. These entries preserve the published 2026-11-09 versions, not an automatic
selection of the newest training candidate.

- openWakeWord evaluation: Selected Penny openWakeWord model on owner recordings (8/12 wakes incl. bare Penny, 0/70 negatives); below the 90% acceptance target.
- microWakeWord evaluation: Owner host replay: 3/12 wakes, 4/70 negatives; misses bare Penny. Not selected (penny-microwakeword is better).

Source: [versioned model release](https://github.com/Keryxion/wakeword-training/releases/tag/wake-models-2026-11-09).
Evaluation and detector settings: [training catalog](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: Training datasets include noncommercial/share-alike terms; retain attribution. See repository documentation.
