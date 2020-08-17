#!/bin/sh
# https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#production-dockerfile

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

# Run these with docker compose exec web {command} instead
#
# python manage.py flush --no-input
# python manage.py migrate

exec "$@"
