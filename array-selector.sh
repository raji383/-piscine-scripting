#!/bin/bash
Array=("red" "blue" "green" "white" "black")

if [[ $# -ne 1 ]]; then
    echo "Error"
    exit 0
fi

if ! [[ $1 =~ ^-?[0-9]+$ ]]; then
    echo "Error"
    exit 0
fi

if [[ $1 -gt ${#Array[@]} ]]; then
    echo "Error"
    exit 0
fi
I=$1-1
echo ${Array[$I]}
