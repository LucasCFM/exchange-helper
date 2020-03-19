from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector

from app.models.instrument.orderbook import OrderBook


APP_CONFIG = Config().config_vars

logger = getLogger()


def handleGet() -> OrderBook:
    logger.info(f'OrderBook API : {__name__}')
