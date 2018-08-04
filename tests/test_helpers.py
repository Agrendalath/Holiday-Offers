from holiday_offers.helpers import generate_endpoint


def test_generate_endpoint():
    custom_kwargs = {
        'hostname': 'example.com',
        'port': '8080',
        'api': 'test',
        'protocol': 'https',
    }
    assert generate_endpoint() == 'http://127.0.0.1:8000/search'
    assert (
        generate_endpoint(**custom_kwargs) == 'https://example.com:8080/test'
    )
