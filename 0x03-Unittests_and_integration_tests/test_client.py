#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """Test GithubOrgClient.org returns correct value"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns expected value"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "http://test.url"}
            client = GithubOrgClient("test")
            result = client._public_repos_url
            self.assertEqual(result, "http://test.url")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns expected repo names"""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = "http://test.url"
            client = GithubOrgClient("test")
            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://test.url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license with different repos and licenses"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
