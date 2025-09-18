#!/usr/bin/env python3
"""
Unit tests for utils.py functions: access_nested_map and get_json
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the correct result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),           # empty dict
        ({"a": 1}, ("a", "b")), # trying to access a key of non-dict
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError or TypeError as expected"""
        with self.assertRaises((KeyError, TypeError)) as cm:
            access_nested_map(nested_map, path)
        # Only assert message if it's a KeyError
        if isinstance(cm.exception, KeyError):
            self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Unit tests for get_json function"""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """Test that get_json returns the expected dictionary"""
        test_payload = {"payload": True}
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        url = "http://fakeurl.com"
        result = get_json(url)

        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()

