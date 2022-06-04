serve:
	python3 manage.py runserver

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

shell:
	python3 manage.py shell

superuser:
	python3 manage.py createsuperuser

testig:
	python3 manage.py test instagram

testuser:
	python3 manage.py test users

