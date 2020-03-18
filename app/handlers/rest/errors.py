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
