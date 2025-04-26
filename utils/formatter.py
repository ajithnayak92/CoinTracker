from datetime import datetime

def from_wei(value):
    return str(int(value) / 1e18)

def from_token(value, decimals):
    try:
        return str(int(value) / (10 ** int(decimals)))
    except (ValueError, ZeroDivisionError):
        return "0"

def format_timestamp(ts):
    return datetime.utcfromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')

def calc_gas_fee(tx):
    try:
        gas_used = int(tx["gasUsed"])
        gas_price = int(tx["gasPrice"])
        return str((gas_used * gas_price) / 1e18)
    except (KeyError, ValueError):
        return ""
