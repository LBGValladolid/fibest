#!/bin/bash

docker-compose run django python manage.py compilemessages --locale=es
docker-compose run django python manage.py compilemessages --locale=en
docker-compose run django python manage.py makemigrations fibest
docker-compose run django python manage.py migrate
docker-compose down
docker-compose up --build

