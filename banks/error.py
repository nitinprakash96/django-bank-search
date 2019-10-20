from rest_framework.exceptions import APIException

class QueryParameterException(APIException):
	"""A custom class to instantiate error codes on 
	missing query parameter while making requests to the server.
	"""
	status_code = 400
	default_detail = 'Expected parameters are missing.'
	default_code = 'query_param_error'