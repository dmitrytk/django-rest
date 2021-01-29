cd client
npm run build
cd ..
python manage.py collectstatic --noinput --settings=config.settings.production