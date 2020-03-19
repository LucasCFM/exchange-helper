from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector

from app.models.account.leverage import Leverage


APP_CONFIG = Config().config_vars

logger = getLogger()


def handleGet() -> Leverage:
    logger.info(f'Leverage API : {__name__}')
    