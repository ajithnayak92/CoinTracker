#!/bin/bash

API_KEY="your-etherscan-api-key"
OUTPUT_DIR="outputs"
mkdir -p $OUTPUT_DIR

ADDRESSES=(
    "0xa39b189482f984388a34460636fea9eb181ad1a6"
    "0xd620AADaBaA20d2af700853C4504028cba7C3333"
    "0xfb50526f49894b78541b776f5aaefe43e3bd8590"
)

for ADDRESS in "${ADDRESSES[@]}"
do
    OUTPUT_FILE="$OUTPUT_DIR/${ADDRESS}.csv"
    echo "🚀 Processing $ADDRESS"
    python3 main.py "$ADDRESS" --output "$OUTPUT_FILE" # --api-key "$API_KEY"
done
