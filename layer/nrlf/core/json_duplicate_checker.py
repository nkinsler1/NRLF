import json
from typing import Any


def check_for_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict:
    keys = {}
    dupes = {}
    normalized_keys = []

    for key, value in pairs:
        normalized_key = key.lower()
        if normalized_key in normalized_keys:
            dupes.setdefault(key, []).append(value)
        else:
            keys[key] = value
            normalized_keys += [normalized_key]

    if dupes:
        keys["__duplicates__"] = dupes

    return keys


def flatten_duplicates(data: dict | list) -> list[str]:
    duplicates = []
    items = data.items() if isinstance(data, dict) else enumerate(data)

    for key, value in items:
        if key == "__duplicates__":
            duplicates.extend(value.keys())
        elif isinstance(value, (dict, list)):
            path = f"{key}" if isinstance(data, dict) else f"[{key}]"
            dupes = flatten_duplicates(value)
            duplicates.extend([f"{path}.{dupe}" for dupe in dupes])

    return duplicates


def format_path(path: str) -> str:
    """Transforms a path like root.key1.[2].key2 into root.key1[2].key2"""
    parts = path.split(".")
    formatted_parts = []
    for part in parts:
        if part.startswith("["):
            formatted_parts[-1] += part
        else:
            formatted_parts.append(part)
    return ".".join(formatted_parts)


def check_duplicate_keys(json_content: str) -> tuple[list[str], list[str]]:
    """Find all duplicate keys in a JSON string.

    Traverses the entire JSON structure and reports:
    - List of keys that appear multiple times at the same level
    - Full paths to each duplicate key occurrence

    A key is considered duplicate if it appears multiple times within
    the same object, regardless of nesting level or array position.
    """
    try:
        dupe_data = json.loads(json_content, object_pairs_hook=check_for_duplicate_keys)
        duplicate_paths = [
            f"root.{format_path(path)}" for path in flatten_duplicates(dupe_data)
        ]
        duplicate_keys = list(
            dict.fromkeys([key.split(".")[-1] for key in duplicate_paths])
        )
        return duplicate_keys, duplicate_paths
    except json.JSONDecodeError:
        raise ValueError("Error: Invalid JSON format")
