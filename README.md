# Horizon geological database

> ### Django and PostgreSQL app with Vue.js front-end

### Run locally

#### Requirements

- Python 3.7+
- PostgreSQL 11+. PSQL command line tool
- Node.js 12+

Clone repository.

```
git clone git@github.com:dmitrytk/horizon.git
cd horizon
```

Setup development environment and run Django development server

```
chmod +x ./scripts/local_setup.sh
./scripts/local_setup.sh
```

Run Vue development server

```
cd client
npm run serve
```

### Run by Docker
```
docker-compose up -d
```

Migrate and create Django superuser
```
docker exec -it horizon_server bash
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py migrate
python manage.py createsuperuser
```

### License

[MIT](LICENSE)
