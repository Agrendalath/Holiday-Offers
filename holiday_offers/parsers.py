# noinspection PyPep8Naming
import xml.etree.ElementTree as ET
from typing import Iterator, Dict


def parse_xml(xml_data: str) -> Iterator[Dict[str, str]]:
    """
    Generate offers from received XML.
    :param xml_data: received XML
    :return: iterator for offers
    """
    for offer in ET.fromstring(xml_data).findall('./Results/Offer'):
        offer: ET.Element = offer
        yield offer.attrib
