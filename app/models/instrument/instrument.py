from app.models.instrument.orderbook import OrderBook
from app.models.instrument.funding import Funding
from app.models.instrument.utils import VALID_INSTRUMENT_NAMES
from app.models.instrument.errors import InvalidInstrumentNameException


class Instrument(object):
    name : str
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

    def __init__(self, name: str):
        if name not in VALID_INSTRUMENT_NAMES:
            raise InvalidInstrumentNameException( name )
        self.name = name


    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str( self.name )
    
    def __call__(self):
        return self.name


    def getInfo(self):
        raise NotImplementedError()


    def getPriceInfo(self):
        raise NotImplementedError()


    def getFeeInfo(self):
        raise NotImplementedError()
