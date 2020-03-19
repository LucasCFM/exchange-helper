class InvalidInstrumentNameException(ValueError):
    def __init__(self, name: str):
        msg = f'{name} is not a valid instrument name'
        super().__init__( name )
