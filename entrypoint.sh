#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create Super User
echo "Create Super User"
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] ; then
    (python manage.py createsuperuser --noinput --username adminadmin)
fi

# # Handling Commands
# python manage.py seed_app_config

# Start Gunicorn
echo "Starting Gunicorn"
exec gunicorn -c gunicorn_config.py core.wsgi