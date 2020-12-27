# Set the default goal if no targets were specified on the command line
.DEFAULT_GOAL = run

PROJECT_NAME=marmon

migrate:
	alembic upgrade head

rollback:
	alembic downgrade -1

migration:
	alembic revision --autogenerate -m "${MESSAGE}"

run:  ## Runs dev server
	@uvicorn --reload main:app

reqs:  ## Install poetry requirements
	@poetry install

.PHONY: \
	migrate \
	rollback \
	migration \
	run \
	reqs