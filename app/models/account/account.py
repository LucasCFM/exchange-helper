from app.models.account.leverage import Leverage
from app.models.account.position import Position


class Account(object):
    name : str
    username : str
    email : str
    TFAEnabled : bool

    APIKeyId : str
    APIPermissions : list

    totalBalance : float
    availableBalance : float
    usedBalance : float

    leverage : Leverage
    position : Position




