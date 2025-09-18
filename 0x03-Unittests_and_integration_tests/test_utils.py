#!/usr/bin/env python3
"""
Unit tests for utils functions
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function"""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """Test that get_json returns expected dictionary"""
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

