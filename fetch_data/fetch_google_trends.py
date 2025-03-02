from pytrends.request import TrendReq

def fetch_google_trends():
    """Fetches Bitcoin search trends from Google Trends."""
    pytrends = TrendReq()
    pytrends.build_payload(["Bitcoin"], timeframe="now 7-d")
    trends = pytrends.interest_over_time()
    
    return trends

if __name__ == "__main__":
    trends = fetch_google_trends()
    print(trends)
