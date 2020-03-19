from flask import Blueprint

from app.utils import getLogger
from app.blueprints.order import api as orderAPI
from app.blueprints.account import api as accountAPI
from app.blueprints.instrument import api as instrumentAPI


api = Blueprint('api', __name__, url_prefix='/api/v1')
logger = getLogger()


###---###   INSTRUMENT   ###---###
api.add_url_rule('/instrument/all', 'instrumetAll', orderAPI.getAll, methods=['GET'])
api.add_url_rule('/instrument', 'instrumet', orderAPI.get, methods=['GET'])


###---###   ORDER        ###---###
### Regular
api.add_url_rule('/order', 'order', orderAPI.get, methods=['GET'])
api.add_url_rule('/order', 'orderUpdate', orderAPI.update, methods=['PUT'])
api.add_url_rule('/order', 'orderDelete', orderAPI.delete, methods=['DELETE'])
api.add_url_rule('/order', 'orderCreate', orderAPI.create, methods=['POST'])

api.add_url_rule('/order/all', 'orderAll', orderAPI.getAll, methods=['GET'])
api.add_url_rule('/order/open', 'orderOpen', orderAPI.getOpen, methods=['GET'])

### Stop
api.add_url_rule('/stop', 'stopAll', orderAPI.getStops, methods=['GET'])
api.add_url_rule('/stop/open', 'stopOpen', orderAPI.getOpenStops, methods=['GET'])

### ORDERBOOK
api.add_url_rule('/orderbook', 'orderbook', orderAPI.getOrderbook, methods=['GET'])


###---###   ACCOUNT      ###---###
### Position
api.add_url_rule('/position', 'position', accountAPI.getPosition, methods=['GET'])

### Balance
api.add_url_rule('/balance', 'balance', accountAPI.getBalance, methods=['GET'])

### Leverage
api.add_url_rule('/leverage', 'leverage', accountAPI.getLeverage, methods=['GET'])
api.add_url_rule('/leverage', 'leverageChange', accountAPI.changeLeverage, methods=['PUT'])



