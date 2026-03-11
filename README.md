# ACDH XML PyUtils

Utility functions to work with XML


## Features

* parse XML from files, strings or URLS
* print/save parsed files

see `tests/test_xml.py` for usage examples


## development

* project uses [uv](https://docs.astral.sh/uv/)
* linting/formatting `uv run ruff check .` `uv run ruff format .`
* before commiting run `flake8` to check linting and `uv run coverage run -m pytest -v` to run the tests

### bump version
```shell
uv version --bump minor
```