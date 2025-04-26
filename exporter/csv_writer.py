import csv
import os

CSV_HEADERS = [
    "Transaction Hash",
    "Date & Time",
    "From Address",
    "To Address",
    "Transaction Type",
    "Asset Contract Address",
    "Asset Symbol / Name",
    "Token ID",
    "Value / Amount",
    "Gas Fee (ETH)"
]

def export_to_csv(records, output_file):
    os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)

    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS)
        writer.writeheader()

        for record in records:
            writer.writerow({
                "Transaction Hash": record["tx_hash"],
                "Date & Time": record["timestamp"],
                "From Address": record["from"],
                "To Address": record["to"],
                "Transaction Type": record["type"],
                "Asset Contract Address": record["contract_address"],
                "Asset Symbol / Name": record["asset"],
                "Token ID": record["token_id"],
                "Value / Amount": record["amount"],
                "Gas Fee (ETH)": record["gas_fee"],
            })

    print(f"Exported {len(records)} records to {output_file}")
