#!/usr/bin/env python3
"""Fixtures for integration tests of GithubOrgClient"""

org_payload = {
    "login": "google",
    "id": 1342004,
    "url": "https://api.github.com/orgs/google",
}

repos_payload = [
    {
        "id": 1,
        "name": "repo1",
        "license": {"key": "mit"},
    },
    {
        "id": 2,
        "name": "repo2",
        "license": {"key": "apache-2.0"},
    },
    {
        "id": 3,
        "name": "repo3",
        "license": {"key": "apache-2.0"},
    },
]

# Expected list of all repo names
expected_repos = ["repo1", "repo2", "repo3"]

# Expected list of repos with apache-2.0 license
apache2_repos = ["repo2", "repo3"]
