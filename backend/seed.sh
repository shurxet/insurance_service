#!/bin/sh


echo "Starting database seed..."

sleep 20

poetry run python -m app.seed

echo "Seed completed."
