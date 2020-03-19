from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector


from flask import request


APP_CONFIG = Config().config_vars

logger = getLogger()


def getPosition():
    logger.info(f'Leverage API : {__name__}')
    pass


def getBalance():
    logger.info(f'Leverage API : {__name__}')
    pass


def getLeverage():
    logger.info(f'Leverage API : {__name__}')
    pass


def changeLeverage():
    logger.info(f'Leverage API : {__name__}')
    pass
