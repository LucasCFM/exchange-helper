from flask import jsonify


class JsonResponse(object):
    def __init__(self, message, status_code: int):
        """
        Class JsonResponse
        Creates a jsonified response
        :param message: response message
        :param status_code: http status code
        """
        self._message = message
        self._status_code = status_code

    def get_response(self, success: bool):
        """
        Gets jsonified response tuple
        :param success: True or False
        :return:
        """
        return jsonify( {'success': success, 'message': self._message} ), self._status_code

    @staticmethod
    def success(message):
        """
        Sugar method for success response
        :param message: response message
        :return: jsonified response
        """
        return JsonResponse( message, 200 ).get_response( True )
    
    @staticmethod
    def accepted(message):
        """
        Sugar method for accepted response
        Accepted means that it was gotten, 
            but nothing is gonna happen now (mainly cause it is already happenning)
        :param message: response message
        :return: jsonified response
        """
        return JsonResponse( message, 202 ).get_response( True )

    @staticmethod
    def failure(message='Internal server error.', status_code: int = 500):
        """
        Sugar method for error response
        :param message: error message
        :param status_code: http error code (400s and 500s)
        :return: jsonified response
        """
        return JsonResponse( message, status_code ).get_response( False )
