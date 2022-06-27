#!/usr/bin/env bash

export FLASK_APP=main
export FLASK_ENV=development
flask init-db
flask run -h localhost -p 5001