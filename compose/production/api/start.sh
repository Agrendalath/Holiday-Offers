#!/bin/bash
pipenv run gunicorn --bind 0.0.0.0 --workers=4 holiday_offers.app:app
