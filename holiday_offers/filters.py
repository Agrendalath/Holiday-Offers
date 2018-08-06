from typing import Dict, Union, List
from werkzeug.datastructures import ImmutableMultiDict

from holiday_offers.constants import OUTPUT_KEYS
from holiday_offers.parsers import parse_xml
from holiday_offers.validators import validate_offer


def strip_unnecessary_keys(
    offer: Dict[str, str]
) -> Union[Dict[str, str], None]:
    """
    Strip keys that should not be returned to user.
    :param offer: offer retrieved from XML
    :return: offer ready to be sent to user
    """
    result = None
    try:
        result = {key: offer[key] for key in OUTPUT_KEYS}
    except KeyError:
        # TODO: Handle logging.
        pass

    return result


def filter_data(
    xml_data: str, query: Union[ImmutableMultiDict, Dict[str, str]]
) -> Dict[str, Union[Dict[str, str], List[Dict[str, str]]]]:
    """
    Retrieve offers from XML and filter them according to query params.
    :param xml_data: retrieved XML
    :param query: user's query params
    :return: list of offers ready to be sent to user
    """
    max_price: float = float('-inf')
    min_price: float = float('inf')
    avg_price: float = 0

    result: Dict[str, Union[Dict[str, str], List[Dict[str, str]]]] = {
        'offers': []
    }

    for offer in parse_xml(xml_data):
        if validate_offer(offer, query):
            try:
                offer = strip_unnecessary_keys(offer)
            except KeyError:
                # TODO: Handle logging.
                continue

            result['offers'].append(offer)

            try:
                current_price = float(offer['Sellprice'])
                max_price = max(max_price, current_price)
                min_price = min(min_price, current_price)
                avg_price += current_price
            except (KeyError, ValueError, TypeError):
                # TODO: Handle logging.
                pass

    if result['offers']:
        avg_price /= len(result['offers'])
    else:
        max_price = min_price = 0

    result['summary'] = {
        'most_expensive_price': round(max_price, 2),
        'cheapest_price': round(min_price, 2),
        'average_price': round(avg_price, 2),
    }

    return result
