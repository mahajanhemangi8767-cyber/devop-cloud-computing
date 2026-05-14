#!/bin/bash

read -rp "Enter something : " data
pattern='[0-9]+$' # pattern you can use variable ''

if [[ $data =~ $pattern ]]; then
echo "It is an integer number"

else

echo "Not an integer number"

fi

# [[.....]] advanced test command
# =~ cannot work without [[]]
# powerful to test regex



