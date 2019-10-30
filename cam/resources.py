import cam
import json
import requests
from .exceptions import InvalidAPIKeyException, BadRequestException


class Endpoint:

    endpoint = ''

    def build_url(self, pk=None):
        path = '%s/%s/%s/' % (cam.api_base, cam.api_version, self.endpoint)
        if pk:
            path += '%s/' % pk
        return path

    def _dispatch(self, method, url, params=None, data=None):
        if data:
            data = json.dumps(data)
        headers = {'X-CAM-APIKEY': cam.api_key}
        response = getattr(requests, method.lower())(url, params=params, data=data,
                                                     headers=headers, verify=cam.verify_ssl_certs)
        if response.ok:
            return response.json()
        elif response.status_code == 400:
            raise BadRequestException(response.json())
        elif response.status_code == 401:
            raise InvalidAPIKeyException()
        response.raise_for_status()

    def list(self, params=None):
        if params is None:
            params = {}
        return self._dispatch('GET', self.build_url(), params=params)

    def read(self, pk, params=None):
        return self._dispatch('GET', self.build_url(pk), params=params)

    def create(self, data):
        return self._dispatch('POST', self.build_url(), data=data)

    def patch(self, pk, data):
        return self._dispatch('PATCH', self.build_url(pk), data=data)

    def update(self, pk, data):
        return self._dispatch('PUT', self.build_url(pk), data=data)

    def delete(self, pk):
        return self._dispatch('DELETE', self.build_url(pk))
