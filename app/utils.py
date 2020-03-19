import logging
from logging import Logger

from flask import request

from app.handlers.warn_informer.informer import Informer
from app.handlers.rest.errors import RequestWithoutExchangeException


def getLogger(name='main') -> Logger:
    return logging.getLogger(name)


def getOperationAttempt() -> int:
    opAttempt = request.headers.get('OP-ATTEMPT', None)
    opAttempt = request.headers.get('OP-ATTEMPT', 1) # TODO: TO REMOVE
    if not opAttempt:
        Informer.sendWarn('OPERATION WITHOUT ATTEMP HEADER')
        opAttempt = 2
    
    return int( opAttempt )


def getAccountExchange() -> str:
    exchange = request.headers.get('EXCHANGE', None)
    exchange = request.headers.get('EXCHANGE', 'binance') # TODO: TO REMOVE
    if not exchange:
        Informer.sendWarn('OPERATION WITHOUT EXCHANGE')
        raise RequestWithoutExchangeException()
    
    return exchange


def getAccountID() -> str:
    accountID = request.headers.get('ACCOUNT-ID', None)
    accountID = request.headers.get('ACCOUNT-ID', 'test') # TODO: TO REMOVE
    if not accountID:
        Informer.sendWarn('OPERATION WITHOUT ACCOUNT ID')
        raise RequestWithoutExchangeException() # TODO:
    
    return accountID
