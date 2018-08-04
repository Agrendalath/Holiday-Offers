import requests

from .constants import ENDPOINT


def retrieve_data():
    response = requests.get(ENDPOINT)
    return response.content
