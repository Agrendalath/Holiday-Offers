#!/bin/bash
FLASK_APP=holiday_offers/app.py \
FLASK_ENV=development \
FLASK_DEBUG=1 \
pipenv run flask run --host=0.0.0.0
