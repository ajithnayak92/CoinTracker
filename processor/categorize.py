from fetcher.parser import (
    parse_normal_tx,
    parse_internal_tx,
    parse_token_tx,
    parse_nft_tx
)

class TransactionProcessor:
    def __init__(self, etherscan_client):
        self.client = etherscan_client

    def process_all_transactions(self, address):
        records = []

        try:
            normal_txs = self.client.stream_normal_transactions(address)
            records.extend([parse_normal_tx(tx) for tx in normal_txs])
        except Exception as e:
            print(f"Error fetching normal txs: {e}")

        try:
            internal_txs = self.client.stream_internal_transactions(address)
            records.extend([parse_internal_tx(tx) for tx in internal_txs])
        except Exception as e:
            print(f"Error fetching internal txs: {e}")

        try:
            token_txs = self.client.stream_token_transfers(address)
            records.extend([parse_token_tx(tx) for tx in token_txs])
        except Exception as e:
            print(f"Error fetching token txs: {e}")

        try:
            nft_txs = self.client.stream_nft_transfers(address)
            records.extend([parse_nft_tx(tx) for tx in nft_txs])
        except Exception as e:
            print(f"Error fetching NFT txs: {e}")

        return records
