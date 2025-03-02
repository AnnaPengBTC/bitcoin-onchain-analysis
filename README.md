# bitcoin-onchain-analysis
Go to GitHub Click on the "+" in the top-right corner → New Repository Repository name: bitcoin-onchain-analysis Description: 

File structure and purposes:
bitcoin_analysis/
│── fetch_data/
│   ├── fetch_transactions.py    # Fetches BTC transaction data
│   ├── fetch_prices.py          # Fetches BTC price data from CoinGecko
│   ├── fetch_google_trends.py   # Fetches BTC search trends
│   ├── fetch_macro_data.py      # Fetches macroeconomic indicators
│── database/
│   ├── db_config.py             # Database connection setup
│   ├── save_data.py             # Stores fetched data in PostgreSQL
│── analysis/
│   ├── analyze_whale_activity.py # Analyzes whale transactions
│   ├── analyze_sentiment.py      # Correlates Google Trends with BTC price
│   ├── visualize_data.py         # Plots BTC price, whale activity, and sentiment
│── dashboard/
│   ├── app.py                    # Flask/Dash web app
│── config.py                     # Configuration (API keys, DB settings)
│── requirements.txt               # Python dependencies
│── run_fetchers.py                # Runs all data fetch scripts
│── README.md                      # Documentation
