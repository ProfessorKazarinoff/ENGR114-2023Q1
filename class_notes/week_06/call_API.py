# call_API.py

import pandas as pd

def call_API(a):
    field_d = {'humidity':'3','temperature':'4','rainfall':'5','pressure':'6'}
    fn = field_d[a[0]]
    url = f"https://api.thingspeak.com/channels/12397/fields/{fn}.csv?results={a[1]}"
    df = pd.read_csv(url)
    return df
