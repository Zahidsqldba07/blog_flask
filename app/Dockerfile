# syntax=docker/dockerfile:1

ARG VERSION=alpine
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
LABEL key="app"
WORKDIR /var/www
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 5001
