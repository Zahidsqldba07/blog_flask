#!/usr/bin/env bash

export $(echo $(cat .flaskenv | sed 's/#.*//g'| xargs))

flask run init-db
flask run -h $FLASK_RUN_HOST -p $FLASK_RUN_PORT
