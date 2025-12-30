#!/bin/bash
set -e

echo "Waiting for database..."
for i in {1..30}; do
    if python -c "import MySQLdb; MySQLdb.connect(host='$DB_HOST', user='$DB_USER', passwd='$DB_PASSWORD', db='$DB_NAME', port=${DB_PORT:-3306})" 2>/dev/null; then
        echo "Database connected successfully"
        break
    fi
    echo "Attempt $i: Waiting for database..."
    sleep 1
done

echo "Running migrations..."
python /app/ecommerce/manage.py migrate --noinput

echo "Starting Django server..."
python /app/ecommerce/manage.py runserver 0.0.0.0:8000
