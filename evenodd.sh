#!/bin/bash

read -p "Enter a number: " number

if ((number % 2 == 0)); then
    echo "$number is Even"
else
    echo "$number is Odd"
fi
