#!/bin/bash

echo "DB Connection --- Establishing . . ."

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 1
    echo "Waiting for DB --- Retrying . . ."
done

echo "DB Connection --- Successfully Established!"
echo "DB Migrations --- Running . . ."

alembic upgrade head

echo "DB Migrations --- Successfully Migrated!"
echo "FastAPI Application --- Running . . ."

python -m src.bidhub.main.web_api
