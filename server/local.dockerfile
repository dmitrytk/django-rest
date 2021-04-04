FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt upgrade
RUN apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements /usr/src/app/requirements
RUN pip install -r ./requirements/local.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]