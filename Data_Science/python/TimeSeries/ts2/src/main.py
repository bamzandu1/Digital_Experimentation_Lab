import pandas as pd
import numpy as np

df = pd.read_csv(
    "../input/datasets/co2.csv",
    index_col='Date',
    parse_dates=['Date'],
)

df['Time'] = np.arange(len(df.index))

print(df.head(20))