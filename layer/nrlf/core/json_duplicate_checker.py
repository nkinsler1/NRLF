import json
from collections import OrderedDict
from typing import Dict, List, Tuple

JsonPrimitive = str | int | float | bool | None
type JsonValue = JsonPrimitive | JsonObject | JsonArray
JsonPair = tuple[str, JsonValue]
JsonObject = list[JsonPair]
JsonArray = list[JsonValue]


class DuplicateKeyChecker:
    """JSON structure duplicate key detector.

    Tracks duplicate keys by maintaining path context during traversal.
    Paths are recorded in dot notation with array indices:
    - Objects: parent.child
    - Arrays: parent.array[0]
    - Nested: parent.array[0].child[1].key
    """

    def __init__(self):
        # Here a list of paths because the same key name could be at different levels
        self.duplicate_keys_and_paths: OrderedDict[str, list[str]] = OrderedDict()
        # Track keys at each path level to detect duplicates
        self.key_registry: Dict[str, Dict[str, bool]] = {}
        self.current_duplicate_index: Dict[str, int] = {}
        # Track seen array elements to detect duplicates
        self.seen_array_elements: Dict[str, List[JsonValue]] = {}

    def get_path_with_index(self, path: List[str], key: str) -> List[str]:
        current_level = ".".join(path)
        index_map = self.current_duplicate_index.setdefault(current_level, {})
        count = index_map.get(key, 0)
        index_map[key] = count + 1

        # If it's the first occurrence, keep the key as is.
        # Subsequent occurrences get bracket-indexed.
        if count == 0:
            return path + [key]
        else:
            return path + [f"{key}[{count - 1}]"]

    def check_key(self, key: str, path: List[str]) -> None:
        """Check if a key at the current path is a duplicate.

        A duplicate occurs when the same key appears twice at the same
        nesting level, even if the values differ.
        """
        current_level = ".".join(path)
        current_keys = self.key_registry.setdefault(current_level, {})
        if key in current_keys:
            duplicate_path = ".".join(path + [key])
            self.duplicate_keys_and_paths.setdefault(key, []).append(duplicate_path)
            print(f"Found duplicate key: {key} at path: {'.'.join(path + [key])}")
        else:
            current_keys[key] = True

    def process_collection(
        self, value: JsonObject | JsonArray, path: list[str], key: str
    ) -> None:
        """Determine if the given 'value' is an object or an array and handle it."""
        new_path = self.get_path_with_index(path, key)
        if value and isinstance(value[0], tuple):
            self.traverse_json(value, new_path)
        else:
            self.traverse_array(value, new_path)

    def traverse_json(self, data: JsonObject, path: list[str]) -> None:
        """Traverse JSON object and check for duplicate keys."""
        for key, value in data:
            print(f"Processing key: {key}, value: {value}")
            self.check_key(key, path)
            if isinstance(value, (list, tuple)):
                self.process_collection(value, path, key)

    def traverse_array(self, items: JsonArray, path: list[str]) -> None:
        """Process JSON array items while updating the path for duplicates."""
        array_path = path[-1]
        base_path = path[:-1]
        seen_elements = self.seen_array_elements.setdefault(".".join(path), set())

        for idx, item in enumerate(items):
            serialized_item = json.dumps(item, sort_keys=True)
            if serialized_item in seen_elements:
                element = f"{array_path}[{idx}]"
                duplicate_path = ".".join(base_path + [element])
                self.duplicate_keys_and_paths.setdefault(element, []).append(
                    duplicate_path
                )
                print(f"Found duplicate array element at path: {duplicate_path}")
            else:
                seen_elements.add(serialized_item)

            if not isinstance(item, (list, tuple)):
                continue
            self.process_collection(item, base_path, f"{array_path}[{idx}]")


def check_duplicate_keys(json_content: str) -> Tuple[List[str], List[str]]:
    """Find all duplicate keys in a JSON string.

    Traverses the entire JSON structure and reports:
    - List of keys that appear multiple times at the same level
    - Full paths to each duplicate key occurrence

    A key is considered duplicate if it appears multiple times within
    the same object, regardless of nesting level or array position.
    """
    try:
        parsed_data = json.loads(json_content, object_pairs_hook=lambda pairs: pairs)
        print("Parsed JSON:", parsed_data)
    except json.JSONDecodeError:
        raise ValueError("Error: Invalid JSON format")

    checker = DuplicateKeyChecker()
    checker.traverse_json(parsed_data, ["root"])

    duplicates = list(checker.duplicate_keys_and_paths.keys())
    # flatten the list of paths
    paths = sum(checker.duplicate_keys_and_paths.values(), [])
    print("Final duplicates:", duplicates)
    print("Final paths:", paths)

    return duplicates, paths
