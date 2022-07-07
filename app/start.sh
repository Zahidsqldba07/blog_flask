#!/usr/bin/env bash

export $(echo $(cat .flaskenv | sed 's/#.*//g'| xargs))

export FLASK_APP=$FLASK_APP
export FLASK_ENV=development
flask init-db
flask run -h $FLASK_RUN_HOST -p $FLASK_RUN_PORT
