from datetime import time
from typing import Dict

from holiday_offers.helpers import generate_endpoint, str_to_time
import pytest


@pytest.mark.parametrize(
    'custom_kwargs, expected',
    [
        ({}, 'http://127.0.0.1:8000/search'),
        (
            {
                'hostname': 'example.com',
                'port': '8080',
                'api': 'test',
                'protocol': 'https',
            },
            'https://example.com:8080/test',
        ),
    ],
)
def test_generate_endpoint(custom_kwargs: Dict[str, str], expected: str):
    """Test generating endpoint."""
    assert generate_endpoint(**custom_kwargs) == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        ('15/08/2018 14:35', time(hour=14, minute=35)),
        ('1/01/1999 00:00', time(hour=0, minute=0)),
        ('12:12', time(hour=12, minute=12)),
        ('00:00', time(hour=0, minute=0)),
    ],
)
def test_str_to_time(data, expected):
    """Test string to time converter."""
    assert str_to_time(data) == expected
