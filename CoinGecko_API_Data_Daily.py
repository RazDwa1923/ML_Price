#%% md
# # CoinGecko API Script for Cryptocurrency Data
# 
# This script will pull data from the CoinGecko API and get the current top 250 coins by market cap. 
# 
# The data will be stored in a pandas dataframe and saved to a csv file.
# 
# I will update the data every day to keep the data fresh and append the new data to the csv file over time.
# 
# I will use all features that are available and have a seperate column for each feature.
#%%
# Import libraries
import os
import requests
import pandas as pd
from datetime import date
#%%
# Get data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=24&precision=4"

API_KEY = os.getenv("COINGECKO_API_KEY")

headers = {"x-cg-demo-api-key": API_KEY}

response = requests.get(url, headers=headers)

data = response.json()
#%%
# Create a pandas dataframe

df = pd.DataFrame(data)
today = date.today()


df['date'] = today


#%%
# Save the data to a csv file

path = '/Users/karolk/Python_Work/Data_Sets/Global_Data/CoinGecko_API_Data.csv'


df.to_csv(path, mode='a', header=True, index=False)
