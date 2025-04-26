import requests
import time

from config.configs import (
    ETHERSCAN_API_KEY,
    ETHERSCAN_BASE_URL,
    ETHERSCAN_RETRY_COUNT,
    ETHERSCAN_API_TIMEOUT,
    ETHERSCAN_MAX_PAGE_SIZE
)


class EtherscanClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or ETHERSCAN_API_KEY
        self.base_url = ETHERSCAN_BASE_URL
        self.page_size = ETHERSCAN_MAX_PAGE_SIZE

    def _make_request(self, params):
        """Single API call"""
        params["apikey"] = self.api_key
        retries = ETHERSCAN_RETRY_COUNT

        for attempt in range(retries):
            try:
                response = requests.get(self.base_url, params=params, timeout=ETHERSCAN_API_TIMEOUT)
                response.raise_for_status()
                data = response.json()

                if data["status"] == "1":
                    return data["result"]
                elif data["message"] == "No transactions found":
                    return []
                else:
                    raise Exception(f"Etherscan error: {data['message']}")
            except Exception as e:
                print(f"[Attempt {attempt+1}] Error: {e}")
                time.sleep(1)

        raise Exception("Failed after multiple retries")

    def _stream_paginated_request(self, base_params):
        """YIELD page by page instead of accumulating"""
        base_params["apikey"] = self.api_key
        page = 1

        while True:
            params = base_params.copy()
            params.update({
                "page": page,
                "offset": self.page_size
            })

            retries = ETHERSCAN_RETRY_COUNT
            for attempt in range(retries):
                try:
                    response = requests.get(self.base_url, params=params, timeout=ETHERSCAN_API_TIMEOUT)
                    response.raise_for_status()
                    data = response.json()

                    if data["status"] == "1":
                        page_results = data["result"]
                        if not page_results:
                            return
                        print(f"Yielding page {page} with {len(page_results)} transactions")
                        for tx in page_results:
                            yield tx
                        if len(page_results) < self.page_size:
                            return
                        else:
                            page += 1
                            break
                    elif data["message"] == "No transactions found":
                        return
                    else:
                        raise Exception(f"Etherscan error: {data['message']}")
                except Exception as e:
                    print(f"[Page {page}][Attempt {attempt+1}] Error: {e}")
                    time.sleep(1)
            else:
                raise Exception(f"Failed after multiple retries on page {page}")

    def _stream_transactions(self, address, action):
        """Unified stream fetcher"""
        base_params = {
            "module": "account",
            "action": action,
            "address": address,
            "sort": "asc"
        }

        print(f"Streaming {action} for {address}...")
        return self._stream_paginated_request(base_params)

    # ---------- Public APIs ----------

    def stream_normal_transactions(self, address):
        return self._stream_transactions(address, "txlist")

    def stream_internal_transactions(self, address):
        return self._stream_transactions(address, "txlistinternal")

    def stream_token_transfers(self, address):
        return self._stream_transactions(address, "tokentx")

    def stream_nft_transfers(self, address):
        return self._stream_transactions(address, "tokennfttx")
