#!/bin/bash


DB_HOST=${POSTGRES_HOST:-localhost}
DB_PORT=${POSTGRES_PORT:-5432}
DB_USER=${POSTGRES_USER:-user}

echo "Checking database readiness..."

for i in $(seq 1 5); do
    echo "Attempt $i to connect to the database..."
    if pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; then
        echo "Database is ready."
        echo "Applying migrations..."
        poetry run alembic upgrade head
        break
    fi
    sleep 2
done
