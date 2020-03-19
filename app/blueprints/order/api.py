from app.config import Config
from app.utils import getLogger
from app.handlers.exchange.exchange_connector import ExchangeConnector


from flask import request


APP_CONFIG = Config().config_vars

logger = getLogger()
Exchange = ExchangeConnector()


def get():
    logger.info(f'Order API : get')
    
    data = request.json
    
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    if orderID: orderID = str( orderID )
    if customID: customID = str( customID )
    instrumentName = data.get('instrumentName', None)
    if not instrumentName:
        raise ValueError('Should Specify a instrument name')
    
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return Exchange.getOrder(instrumentName, orderID=orderID, customID=customID)


def create():
    logger.info(f'Order API : get')
    
    data = request.json
    customID = data.get('customID', None)
    orderType = data.get('type', None)
    side = data.get('side', None)
    price = data.get('price', None)
    instrument = data.get('instrument', None)

    return Exchange.create(
        customID=customID,
        orderType=orderType,
        side=side,
        price=price,
        instrument=instrument
    )


def getAll():
    logger.info(f'Order API : getAll')
    return Exchange.getAllOrders()


def getOpen():
    logger.info(f'Order API : {__name__}')
    return Exchange.getOpenOrders()


def delete():
    logger.info(f'Order API : delete')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return Exchange.deleteOrder(orderID=orderID, customID=customID)


def update():
    logger.info(f'Order API : update')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    size = data.get('size', None)
    price = data.get('price', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}, size: {size}, price: {price}')

    return Exchange.updateOrder(orderID=orderID, customID=customID, size=size, price=price)


def getStops():
    logger.info(f'Order API : get')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return Exchange.getOrder(orderID=orderID, customID=customID)

def getOpenStops():
    logger.info(f'Order API : get')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return Exchange.getOrder(orderID=orderID, customID=customID)



###---###   ORDERBOOK   ###---###
def getOrderbook():
    logger.info(f'Order API : get')
    
    data = request.json
    orderID = data.get('orderID', None)
    customID = data.get('customID', None)
    logger.debug(f'orderID : {orderID}, customID: {customID}')

    return Exchange.getOrder(orderID=orderID, customID=customID)