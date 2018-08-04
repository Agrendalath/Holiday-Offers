from datetime import datetime


def generate_endpoint(**kwargs) -> str:
    """
    Generate full endpoint URL from parameters or default ones.
    :param kwargs: Parameters.
    :return: Generated URL.
    """
    protocol = kwargs.get('protocol', 'http')
    hostname = kwargs.get('hostname', '127.0.0.1')
    port = kwargs.get('port', '8000')
    api = kwargs.get('api', 'search')
    return f'{protocol}://{hostname}:{port}/{api}'


def str_to_time(data: str) -> datetime.time:
    """
    Convert string from user to time object.
    :param data: datetime or date string
    :return: time object
    :raises ValueError if format is wrong
    """
    try:
        return datetime.strptime(data, '%d/%m/%Y %H:%M').time()
    except ValueError:
        try:
            return datetime.strptime(data, '%H:%M').time()
        except ValueError as ex:
            raise ex
