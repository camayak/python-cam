
class InvalidAPIKeyException(Exception):
    """
    An exception raised when the Cam API responds with
    an HTTP 401 - the API key does not exist or is inactive.
    """
    pass
