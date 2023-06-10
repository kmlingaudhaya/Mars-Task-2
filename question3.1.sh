#!/bin/bash

read -p "Enter the length of the password: " length

if [[ -z $length ]]; then
  echo "Please provide a valid length for the password."
  exit 1
fi

# Generate the random password with only numbers
character_set="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password=$(echo "$character_set" | fold -w1 | shuf | tr -d '\n' | head -c "$length")

echo "Random Password: $password"

