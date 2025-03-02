import requests

FRED_API_KEY = "ea5443086c46a700fe9384eb9246d02f" #got my API key at FREED

def fetch_macro_data():
    """Fetches macroeconomic data from FRED (CPI, Interest Rates)."""
    fred_url = f"https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key={FRED_API_KEY}&file_type=json"
    cpi_data = requests.get(fred_url).json()
    
    return cpi_data

if __name__ == "__main__":
    macro_data = fetch_macro_data()
    print(macro_data)


def fetch_interest_rate():
    """Fetches the Federal Funds Rate from FRED API."""
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["observations"]  # List of interest rate data points
    else:
        print(f"Error: {response.status_code}")
        return None

# Test fetching interest rate data
interest_data = fetch_interest_rate()
print(interest_data[:5])  # Print first 5 interest rate records
