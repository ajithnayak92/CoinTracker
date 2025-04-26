from datetime import datetime

def parse_normal_tx(tx):
    return {
        "tx_hash": tx["hash"],
        "timestamp": format_timestamp(tx["timeStamp"]),
        "from": tx["from"],
        "to": tx["to"],
        "type": "ETH Transfer" if tx["input"] == "0x" else "Contract Interaction",
        "contract_address": "",
        "asset": "ETH",
        "token_id": "",
        "amount": from_wei(tx["value"]),
        "gas_fee": calc_gas_fee(tx)
    }

def parse_internal_tx(tx):
    return {
        "tx_hash": tx["hash"],
        "timestamp": format_timestamp(tx["timeStamp"]),
        "from": tx["from"],
        "to": tx["to"],
        "type": "Internal Transfer",
        "contract_address": "",
        "asset": "ETH",
        "token_id": "",
        "amount": from_wei(tx["value"]),
        "gas_fee": ""  # Not available from internal txs
    }

def parse_token_tx(tx):
    return {
        "tx_hash": tx["hash"],
        "timestamp": format_timestamp(tx["timeStamp"]),
        "from": tx["from"],
        "to": tx["to"],
        "type": "ERC-20 Transfer",
        "contract_address": tx["contractAddress"],
        "asset": tx["tokenSymbol"],
        "token_id": "",
        "amount": from_token(tx["value"], tx["tokenDecimal"]),
        "gas_fee": ""  # Can optionally be fetched from normal txs
    }

def parse_nft_tx(tx):
    return {
        "tx_hash": tx["hash"],
        "timestamp": format_timestamp(tx["timeStamp"]),
        "from": tx["from"],
        "to": tx["to"],
        "type": "ERC-721 Transfer",
        "contract_address": tx["contractAddress"],
        "asset": tx.get("tokenName", "NFT"),
        "token_id": tx["tokenID"],
        "amount": "1",  # NFTs are usually single units
        "gas_fee": ""  # Not available directly
    }

# --- Helper functions ---

def from_wei(value):
    return str(int(value) / 1e18)

def from_token(value, decimals):
    return str(int(value) / (10 ** int(decimals)))

def format_timestamp(ts):
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')

def calc_gas_fee(tx):
    gas_used = int(tx["gasUsed"])
    gas_price = int(tx["gasPrice"])
    return str((gas_used * gas_price) / 1e18)
