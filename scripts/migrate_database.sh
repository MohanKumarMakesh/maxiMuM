#!/bin/bash
cd /var/www/maximum/src
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput