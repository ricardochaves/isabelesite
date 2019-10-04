#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata admin.json
python manage.py collectstatic --noinput

python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}

