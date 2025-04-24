#!/bin/bash

# Wait until PostgreSQL is ready
until pg_isready -h db -p 5432 -U user -d applications_db; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

echo "PostgreSQL is ready. Running migrations..."

# Run migrations
python manage.py makemigrations orders_client
python manage.py migrate

# Collect static files (optional if needed)
python manage.py collectstatic --noinput

# Navigate to the frontend directory and run the Gulp task
echo "Running Gulp to compile assets..."
cd frontend
gulp styles  # Adjust the Gulp task name if it's different

# Return to the original directory
cd ..

echo "Starting the Django application..."

# Start the application
exec gunicorn --bind 0.0.0.0:8001 my_blog_django.wsgi:application