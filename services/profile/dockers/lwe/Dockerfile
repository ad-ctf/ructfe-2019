FROM python:3.6-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && rm -rf /var/lib/apt/lists/*

ADD . /app
WORKDIR /app

RUN python setup.py develop

EXPOSE 11111
