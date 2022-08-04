from statsmodels.tsa.stattools import grangercausalitytests
import pandas as pd

df = pd.read_csv('./data/grangerCausality.csv', parse_dates=['date'])

print("df-----", df)

df['month'] = df.date.dt.month
grangercausalitytests(df[['value', 'month']], maxlag=2)
