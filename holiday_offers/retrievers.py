import requests

from holiday_offers.constants import ENDPOINT


def retrieve_data():
    response = requests.get(ENDPOINT)
    return response.content
