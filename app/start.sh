# !/usr/bin/env bash

export $(echo $(cat .flaskenv | sed 's/#.*//g'| xargs))
