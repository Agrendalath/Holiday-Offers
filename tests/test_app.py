import pytest
from flask import url_for

from holiday_offers.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()


def test_response(client):
    """A simple integration test to see if everything pairs well."""
    with app.test_request_context():
        response = client.get(url_for('parse')).get_json()
    assert 'summary' in response
    assert 'offers' in response
