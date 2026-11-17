"""Validate dictionary manifests; optionally verify downloaded release files."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlparse


def validate(root, artifacts=None):
    entries = sorted((root / "words").glob("*/wakeword.json"))
    if not entries:
        raise ValueError("Dictionary has no entries")
    phrases = set()
    for path in entries:
        if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", path.parent.name):
            raise ValueError(f"Invalid entry slug: {path.parent.name}")
        entry = json.loads(path.read_text())
        phrase = entry["phrase"]
        if not isinstance(phrase, str) or not phrase.strip() or phrase in phrases:
            raise ValueError(f"Empty or duplicate phrase in {path}")
        phrases.add(phrase)
        if not path.with_name("README.md").is_file():
            raise ValueError(f"Missing README for {phrase}")
        models = entry["models"]
        if not isinstance(models, dict) or not models:
            raise ValueError(f"No models for {phrase}")
        for engine, model in models.items():
            if engine not in ("micro_wake_word", "open_wake_word"):
                raise ValueError(f"Unknown engine {engine}")
            suffix = ".json" if engine == "micro_wake_word" else ".onnx"
            if not urlparse(model["url"]).path.endswith(suffix):
                raise ValueError(f"Wrong primary artifact for {engine}")
            files = model.get("files", [])
            if engine == "micro_wake_word":
                if len(files) != 1 or not urlparse(files[0]["url"]).path.endswith(".tflite"):
                    raise ValueError(f"Missing microWakeWord TFLite for {phrase}")
            for artifact in [model, *files]:
                url = urlparse(artifact["url"])
                if url.scheme != "https" or url.hostname != "github.com" or not re.fullmatch(
                    r"/[^/]+/[^/]+/releases/download/[^/]+/[^/]+", url.path
                ) or url.query or url.fragment or url.username or url.password:
                    raise ValueError(f"Expected versioned GitHub release URL: {artifact['url']}")
                if not re.fullmatch(r"[0-9a-f]{64}", artifact["sha256"]):
                    raise ValueError(f"Invalid hash for {artifact['url']}")
                if artifacts is not None:
                    local = artifacts / Path(url.path).name
                    if hashlib.sha256(local.read_bytes()).hexdigest() != artifact["sha256"]:
                        raise ValueError(f"Hash mismatch: {local}")
            if artifacts is not None and engine == "micro_wake_word":
                manifest = json.loads((artifacts / Path(urlparse(model["url"]).path).name).read_text())
                model_name = Path(urlparse(files[0]["url"]).path).name
                if manifest["model"] != model_name:
                    raise ValueError(f"Manifest references a different model for {phrase}")
    return len(entries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts", type=Path, help="Directory of downloaded release assets")
    args = parser.parse_args()
    count = validate(Path(__file__).resolve().parents[1], args.artifacts)
    print(f"Validated {count} dictionary entries.")
