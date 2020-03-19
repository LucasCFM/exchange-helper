from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector

from app.models.account.position import Position


APP_CONFIG = Config().config_vars

logger = getLogger()


def handleGet() -> Position:
    logger.info(f'Position API : {__name__}')
    