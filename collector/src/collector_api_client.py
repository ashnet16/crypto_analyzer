import json

from collector.src.constants import approved_urls
import logging
import requests
from collector.src.constants import CMC_PROD_ENDPOINT, LATEST_TOKENS_CMC, CRYPTO_META_DATA_CMC, LATEST_QUOTES_CMC, GAINERS_AND_LOSERS_CMC, HISTORICAL
import os


class CollectorApiClient:
    def __init__(self, url: str, api_key: str):
        if approved_urls[url]:
            self.url = url
        self.api_key_auth = api_key

    """Get Requests """

    def fetch_data(self, endpoint: str, **query_inputs):
        logging.info(f'Attempting to query endpoint {endpoint} at {self.url}')
        headers = query_inputs.get('headers')
        headers['X-CMC_PRO_API_KEY'] = self.api_key_auth
        response = requests.get(self.url+endpoint, headers=headers, params=query_inputs.get('data'))
        logging.debug(f'Received the following response code from {self.url}{endpoint} : {response}')
        return response.content


class CMCApiClient(CollectorApiClient):
    def __init__(self):
        super(CMCApiClient, self).__init__(CMC_PROD_ENDPOINT, os.environ['CMC_API_KEY'])
        logging.debug(f'f Initiated super ')

    """Data refreshed every 60 seconds"""
    def cmc_fetch_latest_token_data(self, **params):
        return self.fetch_data(LATEST_TOKENS_CMC, headers=params.get('headers'), data=params.get('data'))

    def cmc_fetch_token_metadata(self, **params):
        return self.fetch_data(CRYPTO_META_DATA_CMC, headers=params.get('headers'), data=params.get('data'))

    def cmc_fetch_latest_token_quote(self, **params):
        return self.fetch_data(LATEST_QUOTES_CMC, headers=params.get('headers'), data=params.get('data'))

    def cmc_fetch_top_gainers_and_losers(self, **params):
        return self.fetch_data(GAINERS_AND_LOSERS_CMC, headers=params.get('headers'), data=params.get('data') )

    def cmc_fetch_historical_snapshot(self, **params):
        return self.fetch_data(HISTORICAL, headers=params.get('headers'), data=params.get('data'))



""" Coin Gekco API Client"""


class CGApiClient(CollectorApiClient):
    pass
