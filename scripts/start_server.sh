#!/bin/bash
cd /var/www/maximum/src
source venv/bin/activate
gunicorn --workers 3 --bind 127.0.0.1:8000 maximum.wsgi:application --daemon