from pycoingecko import CoinGeckoAPI



cg = CoinGeckoAPI()
# Retrieve Bitcoin data in USD
result = cg.get_coin_market_chart_range_by_id(
    id='bitcoin',
    vs_currency='usd',
    from_timestamp=datetime_to_unix(2022, 3, 1),
    to_timestamp=datetime_to_unix(2022, 3, 8)
)
