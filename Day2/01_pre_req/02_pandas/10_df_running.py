import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2026-01-01",periods=100,freq="D")
prices = 150 + np.random.randn(100).cumsum()

df_stocks = pd.DataFrame({"Date":dates,"Close":prices}).set_index("Date")
print(df_stocks)
print("=" * 60)

# Rolling window
df_stocks["7D_MA"]=df_stocks["Close"].rolling(window=7).mean()
df_stocks["7D_STD"]=df_stocks["Close"].rolling(window=7).std()
print("=" * 60)
print(df_stocks.head(10))