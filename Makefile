deploy: install migrate loaddata run

.PHONY : deploy

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

loaddata:
	python manage.py loaddata dex.json

run:
	python manage.py runserver

createuser:
	python manage.py createsuperuser