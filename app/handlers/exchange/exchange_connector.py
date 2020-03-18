import json

from app.config import Config
from app.utils import getOperationAttempt
from app.handlers.rest.request_handler import RequestHandler
from app.handlers.rest.response_handler import JsonResponse

from requests.exceptions import HTTPError, RequestException, ConnectionError, Timeout


APP_CONFIG = Config().config_vars

EXCHANGE_URI = APP_CONFIG.EXCHANGE_CONNECTOR_URL


class ExchangeConnector( object ):
    def __init__(self, timeout: int = 7):
        super().__init__()
        self.exchangeURI = EXCHANGE_URI
        self.timeout = timeout
    

    def requestExchange(self, endpoint: str, verb: str = 'GET', params: dict = None, data: dict = None, timeout: int = None):
        if data:
            dataJson = json.loads( data )
        
        if not timeout:
            timeout = self.timeout

        response = RequestHandler.send( 
            verb= verb, url= self.exchangeURI, route= endpoint,
            params= params, json= dataJson,
            timeout= timeout
        )

        try:
            response.raise_for_status()
        except RequestException as e:
            if response.status_code >= 400 and response.status_code < 500:
                opAttempt = getOperationAttempt()
                if opAttempt > APP_CONFIG.BAD_REQUEST_MAX_ATTEMPT:
                    self.accountFailover()


            requestExceptionType = type( e )
            if isinstance(e, ConnectionError) or requestExceptionType is Timeout:
                self.retryRequest()
            
            elif isinstance(e, ValueError):
                self.failover()

            return response


    def retryRequest(self):
        pass # TODO


    def accountFailover(self):
        pass


    def failover(self):
        pass # TODO: Sould dispose everyone and shutdown the services, app is not up to date anymore



    ###---### ORDER ###---###
    def getOrder(self, orderID: str = None, customID: str = None):
        if not orderID and not customID:
            raise AttributeError( f'' ) # TODO

