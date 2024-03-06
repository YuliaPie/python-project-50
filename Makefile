install:
	poetry install

test:
	poetry run pytest

test-coverage:
	pytest --cov=gendiff tests/ --cov-report xml

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint
