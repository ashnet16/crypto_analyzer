from collector_api_client import CMCApiClient
from constants import CHOICE_CURRENCY, JSON_HEADER, CONVERT, SLUG, CRYPTO_WATCH_LIST


class CMCService:
    def __init__(self):
        self.client = CMCApiClient()

    def cmc_fetch_latest_tokens(self):
        data = {CONVERT: CHOICE_CURRENCY}
        return self.client.cmc_fetch_latest_token_data(JSON_HEADER, data)

    def cmc_fetch_latest_quote(self):
        data = {CONVERT: CHOICE_CURRENCY, SLUG: CRYPTO_WATCH_LIST}
        return self.client.cmc_fetch_latest_token_data(JSON_HEADER, data)

    def cmc_fetch_token_metadata(self):
        data = {CONVERT: CHOICE_CURRENCY, SLUG: CRYPTO_WATCH_LIST}
        return self.client.cmc_fetch_token_metadata(JSON_HEADER, data)


class CGService:
    pass
