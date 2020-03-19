from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector


from flask import request


APP_CONFIG = Config().config_vars

logger = getLogger()


def get():
    logger.info(f'Order API : get')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    response = ExchangeConnector.getOrder(orderID=orderID, customID=customID)

    responseJson = response.json()
    responseJson





def getAll():
    logger.info(f'Order API : getAll')
    return ExchangeConnector.getAllOrders()


def getOpen():
    logger.info(f'Order API : {__name__}')
    return ExchangeConnector.getOpenOrders()


def delete():
    logger.info(f'Order API : delete')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return ExchangeConnector.deleteOrder(orderID=orderID, customID=customID)


def update():
    logger.info(f'Order API : update')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    size = data.get('size', None)
    price = data.get('price', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}, size: {size}, price: {price}')

    return ExchangeConnector.updateOrder(orderID=orderID, customID=customID, size=size, price=price)


def getStops():
    logger.info(f'Order API : get')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return ExchangeConnector.getOrder(orderID=orderID, customID=customID)
