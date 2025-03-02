import requests

def fetch_latest_transactions():
    """Fetches Bitcoin transactions from the latest block using Blockstream API."""
    latest_block_url = "https://blockstream.info/api/blocks/tip/height"
    latest_block_height = requests.get(latest_block_url).text

    block_url = f"https://blockstream.info/api/block-height/{latest_block_height}"
    block_hash = requests.get(block_url).text

    transactions_url = f"https://blockstream.info/api/block/{block_hash}/txs"
    transactions = requests.get(transactions_url).json()

    return transactions

if __name__ == "__main__":
    data = fetch_latest_transactions()
    print(data[:5])  # Print first 5 transactions
