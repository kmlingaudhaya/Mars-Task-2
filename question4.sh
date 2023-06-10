#!/bin/bash
read -p "Enter the matrix file path: " matrix_file

# Read the matrix from the file into an array
readarray -t matrix < "$matrix_file"

# Transpose the matrix
transposed_matrix=()
for ((i = 0; i < ${#matrix[@]}; i++)); do
    IFS=' ' read -ra row <<< "${matrix[$i]}"
    for ((j = 0; j < ${#row[@]}; j++)); do
        transposed_matrix[$j]+="${row[$j]} "
    done
done

# Print the transposed matrix in standard 2D matrix format
for ((i = 0; i < ${#transposed_matrix[@]}; i++)); do
    echo "${transposed_matrix[$i]}"
done
