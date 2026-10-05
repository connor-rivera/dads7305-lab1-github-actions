# DADS 7305 Lab 1: GitHub Actions CI with Pytest and Unittest

![Pytest](https://github.com/connor-rivera/dads7305-lab1-github-actions/actions/workflows/pytest_action.yml/badge.svg)
![Unittests](https://github.com/connor-rivera/dads7305-lab1-github-actions/actions/workflows/unittest_action.yml/badge.svg)

A small Python calculator module whose tests run automatically through GitHub Actions on every push and pull request to `main`. The pytest workflow runs on three Python versions and enforces a minimum test coverage.

This project is based on Prof. Ramin Mohammadi's [MLOps Github_Labs/Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1). The changes I made to it are listed in the section labeled '## Changes from the original lab'

**Author:** Connor Rivera · DADS 7305 Machine Learning Operations · Fall 2026

## Project structure

```
.
├── .github/workflows/
│   ├── pytest_action.yml     # Pytest + coverage on Python 3.10, 3.11, 3.12
│   └── unittest_action.yml   # Unittest suite
├── data/                     # Placeholder for project data
├── src/
│   └── calculator.py         # Calculator functions
├── test/
│   ├── test_pytest.py        # Parametrized pytest tests
│   └── test_unittest.py      # unittest tests
├── requirements.txt
└── README.md
```

## Functions in `src/calculator.py`

| Function | Description | Raises `ValueError` when |
|---|---|---|
| `add(x, y)` | x + y | an input is not a number |
| `subtract(x, y)` | x - y | an input is not a number |
| `multiply(x, y)` | x * y | an input is not a number |
| `add_three_nums(x, y, z)` | x + y + z | an input is not a number |
| `divide(x, y)` | x / y | an input is not a number, or y is 0 |
| `power(x, y)` | x raised to the power y | an input is not a number |
| `average(numbers)` | Mean of a list of numbers | the list is empty or contains a non-number |

## Running locally

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the pytest suite with coverage
python -m pytest --cov=src --cov-report=term-missing

# Run the unittest suite
python -m unittest test.test_unittest -v
```

Current results: **43 tests passed** under pytest (35 pytest cases plus the 8 unittest tests), **8 tests OK** under unittest, and **100% coverage** of `src/`.

## CI/CD pipeline

| Workflow | Triggers | What it does |
|---|---|---|
| **Testing with Pytest** | push / pull request to `main` | Runs on Python 3.10, 3.11 and 3.12 in parallel; runs pytest with coverage; fails if coverage drops below 90%; uploads the test and coverage reports as artifacts |
| **Python Unittests** | push / pull request to `main` | Runs the unittest suite on Python 3.11 |

## Changes from the original lab

### Code (`src/calculator.py`)
- Renamed `fun1`–`fun4` to descriptive names: `add`, `subtract`, `multiply`, `add_three_nums`.
- Added three new functions: `divide` (raises an error on division by zero), `power`, and `average` (takes a list instead of fixed arguments).
- Added input validation to `add_three_nums`. In the original, `fun4("a", "b", "c")` silently returned `"abc"`; it now raises a `ValueError` like the other functions.

### Tests
- Rewrote `test_pytest.py` using `@pytest.mark.parametrize`, so every input case is reported as its own test (35 cases).
- Added tests confirming that invalid inputs raise `ValueError` for every function, including division by zero and an empty list.
- Updated `test_unittest.py` to the new function names, added tests for the new functions, and added `assertRaises` checks.

### CI/CD pipeline
- Both workflows now also run on pull requests to `main`, so changes are tested before they are merged.
- Removed the unrelated `label` and `issues` triggers from the pytest workflow.
- Added a Python version matrix (3.10, 3.11, 3.12) to the pytest workflow.
- Added test coverage reporting with `pytest-cov` and a 90% minimum coverage gate.
- Uploaded the JUnit test report and the coverage report as artifacts, named per Python version.
- Updated the workflows so they run on current GitHub Actions: `actions/checkout`, `actions/setup-python` and `actions/upload-artifact` moved to v7 (`upload-artifact` v1–v3 have been shut down), Python moved from 3.8 to 3.11, and the `run-nam` typo and the conflicting `branches` / `branches-ignore` filters were fixed.
