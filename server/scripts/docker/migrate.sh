docker-compose exec server python manage.py flush --no-input
docker-compose exec server python manage.py migrate
