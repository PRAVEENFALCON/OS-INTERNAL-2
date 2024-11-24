#!/bin/sh

echo "Enter a number: "
read n

temp=$n
reverse=0

while [ $n -ne 0 ]; do
    remainder=$((n % 10))
    reverse=$((reverse * 10 + remainder))
    n=$((n / 10))
done

if [ $reverse -eq $temp ]; then
    echo "The given number is a Palindrome"
else
    echo "The given number is not a Palindrome"
fi
