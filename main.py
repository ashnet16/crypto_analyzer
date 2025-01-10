from collector.src.collect_service import CMCService
from datetime import datetime, timedelta
import pandas as pd
import json



def fetch_and_save_historical_data(start_date):
    date = datetime.strptime(start_date, '%Y-%m-%d').date()
    cmc_service = CMCService()
    current_date = datetime.now().date()
    result = []
    while date <= current_date:
        recent_dump = json.loads(cmc_service.cmc_fetch_historical_data(date))
        df = pd.json_normalize(recent_dump['data'])
        df['date'] = date.strftime('%Y-%m-%d')
        date += timedelta(days=1)
        result.append(df)
        final_df = pd.concat(result, ignore_index=True)
        final_df.to_csv(f'cryptocurrency_data_{start_date}_to_{current_date}.csv', index=False)


if __name__ == '__main__':
    START_DATE = '2024-12-11'
    fetch_and_save_historical_data(START_DATE)



