install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml tests/

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

run:
	poetry run gendiff tests/fixture/file1.json tests/fixture/file2.json 

.PHONY: install test lint selfcheck check build