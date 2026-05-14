#!/bin/bash

read -rp "Enter IP Address: " IP_address

pattern='^[0-9.]+$'
if [[ $IP_address =~ $pattern ]]; then
  echo "Valid IP address"
else
  echo "Not Valid IP address"
fi






# '^[0-9.]+$' -> IP address pattern 
# '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$' ->IP address pattern'











