import json
import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

logging.basicConfig(
    filename='logs/api_service.log',
    filemode='a',
    format='%(asctime)s in %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%b-%d %H:%M:%S %Z',
    level=logging.DEBUG
)

logger = logging.getLogger("API Service")

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
def index():
    return 'OK', 200

class Players(Resource):
    def get(self):
        data_filename = 'rushing.json'
        try:
            data_file = open(data_filename, 'r')
            return json.load(data_file)
        except FileNotFoundError:
            logger.error(f"Unable to find file {data_filename}")
            return []


api.add_resource(Players, '/players')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8001')
