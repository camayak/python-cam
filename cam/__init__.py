from .endpoints import Users, Organizations, Requests, RequestContributors, Assets

# Configuration variables
api_key = None
api_base = 'https://connect.justask.cam'
api_version = 'v1'
verify_ssl_certs = True

users = Users()
organizations = Organizations()
requests = Requests()
contributors = RequestContributors()
assets = Assets()
