from holiday_offers.helpers import generate_endpoint

ENDPOINT = generate_endpoint(
    hostname='87.102.127.86',
    port='8100',
    api='search/searchoffers.dll?page=SEARCH&platform=WEB&depart=LGW%7CSTN%7CLHR%7CLCY%7CSEN%7CLTN&countryid=1&regionid=4&areaid=9&resortid=0&depdate=15%2F08%2F2018&flex=0&adults=2&children=0&duration=7',  # noqa pylint: disable=C0301
)

OUTPUT_KEYS = [
    'Sellprice',
    'Starrating',
    'Hotelname',
    'Inboundfltnum',
    'Outboundfltnum',
    'Inboundarr',
    'Inbounddep',
]

FILTERS = {
    'earliest_departure_time': 'Outbounddep',
    'earliest_return_time': 'Inbounddep',
    'min_price': 'Sellprice',
    'max_price': 'Sellprice',
    'star_rating': 'Starrating',
}
