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
