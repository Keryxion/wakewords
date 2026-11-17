# Hey Arya

Available as an openWakeWord ONNX head and a microWakeWord manifest plus TFLite
model. The shared openWakeWord frontend stays bundled with the client.

The dictionary lists installable artifacts; inclusion is not a device-validation
claim. Both are the models the training repository selects for Hey Arya. The microWakeWord model is the same file arya-esp32 bundles as its default.

- openWakeWord evaluation (`hey_arya`): Selected Arya openWakeWord model: 24/31 owner Arya utterances (22/22 Hey Arya, 2/5 bare Arya), 2/111 negatives. Pair with arya-openwakeword for bare Arya (together 27/31, 2/111).
  Noisy-bar session `bar-all-20261110-quick`: 10/10 intended wakes detected, 3/39 negatives fired.
- microWakeWord evaluation (`hey_arya-microwakeword`): Selected Arya microWakeWord model (ESP32 default): 23/31 owner Arya utterances (22/22 Hey Arya, 1/1 Okay Arya, 0/8 bare or name-first Arya), 10/111 negatives fired (9%, inside the 10% limit; fires on other "Hey <name>" phrases). Host replay; on-device validation pending.

The published microWakeWord manifest differs from the training build's in two
fields: `model` names the published file `hey_arya-microwakeword.tflite` (the
training build says `hey_arya.tflite`), and `sha256` of that file is added.

Source: [models-2026-11-17.2 release](https://github.com/Keryxion/wakewords/releases/tag/models-2026-11-17.2). Built and first published in the training repository as [voice-regression-2026-11-10](https://github.com/Keryxion/wakeword-training/releases/tag/voice-regression-2026-11-10) (openWakeWord) and [arya-2026-11-13](https://github.com/Keryxion/wakeword-training/releases/tag/arya-2026-11-13) (microWakeWord).
Evaluation and detector settings: [training repository candidate inventory](https://github.com/Keryxion/wakeword-training/blob/main/catalog/models.json).
License notes: See source attribution; Arya custom heads use noncommercial/share-alike negative features. Trained with kahrendt/microWakeWord on Piper LibriTTS synthetic clips, MIT RIRs, AudioSet and microWakeWord negative sets; datasets include noncommercial/share-alike terms.
