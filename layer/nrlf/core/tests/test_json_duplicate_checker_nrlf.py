import json

import pytest
from json_duplicate_checker import check_duplicate_keys

from layer.nrlf.tests.data import load_document_reference_data


def get_all_fields_from_json(json_str):
    def extract_fields(data, parent_key=""):
        fields = []
        if isinstance(data, dict):
            for k, v in data.items():
                full_key = f"{parent_key}.{k}" if parent_key else k
                fields.append(full_key)
                fields.extend(extract_fields(v, full_key))
        elif isinstance(data, list):
            for i, item in enumerate(data):
                full_key = f"{parent_key}[{i}]"
                fields.extend(extract_fields(item, full_key))
        return fields

    data = json.loads(json_str)
    return extract_fields(data)


def duplicate_field_in_json(json_str, field_path):
    data = json.loads(json_str)
    path = field_path.replace("]", "").replace("[", ".").split(".")
    current = data
    for key in path[:-1]:
        current = current[int(key) if key.isdigit() else key]
    field = path[-1]

    if field in current:
        duplicate_field = f"{field}_duplicate"
        current[duplicate_field] = current[field]
        modified_json_str = json.dumps(data)
        # Replace the duplicate field name with the original field name to simulate duplication
        duplicated_json_str = modified_json_str.replace(
            f'"{duplicate_field}":', f'"{field}":', 1
        )
        return duplicated_json_str
    return json_str


def load_document_reference_data_with_all_fields():
    docref_body = load_document_reference_data("Y05868-736253002-Valid")
    return get_all_fields_from_json(docref_body)


@pytest.mark.parametrize("field", load_document_reference_data_with_all_fields())
def test_parse_body_valid_docref_with_duplicate_keys(field):
    docref_body = load_document_reference_data("Y05868-736253002-Valid")

    docref_body = duplicate_field_in_json(docref_body, field)

    result = check_duplicate_keys(docref_body)

    node = field.split(".")[-1]
    assert result[0] == [node]
    assert result[1] == [f"DocumentReference.{field}"]
