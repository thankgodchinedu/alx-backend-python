# 0x03. Unittests and Integration Tests

## Description
This project focuses on writing unit tests and integration tests in Python.  
It covers parameterized tests, mocking external calls, and verifying correct function behavior.

## Requirements
- Python 3.7 (on Ubuntu 18.04 LTS)
- pycodestyle 2.5
- All files are executable and end with a new line
- All functions, classes, and modules contain proper documentation
- All functions and coroutines are type-annotated

## Files
- `utils.py`: Contains utility functions (`access_nested_map`, `get_json`, `memoize`).
- `client.py`: Client-related functions.
- `fixtures.py`: JSON test fixtures.
- `test_utils.py`: Unit tests for `utils.py`.

## How to Run Tests
```bash
python3 -m unittest test_utils.py
