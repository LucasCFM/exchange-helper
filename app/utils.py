from flask import request

from app.handlers.warn_informer.informer import Informer


def getOperationAttempt():
    opAttempt = request.headers.get('OP-ATTEMPT', None)
    if not opAttempt:
        Informer.sendWarn('OPERATION WITHOUT ATTEMP HEADER')
        opAttempt = 2
    
    return int( opAttempt )
