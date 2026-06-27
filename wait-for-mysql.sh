#!/bin/sh

echo "Waiting for MySQL..."

while ! nc -z mysql 3306; do
  sleep 2
done

echo "MySQL is up!"

python app.py