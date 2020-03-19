from app.models.instrument.instrument import Instrument
from app.models.order.utils import VALID_ORDER_STATUS, VALID_ORDER_TYPE, VALID_ORDER_SIDE
from app.models.order.errors import InvalidOderStatusException, InvalidOderTypeException, InvalidOderSideException


class OrderSide(object):
    value: str

    def __init__(self, side):
        if side not in VALID_ORDER_SIDE:
            raise InvalidOderSideException( side )
        self.value = side
    
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str( self.value )
    
    def __call__(self):
        return self.value


class OrderStatus(object):
    value: str

    def __init__(self, status):
        if status not in VALID_ORDER_STATUS:
            raise InvalidOderStatusException( status )
        self.value = status
    
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str( self.value )
    
    def __call__(self):
        return self.value


class OrderType(object):
    value: str

    def __init__(self, orderType):
        if orderType not in VALID_ORDER_TYPE:
            raise InvalidOderTypeException( orderType )
        self.value = orderType
    
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str( self.value )
    
    def __call__(self):
        return self.value


class Order(object):
    id: str
    customID: str

    instrument: Instrument
    size: int
    leftSize: int
    side: OrderSide
    price: float
    status: OrderStatus
    statusDescription: str
    type: OrderType
    open: bool
    description: str
    timestamp: int


    def __init__(self,
        instrument: Instrument, type: OrderType, size: int, side: OrderSide, price: float,
        status: OrderStatus, open: bool, timestamp: int, desc: str = '', statusDesc: str = ''
    ):
        self.instrument = instrument
        self.type = type
        self.size = size
        self.side = side
        self.price = price
        self.status = status
        self.open = open
        self.timestamp = timestamp
        self.description = desc
        self.statusDescription = statusDesc


    def get(self, orderID: str = None, customID: str = None):
        raise NotImplementedError()


    def create(self,
        instrument: Instrument,
        size: int, side: OrderSide,
        type: OrderType,
        price: float = None, description: str = None,
        customID: str = None,
    ):
        raise NotImplementedError()


    def update(self,
        orderID: str = None, customID: str = None,
        size: int = None,
        price: str = None
    ):
        raise NotImplementedError()


    def cancell(self, orderID: str = None, customID: str = None):
        raise NotImplementedError()




