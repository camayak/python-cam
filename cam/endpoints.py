from .resources import Endpoint


class Users(Endpoint):
    endpoint = 'users'


class Organizations(Endpoint):
    endpoint = 'organizations'


class Requests(Endpoint):
    endpoint = 'requests'


class RequestContributors(Endpoint):
    endpoint = 'request_contributors'


class Assets(Endpoint):
    endpoint = 'assets'

