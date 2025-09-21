POETRY ?= poetry

.PHONY: install test coverage clean web

tree:
	tree > tree.txt

run:
	$(POETRY) run uvicorn main:app --reload --app-dir src/ps_camp

fmt:
	$(POETRY) run autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r .
	$(POETRY) run isort .
	$(POETRY) run black .

lint:
	$(POETRY) run flake8 .

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