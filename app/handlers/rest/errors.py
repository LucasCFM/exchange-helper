class ResponseMissingDataAttributeException(Exception):
    attrs = []
    
    def __init__(self, attrs: list, *args, **kwargs):
        msg = f'Request is missing data attribute: {attrs}'
        super( ResponseMissingDataAttributeException, self ).__init__( msg, *args, **kwargs )
        self.set_attrs( attrs )
    
    def set_attrs(self, attrs: list):
        self.attrs = attrs

    def get_attrs(self):
        return self.attrs


# TODO: TO FINISH
class AccountFailOverException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# TODO: TO FINISH
class RequestWithoutExchangeException(AccountFailOverException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
