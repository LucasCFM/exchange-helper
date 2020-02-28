from app.models.instrument.orderbook import OrderBook
from app.models.instrument.funding import Funding


class Instrument(object):
    tickSize : float
    maxLeverage : float

    currentPrice : float
    currentMarkPrice : float
    bidPrice : float
    askPrice : float

    takerFee : float
    makerFee : float

    funding : Funding
    orderBook : OrderBook



    def getInfo(self):
        pass


    def getPriceInfo(self):
        pass


    def getFeeInfo(self):
        pass
