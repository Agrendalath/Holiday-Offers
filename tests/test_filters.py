import pytest as pytest
from typing import Iterator, Dict
from unittest import mock
from unittest.mock import MagicMock

from holiday_offers.constants import OUTPUT_KEYS
from holiday_offers.filters import strip_unnecessary_keys, filter_data
from tests.resources.example_offers import (
    EXAMPLE_GOOD_OFFER,
    EXAMPLE_BAD_OFFER,
)


def test_strip_unnecessary_keys():
    """"Test stripping keys for user."""
    assert len(strip_unnecessary_keys(EXAMPLE_GOOD_OFFER)) == len(OUTPUT_KEYS)
    assert strip_unnecessary_keys(EXAMPLE_BAD_OFFER) is None


def mock_data() -> Iterator[Dict[str, str]]:
    for _ in range(5):
        yield EXAMPLE_GOOD_OFFER


def mock_validator(offer: Dict[str, str], query: Dict[str, str]):
    return float(offer['Starrating']) >= float(query['star_rating'])


@mock.patch('holiday_offers.filters.parse_xml', return_value=mock_data())
@mock.patch(
    'holiday_offers.filters.validate_offer', side_effect=mock_validator
)
@pytest.mark.parametrize('stars, price, offers', [(3, 424.35, 5), (4, 0, 0)])
def test_filter_data(
    _parser: MagicMock,
    _validator: MagicMock,
    stars: float,
    price: float,
    offers: int,
):
    """Test filtering data."""
    result = filter_data('', {'star_rating': str(stars)})
    assert 'summary' in result
    assert result['summary']['most_expensive_price'] == price
    assert result['summary']['cheapest_price'] == price
    assert result['summary']['average_price'] == price

    assert 'offers' in result
    assert len(result['offers']) == offers
