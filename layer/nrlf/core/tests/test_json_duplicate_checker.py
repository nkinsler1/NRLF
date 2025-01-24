import unittest

from json_duplicate_checker import check_duplicate_keys


class TestJsonDuplicateChecker(unittest.TestCase):
    def test_no_duplicates(self):
        json_content = '{"a": 1, "b": 2, "c": {"d": 3, "e": 4}}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, [])
        self.assertEqual(paths, [])

    def test_simple_duplicates(self):
        json_content = '{"a": 1, "b": 2, "a": 3}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, ["a"])
        self.assertEqual(paths, ["root.a"])

    def test_nested_duplicates(self):
        # This JSON has no duplicates because the 'b' keys are at different levels
        json_content = '{"a": {"b": 1}, "c": {"b": 2}, "d": {"e": {"b": 3}}}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, [])
        self.assertEqual(paths, [])

    def test_same_level_duplicates(self):
        # This JSON has duplicates because there are two 'b' keys at the same level
        json_content = '{"a": {"b": 1, "b": 2}, "c": {"d": 3}}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, ["b"])
        self.assertEqual(paths, ["root.a.b"])

    def test_same_level_duplicates_objects(self):
        # This JSON has duplicates because there are two 'b' keys at the same level
        # The difference with above is that the 'b' keys are objects and every element in the object is the same
        json_content = (
            '{"a": {"b": { "f": 4, "g": 5 }, "b": { "f": 4, "g": 5 } }, "c": {"d": 3}}'
        )
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, ["b"])
        self.assertEqual(paths, ["root.a.b"])

    def test_multiple_level_duplicates(self):
        # This JSON has duplicates at multiple levels
        json_content = '{"a": 1, "b": {"c": 2, "c": 3}, "a": 4}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(sorted(duplicates), sorted(["a", "c"]))
        self.assertEqual(sorted(paths), sorted(["root.a", "root.b.c"]))

    def test_invalid_json(self):
        json_content = "{invalid json}"
        with self.assertRaises(ValueError):
            check_duplicate_keys(json_content)

    def test_complex_nested_duplicates(self):
        json_content = '{"a": {"b": 1, "c": {"d": 2, "c": 3}}, "a": {"e": 4}}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(sorted(duplicates), sorted(["a"]))
        self.assertEqual(sorted(paths), sorted(["root.a"]))

    def test_multiple_duplicates_same_path(self):
        json_content = """
        {
            "a": 1,
            "b": {
                "c": 2,
                "c": 3,
                "d": {
                    "e": 4,
                    "e": 5,
                    "f": {
                        "g": 6,
                        "g": 7
                    }
                }
            },
            "b": {
                "h": 8
            }
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(sorted(duplicates), sorted(["b", "c", "e", "g"]))
        self.assertEqual(
            sorted(paths), sorted(["root.b", "root.b.c", "root.b.d.e", "root.b.d.f.g"])
        )

    def test_no_duplicates_deeply_nested(self):
        json_content = """
        {
            "a": {
                "b": {
                    "c": 1
                },
                "d": {
                    "e": 2
                }
            },
            "f": {
                "g": {
                    "h": 3
                }
            }
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, [])
        self.assertEqual(paths, [])

    def test_duplicates_with_arrays(self):
        json_content = """
        {
            "a": [
                {"b": 1, "b": 2},
                {"c": 3, "c": 4}
            ],
            "d": 5
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(sorted(duplicates), sorted(["b", "c"]))
        self.assertEqual(sorted(paths), sorted(["root.a[0].b", "root.a[1].c"]))

    def test_large_json_with_mixed_duplicates(self):
        json_content = """
        {
            "a": 1,
            "b": {
                "c": 2,
                "d": 3,
                "c": 4,
                "e": {
                    "f": 5,
                    "f": 6,
                    "g": {
                        "h": 7,
                        "h": 8
                    }
                }
            },
            "i": {
                "j": 10,
                "j": 11
            }
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(sorted(duplicates), sorted(["c", "f", "h", "j"]))
        self.assertEqual(
            sorted(paths),
            sorted(["root.b.c", "root.b.e.f", "root.b.e.g.h", "root.i.j"]),
        )

    def test_complex_nested_arrays_with_duplicates(self):
        json_content = """
        {
            "level1": {
                "arrays": [
                    {
                        "a": 1,
                        "a": 2,
                        "nested": {
                            "b": [
                                {"c": 3, "c": 4},
                                {"d": 5}
                            ],
                            "b": "duplicate"
                        }
                    },
                    {
                        "mixed": [
                            {"e": 6},
                            {"e": 7, "f": [
                                {"g": 8, "g": 9},
                                {"h": {"i": 10, "i": 11}}
                            ]}
                        ],
                        "mixed": "duplicate"
                    }
                ],
                "arrays": "duplicate_at_parent"
            }
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(
            sorted(duplicates), sorted(["a", "b", "c", "g", "i", "mixed", "arrays"])
        )
        self.assertEqual(
            sorted(paths),
            sorted(
                [
                    "root.level1.arrays",
                    "root.level1.arrays[0].a",
                    "root.level1.arrays[0].nested.b",
                    "root.level1.arrays[0].nested.b[0].c",
                    "root.level1.arrays[1].mixed",
                    "root.level1.arrays[1].mixed[1].f[0].g",
                    "root.level1.arrays[1].mixed[1].f[1].h.i",
                ]
            ),
        )

    def test_deep_nested_array_object_duplicates(self):
        json_content = """
        {
            "root": {
                "level1": [
                    {
                        "level2": [
                            [
                                {
                                    "data": 1,
                                    "data": 2,
                                    "unique": 3
                                }
                            ],
                            [
                                {
                                    "other": 4,
                                    "other": 5
                                }
                            ]
                        ]
                    }
                ]
            }
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(sorted(duplicates), sorted(["data", "other"]))
        self.assertEqual(
            sorted(paths),
            sorted(
                [
                    "root.root.level1[0].level2[0][0].data",
                    "root.root.level1[0].level2[1][0].other",
                ]
            ),
        )

    def generate_nested_json(self, depth, current_level=0):
        """Helper function to generate nested JSON with duplicates at each level."""
        if depth == 0:
            return '{"key": 1, "key": 2}'

        next_json = self.generate_nested_json(depth - 1, current_level + 1)
        return f"""{{
            "level{current_level}": [
                {{
                    "array_obj": {next_json},
                    "array_obj": "duplicate_at_depth_{current_level}"
                }}
            ]
        }}"""

    def get_expected_duplicates(self, max_depth):
        """Helper function to get expected duplicate keys."""
        duplicates = ["array_obj"]  # array_obj appears at each level
        duplicates.extend(["key"])  # key appears at the innermost level
        return sorted(list(set(duplicates)))

    def get_expected_paths(self, max_depth):
        """Helper function to get expected duplicate paths."""
        paths = []
        current_path = "root"

        # Start from level0 and increment
        for i in range(max_depth):
            current_path += f".level{i}[0]"
            paths.append(f"{current_path}.array_obj")
            if i < max_depth - 1:  # If not at the last level
                current_path += ".array_obj"  # Navigate into the nested object

        # Add the key duplicate at the innermost level
        if max_depth > 0:
            paths.append(f"{current_path}.array_obj.key")

        return sorted(paths)

    def test_parametrized_nested_arrays(self):
        """Test different depths of nested arrays with duplicates at each level."""
        for depth in range(1, 11):  # Test depths 1 through 10
            with self.subTest(depth=depth):
                json_content = self.generate_nested_json(depth)

                duplicates, paths = check_duplicate_keys(json_content)

                expected_duplicates = self.get_expected_duplicates(depth)
                expected_paths = self.get_expected_paths(depth)

                self.assertEqual(
                    sorted(duplicates),
                    sorted(expected_duplicates),
                    f"Failed for depth {depth} - duplicates mismatch",
                )
                self.assertEqual(
                    sorted(paths),
                    sorted(expected_paths),
                    f"Failed for depth {depth} - paths mismatch",
                )

    def test_array_edge_case_duplicate(self):
        json_content = """
        {
            "array": [
                1,
                "string",
                {"key": "value"},
                [1, 2, 3]
            ],
            "array": "duplicate"
        }
        """
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, ["array"])
        self.assertEqual(paths, ["root.array"])

    def test_case_sensitive_keys(self):
        json_content = '{"a": 1, "A": 2, "aA": 3, "Aa": 4}'
        duplicates, paths = check_duplicate_keys(json_content)
        self.assertEqual(duplicates, ["A", "Aa"])
        self.assertEqual(paths, ["root.A", "root.Aa"])
