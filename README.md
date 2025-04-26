# Ethereum Wallet Transaction Exporter
Maintainer: Ajith Nayak

_NOTE: This is an assignment for CoinTracker, details [here](https://www.notion.so/cointracker/Ajith-Nayak-1e0a6ee5e05f806fb767f2106286a4c1)_

Retrieve, categorize, and export all Ethereum wallet transactions to a CSV file — including normal transfers, internal transfers, ERC-20 tokens, and NFTs — ready for portfolio tracking or personal records.

We're using the apis of `EtherScan` organisation, using the fetch transaction [api](https://docs.etherscan.io/api-endpoints/accounts#get-a-list-of-normal-transactions-by-address)

The script requires `python3` to execute.

---

## Project Overview

This script:

- Accepts Ethereum wallet addresses as input
- Fetches complete transaction history using the Etherscan API
- Handles large wallets through smart pagination fetching
- Categorizes transactions:
  - `External (Normal) Transfers`
  - `Internal Transfers`
  - `ERC-20 Token Transfers`
  - `ERC-721 (NFT) Transfers`
- Exports structured data into CSV files

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ajithnayak92/CoinTracker.git
cd CoinTracker
```

### 2. Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration
Update configs.py with the api key for your account:

```python
...
ETHERSCAN_API_KEY = "your_etherscan_api_key"
...
```

##  Usage
For Single address fetch, use the command:
```bash
python main.py --address 0xa39b189482f984388a34460636fea9eb181ad1a6
```

### Assumptions
- This app is a script that allows a user to download the transaction history for a given wallet.
- There is no storage, we will directly use third party services of etherscan
- There is no caching/storage layer in the script
- We rely on the availability of etherscan for our services, no resiliency issues addressed

### Architectural decisions
- This app logic resides within a script, but the structure of the project is modular
- We have configs separated out into a file of its own
- We make use of a csv writer library to export the output of the file
- We have a processor package that configures the data that we fetch for a given wallet
- Fetcher package is a client for the apis provided by etherscan