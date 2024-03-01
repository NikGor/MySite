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

migration:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

check:
	poetry run python manage.py check

dumpdata:
	@mkdir -p dumps
	@python manage.py close_old_connections
	@python manage.py dumpdata --indent 2 > dumps/content_dump_$(shell date +%d%m%Y).json

loaddata:
	@python manage.py loaddata content_dump.json
