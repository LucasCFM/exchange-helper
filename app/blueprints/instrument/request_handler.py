from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector

from app.models.instrument.instrument import Instrument


APP_CONFIG = Config().config_vars

logger = getLogger()


def handleGet() -> Instrument:
    logger.info(f'Instrument API : {__name__}')
    