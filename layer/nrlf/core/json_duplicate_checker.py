import json
from typing import List, Tuple, Set, Any, Dict, Union
from nrlf.core.errors import OperationOutcomeError
from nrlf.core.response import SpineErrorConcept

JsonValue = List[Any] | Tuple[Any, ...] | Any
JsonPair = Tuple[str, JsonValue]

class DuplicateKeyChecker:
    """JSON structure duplicate key detector.
    
    Tracks duplicate keys by maintaining path context during traversal.
    Paths are recorded in dot notation with array indices:
    - Objects: parent.child
    - Arrays: parent.array[0]
    - Nested: parent.array[0].child[1].key
    """

    def __init__(self):
        self.duplicate_keys: Set[str] = set()
        self.duplicate_paths: Set[str] = set()
        # Track keys at each path level to detect duplicates
        self.key_registry: Dict[str, Dict[str, bool]] = {}

    def check_key(self, key: str, path: List[str]) -> None:
        """Check if a key at the current path is a duplicate.
        
        A duplicate occurs when the same key appears twice at the same
        nesting level, even if the values differ.
        """
        current_level = '.'.join(path)
        
        if current_level not in self.key_registry:
            self.key_registry[current_level] = {}
            
        if key in self.key_registry[current_level]:
            self.duplicate_keys.add(key)
            full_path = '.'.join(path + [key])
            self.duplicate_paths.add(full_path)
            print(f"Found duplicate key: {key} at path: {full_path}")
        else:
            self.key_registry[current_level][key] = True

    def traverse_json(self, data: List[JsonPair], path: List[str]) -> None:
        """Traverse JSON structure and check for duplicate keys.
        
        Handles both objects and arrays, maintaining proper path context
        during traversal.
        """
        for key, value in data:
            print(f"Processing key: {key}, value: {value}")
            self.check_key(key, path)
            
            if isinstance(value, (list, tuple)):
                if value and isinstance(value[0], tuple):
                    # Handle nested object
                    self.traverse_json(value, path + [key])
                else:
                    # Handle array
                    self.traverse_array(value, path + [key])

    def traverse_array(self, items: List[Any], path: List[str]) -> None:
        """Process array items while tracking their indices in the path."""
        array_path = path[-1]
        base_path = path[:-1]
        
        for idx, item in enumerate(items):
            if not isinstance(item, (tuple, list)):
                continue
                
            current_path = base_path + [f"{array_path}[{idx}]"]
            if item and isinstance(item[0], tuple):
                # Handle object in array
                pairs = [item] if isinstance(item, tuple) else item
                self.traverse_json(pairs, current_path)
            else:
                # Handle nested array
                self.traverse_array(item, current_path)

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
    checker.traverse_json(parsed_data, ['root'])
    
    duplicates = list(checker.duplicate_keys)
    paths = list(checker.duplicate_paths)
    print("Final duplicates:", duplicates)
    print("Final paths:", paths)

    return duplicates, paths
