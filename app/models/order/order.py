from app.models.instrument.instrument import Instrument
from app.models.order.utils import VALID_ORDER_STATUS, VALID_ORDER_TYPE, VALID_ORDER_SIDE
from app.models.order.error import InvalidOderStatusException, InvalidOderTypeException, InvalidOderSideException


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
        instrument: Instrument, size: int, side: OrderSide
    )


    def get(self, orderID: str = None, customID: str = None):
        if not orderID and not customID:
            raise Exception('Must specify a ID or custom one')
        pass


    def create(self,
        instrument: Instrument,
        size: int, side: OrderSide,
        type: OrderType,
        price: float = None, description: str = None,
        customID: str = None,
    ):
        pass


    def update(self,
        orderID: str = None, customID: str = None,
        size: int = None,
        price: str = None
    ):
        if not orderID and not customID:
            raise Exception('Must specify a ID or custom one')
        if not size and not price:
            raise Exception('Must specify a size or price to update/change')
        pass


    def cancell(self, orderID: str = None, customID: str = None):
        if not orderID and not customID:
            raise Exception('Must specify a ID or custom one')
        pass




