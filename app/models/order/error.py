
class InvalidOderStatusException(Exception):
    def __init__(self, orderStatus: str):
        msg = f'{orderStatus} is not a valid order status'
        super().__init__( orderStatus )


class InvalidOderTypeException(Exception):
    def __init__(self, orderType: str):
        msg = f'{orderType} is not a valid order type'
        super().__init__( orderType )


class InvalidOderSideException(Exception):
    def __init__(self, orderSide: str):
        msg = f'{orderSide} is not a valid order side'
        super().__init__( orderSide )
