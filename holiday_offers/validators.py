from typing import Dict, Union
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.exceptions import BadRequest

from holiday_offers.constants import FILTERS
from holiday_offers.helpers import str_to_time


def validate_offer(
    offer: Dict[str, str], query: Union[ImmutableMultiDict, Dict[str, str]]
) -> bool:
    """
    Check if offer meets the user's requirements.
    :param offer: non-stripped offer
    :param query: user's query params
    :return: bool
    """
    # Check if all needed keys are present in offer.
    if not set(FILTERS.values()) <= offer.keys():
        # TODO: Handle logging
        return False

    for key in query:
        if key not in FILTERS:
            raise BadRequest(f"Unknown parameter: {key}")

        this = offer.get(FILTERS[key])
        desired = query.get(key)

        if key in ('star_rating', 'min_price', 'max_price'):
            try:
                this = float(this)
                desired = float(desired)
            except ValueError:
                raise BadRequest(f"{desired} is not valid value for {key}")

        else:
            try:
                this = str_to_time(this)
                desired = str_to_time(desired)
            except ValueError:
                raise BadRequest(f"Invalid time format for {key}")

        if key == 'max_price':
            if this > desired:
                return False
        elif this < desired:
            return False

    return True
