#!/bin/bash
# run this once to set up the project

echo "Installing packages..."
pip install -r requirements.txt

echo "Setting up database..."
python manage.py makemigrations card
python manage.py migrate

echo "Done! Now run: python manage.py runserver"
