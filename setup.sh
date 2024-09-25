#!/bin/bash

# Navigate to the directory containing requirements.txt
cd "$(dirname "$0")"

# Check if requirements.txt exists
if [ -f requirements.txt ]; then
    echo "Installing Python packages from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
    exit 1
fi