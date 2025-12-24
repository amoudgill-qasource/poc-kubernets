#!/bin/bash
set -e

echo "Waiting for database..."
sleep 10

echo "Running migrations..."
cd /app/ecommerce
python manage.py migrate --noinput

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000



