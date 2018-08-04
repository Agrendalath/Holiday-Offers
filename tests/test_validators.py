import pytest
from typing import Dict
from werkzeug.exceptions import BadRequest

from holiday_offers.validators import validate_offer
from tests.resources.example_offers import (
    EXAMPLE_GOOD_OFFER,
    EXAMPLE_BAD_OFFER,
)


@pytest.mark.parametrize(
    'params, expected',
    [
        ({'star_rating': '3'}, True),
        ({'star_rating': '4'}, False),
        ({'min_price': '424.35'}, True),
        ({'min_price': '424.36'}, False),
        ({'max_price': '424.35'}, True),
        ({'max_price': '424.34'}, False),
        ({'earliest_departure_time': '14:35'}, True),
        ({'earliest_departure_time': '14:36'}, False),
        ({'earliest_return_time': '20:05'}, True),
        ({'earliest_return_time': '20:06'}, False),
    ],
)
def test_validate_offer(params: Dict[str, str], expected: bool):
    """Test offer validator."""
    assert validate_offer(EXAMPLE_GOOD_OFFER, params) is expected


@pytest.mark.parametrize(
    'params',
    [
        ({'star_rating': 'debug'}),
        ({'earliest_departure_time': '0000'}),
        ({'debug': '123'}),
    ],
)
def test_validate_offer_invalid_value(params: Dict[str, str]):
    """Test invalid params for validator."""
    with pytest.raises(BadRequest):
        validate_offer(EXAMPLE_GOOD_OFFER, params)


def test_validate_offer_invalid_offer():
    assert validate_offer(EXAMPLE_BAD_OFFER, {}) is False
