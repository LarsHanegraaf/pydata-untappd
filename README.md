# PyData - Untappd

Code used for my talk about ['How to not pull your hair out while providing data to the business, unit testing for data pipelines'](https://eindhoven2022.pydata.org/cfp/talk/HVQZR7/).

# What is in this repo?

This repo contains three phases of the talk; the initial code, refactoring no. 1 and refactoring no. 2.

- Initial code: [`orginal.py`](original.py).
- First refactoring: [`refactor_1.py`](refactor_1.py) and [`tests/test_1.py`](tests/test_1.py).
- Second refactoring [`refactor_2.py`](refactor_2.py) and [`tests/test_2.py`](tests/test_2.py).

## How to run

1. Have [Poetry](https://python-poetry.org/) installed.
2. Clone the repo.
3. Run `poetry install`
4. Run `poetry run pytest` to run the test suite (or activate the virtual environment that Poetry created and then just run `pytest`).
