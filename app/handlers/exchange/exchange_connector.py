import json

from app.config import Config
from app.utils import getOperationAttempt, getLogger, getAccountExchange
from app.handlers.rest.request_handler import RequestHandler
from app.handlers.rest.response_handler import JsonResponse
from app.models.instrument.instrument import Instrument

from requests.models import Response
from requests.exceptions import HTTPError, RequestException, ConnectionError, Timeout


APP_CONFIG = Config().config_vars

EXCHANGE_URI = APP_CONFIG.EXCHANGE_CONNECTOR_URL

logger = getLogger()


class ExchangeConnector( object ):
    def __init__(self, timeout: int = 7):
        super().__init__()
        self.exchangeURI = EXCHANGE_URI
        self.timeout = timeout
    

    def requestExchange(self, endpoint: str, verb: str = 'GET', params: dict = None, data: dict = None, timeout: int = None) -> Response:
        if data:
            dataJson = json.loads( data )
        
        if not timeout:
            timeout = self.timeout

        uri = self.exchangeURI + f'/{getAccountExchange()}'

        logger.info(f'Requesting exchange: {uri}{endpoint} - {verb} - {params} - {data}')
        response = RequestHandler.send(
            verb= verb, url= uri, route= endpoint,
            params= params, json= dataJson,
            timeout= timeout
        )

        try:
            response.raise_for_status()
        except RequestException as e:
            # TODO: Define variables to store request status code and errors
            if response.status_code >= 400 and response.status_code < 500:
                opAttempt = getOperationAttempt()
                if opAttempt > APP_CONFIG.BAD_REQUEST_MAX_ATTEMPT:
                    self.accountFailover()


            requestExceptionType = type( e )
            if isinstance(e, ConnectionError) or requestExceptionType is Timeout:
                self.retryRequest()
            
            elif isinstance(e, ValueError):
                self.failover()

        logger.debug(f'Request response: {response}')
        return response


    def retryRequest(self):
        pass # TODO


    def accountFailover(self):
        pass # TODO


    def failover(self):
        pass # TODO: Sould dispose everyone and shutdown the services, app is not up to date anymore



    ###---### ORDER ###---###
    def getOrder(self, orderID: str = None, customID: str = None) -> Response:
        if not orderID and not customID:
            raise AttributeError( f'Must specify a order ID or custom ID' )
        
        if orderID and customID:
            logger.warning(f'Both order ID and custom ID was infromed, gonna use order ID')

        endpoint = '/order'
        if orderID:
            attrs = {'orderId': orderID}
        else:
            attrs = {'orderId': customID} # TODO : Ask Guilherme if there custom id implemented
        
        logger.info(f'Getting order: {attrs}')
        return self.requestExchange(endpoint, params=attrs)


    def getAllOrders(self) -> Response:
        logger.info(f'Getting all orders')

        endpoint = '/order/all'
        return self.requestExchange(endpoint)


    def getOpenOrders(self) -> Response:
        logger.info(f'Getting open orders')

        endpoint = '/order/open'
        return self.requestExchange(endpoint)


    def updateOrder(self, orderID: str = None, customID: str = None, size: int = None, price: float = None) -> Response:
        if not orderID and not customID:
            raise AttributeError( f'Must specify a order ID or custom ID' )
        
        if orderID and customID:
            logger.warning(f'Both order ID and custom ID was infromed, gonna use order ID')

        endpoint = '/order'
        if orderID:
            attrs = {'orderId': orderID}
        else:
            attrs = {'orderId': customID} # TODO : Ask Guilherme if there custom id implemented
        
        logger.info(f'Getting order: {attrs}')
        return self.requestExchange(endpoint, params=attrs)


    def deleteOrder(self, orderID: str = None, customID: str = None) -> Response:
        if not orderID and not customID:
            raise AttributeError( f'Must specify a order ID or custom ID' )
        
        if orderID and customID:
            logger.warning(f'Both order ID and custom ID was infromed, gonna use order ID')

        endpoint = '/order'
        if orderID:
            attrs = {'orderId': orderID}
        else:
            attrs = {'orderId': customID} # TODO : Ask Guilherme if there custom id implemented
        
        logger.info(f'Getting order: {attrs}')
        return self.requestExchange(endpoint, params=attrs)


    def deleteAllOrders(self) -> Response:
        logger.info(f'Getting all orders')

        endpoint = '/order/delete/all'
        return self.requestExchange(endpoint)
    

    def getAllStops(self, instrument: Instrument) -> Response:
        logger.info(f'Getting open orders')

        endpoint = '/stop'
        attrs = {'instrumentName': str(instrument)}

        return self.requestExchange(endpoint, params=attrs)
    

    def getOpenStops(self, instrument: Instrument) -> Response:
        logger.info(f'Getting open orders')

        endpoint = '/stop/open'
        attrs = {'instrumentName': str(instrument)}

        return self.requestExchange(endpoint, params=attrs)



    ######### ACCOUNT #########
    ###---### Position ###---###
    def getPosition(self, instrument: Instrument) -> Response:
        logger.info(f'Getting all orders')

        endpoint = '/position'
        attrs = {'instrumentName': str(instrument)}
        
        return self.requestExchange(endpoint, params=attrs)
    

    def getBalance(self, instrument: Instrument) -> Response:
        logger.info(f'Getting all orders')

        endpoint = '/balance'
        attrs = {'instrumentName': str(instrument)}
        
        return self.requestExchange(endpoint, params=attrs)



    ###---### Instrument ###---###
    def getInstrumentInfo(self) -> Response:
        logger.info(f'Getting all orders')

        endpoint = '/instrument/all'
        return self.requestExchange(endpoint)


    def getInstrumentInfo(self, instrument: Instrument) -> Response:
        logger.info(f'Getting all orders')

        endpoint = '/instrument'
        attrs = {'instrumentName': str(instrument)}
        
        return self.requestExchange(endpoint, params=attrs)

    

