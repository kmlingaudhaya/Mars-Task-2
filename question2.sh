#!/bin/bash

directory="Modified"

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "Directory '$directory' does not exist."
  exit 1
fi

# Get the current date and time
current_date=$(date +"%Y-%m-%d %H:%M:%S")

# Iterate over each file in the directory
for file in "$directory"/*; do
  if [ -f "$file" ]; then  # Check if it is a regular file
    # Display the file name along with the current date and time
    echo "$file - $current_date"
  fi
done

