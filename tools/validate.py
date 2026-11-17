"""Validate dictionary manifests; optionally verify downloaded release files."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlparse


def validate(root, artifacts=None):
    index = json.loads((root / "index.json").read_text())
    if type(index.get("version")) is not int or index["version"] != 1:
        raise ValueError("Unsupported dictionary index version")
    listing = index.get("entries")
    if not isinstance(listing, list) or not listing:
        raise ValueError("Dictionary index must list entries")
    if any(not isinstance(item, dict) for item in listing):
        raise ValueError("Dictionary entries must be metadata objects")
    paths = [item.get("manifest") for item in listing]
    if any(not isinstance(path, str) or not re.fullmatch(
        r"words/[a-z0-9]+(?:_[a-z0-9]+)*/wakeword\.json", path
    ) for path in paths):
        raise ValueError("Invalid dictionary entry path")
    if len(set(paths)) != len(paths):
        raise ValueError("Duplicate dictionary entry path")
    actual = {path.relative_to(root).as_posix() for path in (root / "words").glob("*/wakeword.json")}
    if set(paths) != actual:
        raise ValueError("Index must list every entry exactly once, with no missing files")
    entries = [root / path for path in paths]
    phrases = set()
    for path, metadata in zip(entries, listing):
        if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", path.parent.name):
            raise ValueError(f"Invalid entry slug: {path.parent.name}")
        entry = json.loads(path.read_text())
        phrase = entry["phrase"]
        if not isinstance(phrase, str) or not phrase.strip() or phrase in phrases:
            raise ValueError(f"Empty or duplicate phrase in {path}")
        phrases.add(phrase)
        if metadata.get("id") != path.parent.name or metadata.get("phrase") != phrase:
            raise ValueError(f"Index identity differs from manifest: {path}")
        description = metadata.get("description")
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"Missing description for {phrase}")
        version = metadata.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", version):
            raise ValueError(f"Expected entry version major.minor.patch for {phrase}")
        for field in ("languages", "engines", "tags"):
            values = metadata.get(field)
            if not isinstance(values, list) or not values or any(
                not isinstance(value, str) or not value.strip() for value in values
            ) or len(set(values)) != len(values):
                raise ValueError(f"Expected unique nonempty {field} for {phrase}")
        if any(not re.fullmatch(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*", language) for language in metadata["languages"]):
            raise ValueError(f"Invalid language tag for {phrase}")
        if metadata.get("status") not in ("experimental", "device_validated"):
            raise ValueError(f"Missing evaluation status for {phrase}")
        if metadata.get("readme") != path.with_name("README.md").relative_to(root).as_posix():
            raise ValueError(f"Index README differs from entry: {path}")
        if not path.with_name("README.md").is_file():
            raise ValueError(f"Missing README for {phrase}")
        models = entry["models"]
        if not isinstance(models, dict) or not models:
            raise ValueError(f"No models for {phrase}")
        if set(metadata["engines"]) != set(models):
            raise ValueError(f"Index engine compatibility differs from manifest: {path}")
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
