
from pycoingecko import CoinGeckoAPI

from pycoingecko import CoinGeckoAPI
from datetime import timezone
from datetime import datetime
import numpy as np
import altair as alt
import pandas as pd

def datetime_to_unix(year, month, day):
    '''datetime_to_unix(2021, 6, 1) => 1622505600.0'''
    dt = datetime(year, month, day)
    timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
    return timestamp
def unix_to_datetime(unix_time):
    '''unix_to_datetime(1622505700)=> ''2021-06-01 12:01am'''
    ts = int(unix_time/1000 if len(str(unix_time)) > 10 else unix_time) # /1000 handles milliseconds
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %l:%M%p').lower()

# Initialize the client
cg = CoinGeckoAPI()
# Retrieve Bitcoin data in USD
result = cg.get_coin_market_chart_range_by_id(
    id='bitcoin',
    vs_currency='usd',
    from_timestamp=datetime_to_unix(2022, 3, 1),
    to_timestamp=datetime_to_unix(2022, 3, 8)
)

result.keys()

time = [ unix_to_datetime(i[0]) for i in result['prices'] ]

p_array = np.array(result['prices'])
price = p_array[:,1]

v_array = np.array(result['total_volumes'])
volume = v_array[:,1]

df = pd.DataFrame({'time':time, 'price':price, 'volume':volume})
df.head()

# Create y-axis
base = alt.Chart(df).encode(x='time:O')
# Create bars 
bar = base.mark_bar().encode(
    alt.Y(
        'volume:Q',
        scale=alt.Scale(domain=(20000000000, 70000000000)),
    )
)
# Create line
line =  base.mark_line(color='orange').encode(
    alt.Y(
        'price:Q', 
        axis=alt.Axis(titleColor='#5276A7'),
        scale=alt.Scale(domain=(30000, 70000))
    )
)
# Build the chart
chart = alt.layer(bar, line).resolve_scale(y='independent').properties(width=600, title='Bitcoin Price & Volume')
# Configure title
chart.configure_title(
    fontSize=20,
    font='Helvetica',
    color='black',
    offset=10
)