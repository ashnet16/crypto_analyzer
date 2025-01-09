from collector.src.collect_service import CMCService
import pandas as pd
import json


if __name__ == '__main__':
    recent_dump = json.loads(CMCService().cmc_fetch_historical_data('2024-12-09'))
    df = pd.json_normalize(recent_dump['data'])
    df.to_csv('cryptocurrency_data.csv', index=False)



