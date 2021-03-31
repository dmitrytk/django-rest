# Horizon geological database

> ### Django and PostgreSQL app with Vue.js front-end

### Run locally

#### Requirements

- Python 3.7+
- PostgreSQL 11+
- Node.js 12+

Clone repository.

```
git clone git@github.com:dmitrytk/horizon.git
cd horizon
```

Create Postgresql database for project.

Create and activate Python virtual environment.

```
cd server
python3 -m venv venv
source venv/bin/activate
```

Install Python requirements.

```
pip install -r requirements/local.txt
```

Create server/config/.env file and populate environment variables.

```
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=<your_secret_key>
POSTGRES_DB=<db_name>
POSTGRES_USER=<db_user>
POSTGRES_PASSWORD=<db_password>
POSTGRES_HOST=<db_host>
POSTGRES_PORT=<db_port>
```

Create client/.env file and populate environment variables.

```
VUE_APP_NAME=<app_name>
VUE_APP_ENV=development
```

Migrate and create superuser.

```
python manage.py migrate --settings=config.settings.local
python manage.py createsuperuser --settings=config.settings.local
```

Install Node dependencies.

```
cd client
npm install
```

Run development server.

```
cd server
python manage.py runserver --settings=config.settings.local
```

```
cd client
npm run serve
```


### License

[MIT](LICENSE)
