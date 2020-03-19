from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector

from app.models.order.order import Order


APP_CONFIG = Config().config_vars

logger = getLogger()


def handleGet() -> Order:
    logger.info(f'Order API : {__name__}')
    