POETRY_RUN = poetry run

lint:
	$(POETRY_RUN) pycodestyle .

test:
	$(POETRY_RUN) pytest

coverage:
	$(POETRY_RUN) pytest --cov=src tests/