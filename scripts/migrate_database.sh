#!/bin/bash
cd /var/www/maximum
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput