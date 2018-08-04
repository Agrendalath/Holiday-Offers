from datetime import datetime

from typing import Dict
from werkzeug.datastructures import ImmutableMultiDict

from holiday_offers.constants import FILTERS


def validate_offer(offer: Dict[str, str], query: ImmutableMultiDict) -> bool:
    """
    Check if offer meets the user's requirements.
    :param offer: non-stripped offer
    :param query: user's query params
    :return: bool
    """
    for key in query:
        this = offer.get(FILTERS[key])
        desired = query.get(key)

        if key in ('star_rating', 'min_price', 'max_price'):
            try:
                this = float(this)
                desired = float(desired)
            except ValueError:
                # TODO: Handle Bad Request
                pass

        else:
            try:
                this = datetime.strptime(this, '%d/%m/%Y %H:%M').time()
                desired = datetime.strptime(desired, '%H:%M').time()
            except AttributeError:
                # TODO: Handle Bad Request
                pass

        if key == 'max_price':
            if this > desired:
                return False
        elif this < desired:
            return False

    return True
