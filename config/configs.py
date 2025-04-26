import os

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "P5V92C98AQV4YS341QDFJFKQRBRCKRIHQ9")  # fallback api key
ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"
# Default values
ETHERSCAN_RETRY_COUNT = 3
ETHERSCAN_API_TIMEOUT = 10
ETHERSCAN_MAX_PAGE_SIZE = 10000 # 10K transactions supported per call by ETHERSCAN