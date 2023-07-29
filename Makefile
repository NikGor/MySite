.PHONY: install test run

install:
	poetry install

test:
	poetry run python manage.py test

run:
	poetry run python manage.py runserver

lint:
	poetry run flake8 mysite

amend-and-push:
	git add .
	git commit --amend --no-edit
	git push --force

say-hello:
	@echo "Hello, World!"