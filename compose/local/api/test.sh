#!/bin/bash
set -x

pipenv run pylint holiday_offers
pipenv run black --check holiday_offers
pipenv check
pipenv run coverage run -m pytest
pipenv run coverage report
