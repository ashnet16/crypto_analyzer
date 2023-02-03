import json

from collector.src.collector_api_client import CMCApiClient
from collector.src.constants import CHOICE_CURRENCY, JSON_HEADER, CONVERT, SLUG, CRYPTO_WATCH_LIST


class CMCService:
    def __init__(self):
        self.client = CMCApiClient()

    def cmc_fetch_latest_tokens(self):
        return self.client.cmc_fetch_latest_token_data(headers=JSON_HEADER)

    def cmc_fetch_latest_quote(self):
        data = {CONVERT: CHOICE_CURRENCY, SLUG: CRYPTO_WATCH_LIST}
        return self.client.cmc_fetch_latest_token_quote(headers=JSON_HEADER, data=data)

    def cmc_fetch_token_metadata(self):
        data = {SLUG: CRYPTO_WATCH_LIST}
        return self.client.cmc_fetch_token_metadata(headers=JSON_HEADER, data=data)


class CGService:
    pass
