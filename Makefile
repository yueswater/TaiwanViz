POETRY ?= poetry

.PHONY: install test coverage clean web

tree:
	tree > tree.txt

run:
	$(POETRY) run uvicorn api.main:app --reload

fmt:
	$(POETRY) run autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r . --exclude="*/__init__.py,*/venv/*,*/.venv/*"
	$(POETRY) run isort . --skip="__init__.py" --skip="venv" --skip=".venv"
	$(POETRY) run black . --exclude="/(venv|\.venv|__init__\.py)/"

lint:
	$(POETRY) run flake8 . --exclude="*/__init__.py,venv/*,.venv/*"

test:
	$(POETRY) run pytest $(ARGS)

ptw:
	PYTHONPATH=src $(POETRY) run pytest-watch

install:
	$(POETRY) install

coverage:
	$(POETRY) run pytest --cov --cov-report=term-missing $(ARGS)

clean:
	rm -rf .pytest_cache .coverage htmlcov
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;

web:
	$(POETRY) run uvicorn app:app --reload --app-dir web --port 8001