from flask import Flask, request, jsonify

from holiday_offers.filters import filter_data
from holiday_offers.retrievers import retrieve_data

app = Flask(__name__)  # pylint: disable=C0103


@app.route('/')
def hello_world():
    xml = retrieve_data()
    result = filter_data(xml, request.args)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
