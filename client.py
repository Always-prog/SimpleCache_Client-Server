import requests
import logging
from typing import AnyStr


class CacheClient:
    def __init__(self, endpoint_url: str):
        """
        :param endpoint_url: full url where is CacheServer running. Example: 'http://localhost:8000'
        """
        self.endpoint_url = endpoint_url
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def get_cache(self, key: str) -> AnyStr or None:
        """
        :param key: string key that you have cached already in set_cache
        :return: value, or none if it not exists.
        :rtype: string or None
        """
        logging.info(f'Getting cache by key {key}')
        _response = requests.get(self.endpoint_url, json={'key': key})
        _json = _response.json()
        if _json['status_code'] == 404:
            logging.error(f'Key {key} not exists')
            return

        return _json['value']

    def set_cache(self, key: str, value: str) -> bool:
        """
        :param key: Key
        :param value: Value
        :return: True - if it has set, else - False
        :rtype: bool
        """
        logging.info(f'Requesting settings cache with key {key}')
        _response = requests.post(self.endpoint_url, json={'key': key, 'value': value})
        _json = _response.json()

        if _json['status_code'] != 200:
            logging.error(_json['detail'])
            return False
        logging.info(_json['detail'])

        return True

