#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Error"
    exit 0
fi

if ! [[ $1 =~ ^-?[0-9]+$ ]]; then
    echo "Error"
    exit 0
fi

if [[ $1 > 6 ]]; then
    echo "Error"
    exit 0
fi
Array=("red" "blue" "green" "white" "black")
I=$1-1
echo ${Array[$I]}
