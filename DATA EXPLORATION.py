import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
auto_prices = pd.read_csv('Automobile price data _Raw_.csv')
def clean_auto_data(auto_prices):
    import pandas as pd
    import numpy as np
    cols = auto_prices.columns
    auto_prices.columns = [str.replace('-','_') for str in cols]
    cols = ['price','bore','sroke','horsepower','peak_rpm']
    for column in cols:
        auto_prices.loc[auto_prices[column] == '?',column] = np.nan
    auto_prices.dropna(axis=0 , inplace = True)
    for column in cols:
        auto_prices[column] = pd.to_numeric(auto_prices[column])
        return auto_prices
auto_prices = clean_auto_data(auto_prices)
print(auto_prices.columns)

