#!/bin/sh

if [ "$DATABASE" = "random_desert" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata -e contenttypes db.json

exec "$@"