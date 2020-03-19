from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector


from flask import request


APP_CONFIG = Config().config_vars

logger = getLogger()


def getInfo():
    logger.info(f'Position API : {__name__}')
    pass


def getAll():
    logger.info(f'Position API : {__name__}')
    pass
