#!/usr/bin/env python3
"""
Utility functions for working with nested maps, JSON requests, and memoization.
"""
import requests
from functools import wraps
from typing import Mapping, Any, Sequence


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access an element in a nested map using a path of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Any:
    """Make a GET request to a URL and return the JSON response"""
    response = requests.get(url)
    return response.json()


def memoize(method):
    """Decorator to cache method results"""
    attr_name = "_{}".format(method.__name__)

    @wraps(method)
    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)
    return property(memoized)
