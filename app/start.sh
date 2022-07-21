#!/usr/bin/env bash

export $(echo $(cat .flaskenv | sed 's/#.*//g'| xargs))

app="blog-app"
docker build -t ${app} .
docker run -d -p ${FLASK_RUN_PORT}:80 -t ${app}

# python3 -m flask run init-db
# python3 -m flask run -h $FLASK_RUN_HOST -p $FLASK_RUN_PORT
