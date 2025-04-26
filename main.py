import argparse
from fetcher.etherscan_client import EtherscanClient
from processor.categorize import TransactionProcessor
from exporter.csv_writer import export_to_csv

def main():
    parser = argparse.ArgumentParser(description="Ethereum Wallet Transaction Exporter")
    parser.add_argument("address", help="Ethereum wallet address")
    parser.add_argument("--output", help="Path to output CSV file", default="eth_transactions.csv")
    parser.add_argument("--api-key", help="Etherscan API Key", required=False)

    args = parser.parse_args()

    print(f"Fetching transactions for: {args.address}")
    client = EtherscanClient(api_key=args.api_key)
    processor = TransactionProcessor(client)

    try:
        all_records = processor.process_all_transactions(args.address)
        print(f"Total transactions fetched: {len(all_records)}")
        export_to_csv(all_records, args.output)
    except Exception as e:
        print(f"Error processing transactions: {e}")

if __name__ == "__main__":
    main()
