import json

from constants import approved_urls
import requests.auth
from requests.auth import HTTPBasicAuth
import logging
from constants import CMC_PROD_ENDPOINT, LATEST_TOKENS_CMC, CRYPTO_META_DATA_CMC, LATEST_QUOTES_CMC
import os


class CollectorApiClient:
    def __init__(self, url: str, api_key: str):
        if approved_urls[url]:
            self.url = url,
        self.api_key_auth = api_key

    """Get Requests """

    def fetch_data(self, endpoint: str, data: dict, headers: dict):
        logging.info(f'Attempting to query endpoint {endpoint} at {self.url}')
        auth = HTTPBasicAuth('apikey', self.api_key_auth)
        response = requests.get(self.url, headers=headers, auth=auth, data=json.dumps(data))
        logging.debug(f'Received the following response code from {self.url}{self.endpoint} : {response}')
        return response


class CMCApiClient(CollectorApiClient):
    def __init__(self):
        super(CMC_PROD_ENDPOINT, os.environ['CMC_API_KEY'])
        logging.debug(f'f Initiated super {super.__str__()} ')

    """Data refreshed every 60 seconds"""
    def cmc_fetch_latest_token_data(self, headers: dict, data: dict):
        return self.fetch_data(LATEST_TOKENS_CMC, headers, data)

    def cmc_fetch_token_metadata(self, headers: dict, data: dict):
        return self.fetch_data(CRYPTO_META_DATA_CMC, headers, data)

    def cmc_fetch_latest_token_quote(self, headers: dict, data: dict):
        return self.fetch_data(LATEST_QUOTES_CMC, headers, data)


""" Coin Gekco API Client"""


class CGApiClient(CollectorApiClient):
    pass
