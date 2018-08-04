from holiday_offers.constants import OUTPUT_KEYS
from holiday_offers.filters import strip_unnecessary_keys
from tests.resources.example_offers import (
    EXAMPLE_GOOD_OFFER,
    EXAMPLE_BAD_OFFER,
)


def test_strip_unnecessary_keys():
    """"Test stripping keys for user."""
    assert len(strip_unnecessary_keys(EXAMPLE_GOOD_OFFER)) == len(OUTPUT_KEYS)
    assert strip_unnecessary_keys(EXAMPLE_BAD_OFFER) is None
