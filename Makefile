install:
	pip install poetry
	poetry install --all-groups

run:
	poetry run python manage.py migrate
	poetry run python manage.py runserver
