import requests, json

from app.handlers.rest.errors import ResponseMissingDataAttributeException
from app.utils import getLogger

from requests.models import Response


logger = getLogger()


REQUEST_HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

SESSION = requests.session()


class RequestHandler(object):
    @staticmethod
    def get(url: str, route: str = None, json: dict = None, params: dict = None, timeout: int = 7):
        return RequestHandler.send( 'get', url=url, route=route, json=json, params=params, timeout=timeout )
    
    @staticmethod
    def post(url: str, route: str = None, json: dict = None, params: dict = None, timeout: int = 7):
        return RequestHandler.send( 'post', url=url, route=route, json=json, params=params, timeout=timeout )
    
    @staticmethod
    def put(url: str, route: str = None, json: dict = None, params: dict = None, timeout: int = 7):
        return RequestHandler.send( 'put', url=url, route=route, json=json, params=params, timeout=timeout )

    @staticmethod
    def delete(url: str, route: str = None, json: dict = None, params: dict = None, timeout: int = 7):
        return RequestHandler.send( 'delete', url=url, route=route, json=json, params=params, timeout=timeout )


    # TODO: Add attribute for headers, if there any should update header dict
    @staticmethod
    def send(verb: str, url: str, route: str = None, params: dict = None, json: dict = None, timeout: int = 7, headers: dict = None) -> Response:
        if route: url += route
        logger.info( f'Requesting ({verb.upper()}) {url}?{params}: {json}' )
        
        sendingHeaders = REQUEST_HEADERS
        if headers: sendingHeaders.update( headers )
        logger.debug(f'HEADERS: {sendingHeaders}')

        req = requests.Request(
            verb, url, json=json, params=params, headers=sendingHeaders
        )
        prepped = SESSION.prepare_request( req )
        response = SESSION.send( prepped, timeout=timeout )

        return response

    # TODO: This should be on utils, and should be a more intuitive name, cause it checks the response, not the request
    @staticmethod
    def check_empty_attributes(attr_names: list, data: dict):
        missing_attrs = []

        for name in attr_names:
            attr = data.get( name, None )

            if not attr:
                missing_attrs.append( name )
        
        if missing_attrs:
            raise ResponseMissingDataAttributeException( missing_attrs )
