# Ethereum Wallet Transaction Exporter
Maintainer: Ajith Nayak

_NOTE: This is an assignment for CoinTracker, details [here](https://www.notion.so/cointracker/Ajith-Nayak-1e0a6ee5e05f806fb767f2106286a4c1)_

Retrieve, categorize, and export all Ethereum wallet transactions to a CSV file — including normal transfers, internal transfers, ERC-20 tokens, and NFTs — ready for portfolio tracking or personal records.

The script requires `python3` to execute.

---

## Project Overview

This script:

- Accepts Ethereum wallet addresses as input
- Fetches complete transaction history using the Etherscan API
- Handles large wallets through smart pagination and multi-threaded fetching
- Categorizes transactions:
  - External (Normal) Transfers
  - Internal Transfers
  - ERC-20 Token Transfers
  - ERC-721 (NFT) Transfers
- Exports structured data into CSV files

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/eth-wallet-exporter.git
cd eth-wallet-exporter
```

### 2. Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration
Update config/configs.py:

```python
...
ETHERSCAN_API_KEY = "your_etherscan_api_key"
...
```

##  Usage
Single address
```bash
python main.py --address 0xa39b189482f984388a34460636fea9eb181ad1a6
```