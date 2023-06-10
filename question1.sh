#!/bin/bash

# Prompt user for current working directory
read -p "Enter the current working directory: " dir

# Check if the provided directory exists
if [ ! -d "$dir" ]; then
  echo "Directory '$dir' does not exist."
  exit 1
fi

# Create the "Modified" directory
mkdir -p "$dir/Modified"

# Recursively search for ".txt" files and copy them with extension ".bak"
find "$dir" -type f -name "*.txt" -exec sh -c 'cp "$1" "$0/Modified/$(basename "$1" .txt).bak"' "$dir" {} \;

echo "Files with extension '.txt' copied to 'Modified' directory with extension '.bak'."

