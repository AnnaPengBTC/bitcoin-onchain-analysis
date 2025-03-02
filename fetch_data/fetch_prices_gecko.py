import os
import requests
import pandas as pd

os.makedirs("data", exist_ok=True)

def fetch_btc_prices():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30" #This URL is from the CoinGecko API and requests Bitcoin price data for the last 30 days in USD.
    response = requests.get(url).json()
    btc_prices = pd.DataFrame(response['prices'], columns=['timestamp', 'price'])#timestamp in milliseconds need conversion and price 
    btc_prices['date'] = pd.to_datetime(btc_prices['timestamp'], unit='ms') #convert to date form
    return btc_prices

if __name__ == "__main__":
    btc_prices = fetch_btc_prices()
    btc_prices.to_csv("data/btc_prices.csv", index=False)
    print("BTC Price Data Fetched & Saved ✅")
