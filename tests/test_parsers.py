from holiday_offers.parsers import parse_xml


def test_parse_xml():
    with open('tests/resources/example.xml') as file:
        xml_data = file.read()

    result = list(parse_xml(xml_data))
    assert len(result) == 216
