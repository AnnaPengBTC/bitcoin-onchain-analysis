import sys
import os

# Add the project root directory to Python’s path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.db_config import get_db_connection
import pandas as pd
from config.db_config import get_db_connection
from fetch_data.fetch_transactions import fetch_latest_transactions

def save_btc_transactions():
    """Fetch and store Bitcoin transactions in PostgreSQL."""
    transactions = fetch_latest_transactions()
    df = pd.DataFrame(transactions)

    # Extract useful fields
    df = df[["txid", "fee", "vin", "vout", "status"]]
    df["inputs"] = df["vin"].apply(len)
    df["outputs"] = df["vout"].apply(len)
    df["timestamp"] = pd.to_datetime(df["status"].apply(lambda x: x["block_time"]), unit='s')

    # Store in PostgreSQL
    engine = get_db_connection()
    df.to_sql("bitcoin_transactions", engine, if_exists="replace", index=False)

    print("✅ Bitcoin transactions saved!")

save_btc_transactions()

def save_btc_prices():
    """Fetch and store BTC price data."""
    btc_prices = fetch_btc_price()
    engine = get_db_connection()
    btc_prices.to_sql("bitcoin_prices", engine, if_exists="replace", index=False)
    print("✅ BTC prices saved!")

save_btc_prices()

def save_google_trends():
    """Fetch and store Google Trends data."""
    google_trends = fetch_google_trends()
    google_trends.reset_index(inplace=True)  # Move date from index to column

    engine = get_db_connection()
    google_trends.to_sql("google_trends", engine, if_exists="replace", index=False)
    print("✅ Google Trends data saved!")

save_google_trends()

def save_macro_data():
    """Fetch and store macroeconomic data."""
    cpi_data = fetch_cpi_data()
    interest_data = fetch_interest_rate()

    df_cpi = pd.DataFrame(cpi_data)
    df_interest = pd.DataFrame(interest_data)

    df_cpi.rename(columns={"value": "cpi"}, inplace=True)
    df_interest.rename(columns={"value": "interest_rate"}, inplace=True)

    df = pd.merge(df_cpi, df_interest, on="date", how="outer")

    engine = get_db_connection()
    df.to_sql("macro_data", engine, if_exists="replace", index=False)
    print("✅ Macro data saved!")

save_macro_data()