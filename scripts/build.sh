cd client || exit
npm run build
cd .. || exit
python manage.py collectstatic --noinput --settings=config.settings.production
python manage.py runserver 127.0.0.1:8000 --settings=config.settings.production