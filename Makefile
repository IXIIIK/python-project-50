install:
	poetry install

package-install:
	python3 -m pip install  dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

build:
	poetry build

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
