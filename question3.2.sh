#!/bin/bash

# Prompt user for password length
read -p "Enter the desired password length: " length

# Generate a random password
password=$(openssl rand -hex $((length)))

echo "Random Password: $password"


