#!/bin/bash

mkdir -p .envs/.local .envs/.prod

# Read environment variables
echo "Input development environment variables"

read -p "POSTGRES_USER [postgres]: " POSTGRES_USER
POSTGRES_USER=${POSTGRES_USER:-postgres}

stty -echo
printf "POSTGRES_PASSWORD: "
read POSTGRES_PASSWORD
stty echo
printf "\n"

read -p "POSTGRES_DB [horizon_dev]: " POSTGRES_DB
POSTGRES_DB=${POSTGRES_DB:-horizon_dev}

read -p "POSTGRES_HOST [localhost]: " POSTGRES_HOST
POSTGRES_HOST=${POSTGRES_HOST:-localhost}

read -p "POSTGRES_PORT [5432]: " POSTGRES_PORT
POSTGRES_PORT=${POSTGRES_PORT:-5432}

read -p "VUE_APP_NAME [Horizon]: " VUE_APP_NAME
VUE_APP_NAME=${VUE_APP_NAME:-Horizon}



# Write environment variables to files
cat > .envs/.local/.django <<EOL
DJANGO_READ_DOT_ENV_FILE=0
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=$(openssl rand -hex 32)
EOL

cat > .envs/.local/.postgres <<EOL
POSTGRES_USER=${POSTGRES_USER}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
POSTGRES_DB=${POSTGRES_DB}
POSTGRES_HOST=db
POSTGRES_PORT=${POSTGRES_PORT}
EOL

cat > server/config/.env <<EOL
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=$(openssl rand -hex 32)
POSTGRES_USER=${POSTGRES_USER}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
POSTGRES_DB=${POSTGRES_DB}
POSTGRES_HOST=${POSTGRES_HOST}
POSTGRES_PORT=${POSTGRES_PORT}
EOL

cat > client/.env <<EOL
VUE_APP_NAME=${VUE_APP_NAME}
VUE_APP_ENV=development
EOL


# Create PostgreSQL database
psql -U $POSTGRES_USER -c "CREATE DATABASE $POSTGRES_DB;"


# Install npm dependencies
cd client
npm install

# Create virtual environment and install requirements
cd ../server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/local.txt

# Migrate and create superuser
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py migrate
python manage.py createsuperuser

# Run Django development server
python manage.py runserver


