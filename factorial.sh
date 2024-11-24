#!/bin/sh

echo "Enter a number: "
read n

a=1
product=1

while [ $a -le $n ]; do
    product=$((product * a))
    a=$((a + 1))
done

echo "The Factorial of Number $n is $product"
