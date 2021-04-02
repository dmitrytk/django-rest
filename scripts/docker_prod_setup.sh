#!/bin/bash

mkdir -p .envs/.prod

# Read Docker production environment variables
echo "
### Input Docker production env variables ###
"

read -p "DJANGO_ALLOWED_HOSTS [example.com]: " DJANGO_ALLOWED_HOSTS
DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS:-example.com}

read -p "POSTGRES_PROD_USER [postgres]: " POSTGRES_PROD_USER
POSTGRES_PROD_USER=${POSTGRES_PROD_USER:-postgres}

stty -echo
printf "POSTGRES_PROD_PASSWORD: "
read POSTGRES_PROD_PASSWORD
stty echo
printf "\n"

read -p "POSTGRES_PROD_DB [horizon_dev]: " POSTGRES_PROD_DB
POSTGRES_PROD_DB=${POSTGRES_PROD_DB:-horizon_dev}

read -p "POSTGRES_PROD_PORT [5432]: " POSTGRES_PROD_PORT
POSTGRES_PROD_PORT=${POSTGRES_PROD_PORT:-5432}

read -p "VUE_APP_PROD_NAME [Horizon]: " VUE_APP_PROD_NAME
VUE_APP_PROD_NAME=${VUE_APP_PROD_NAME:-Horizon}


# Write Docker production environment variables to files
cat > .envs/.prod/.django <<EOL
DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}
DJANGO_READ_DOT_ENV_FILE=0
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=$(openssl rand -hex 32)
EOL

cat > .envs/.prod/.postgres <<EOL
POSTGRES_USER=${POSTGRES_PROD_USER}
POSTGRES_PASSWORD=${POSTGRES_PROD_PASSWORD}
POSTGRES_DB=${POSTGRES_PROD_DB}
POSTGRES_HOST=db
POSTGRES_PORT=${POSTGRES_PROD_PORT}
EOL

cat > .envs/.prod/.vue <<EOL
VUE_APP_NAME=${VUE_APP_PROD_NAME}
VUE_APP_ENV=production
EOL