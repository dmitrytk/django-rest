#!/bin/sh

echo "Initializing postgres db..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "Postgres database has initialized successfully."


exec "$@"