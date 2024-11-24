#!/bin/sh

echo "Enter a number for base: "
read a
echo "Enter a number for power: "
read b

i=1
res=1

while [ $i -le $b ]; do
    res=$((res * a))
    i=$((i + 1))
done 

# result=$((base ** exponent))

echo "$a^$b = $res"
