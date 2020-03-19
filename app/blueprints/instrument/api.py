from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector


from flask import request


APP_CONFIG = Config().config_vars

logger = getLogger()


def get():
    logger.info(f'Instrument API : {__name__}')
    pass


def getAll():
    logger.info(f'Instrument API : {__name__}')
    pass
