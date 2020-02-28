from app.models.instrument.instrument import Instrument
from app.models.account.leverage import Leverage


class Position(object):
    instrument : Instrument
    size : int
    balanceUsed : float
    entryPrice : float
    pnlPercentage : float
    leverage : Leverage

    def get(self):
        pass
