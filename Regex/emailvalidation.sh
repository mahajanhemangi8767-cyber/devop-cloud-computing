#!/bin/bash

read -rp "Enter Email ID: " email

pattern='^[A-Za-z0-9._-]+@[A-Za-z0-9._-]+\.[A-Za-z]{2,4}$'

if [[ $email =~ $pattern ]]; then
  echo "Valid Email ID"
else
  echo "Not Valid Email ID"
fi


# ^[A-za-za-9._-]+@[A-za-za-9._-]+\.[A-Za-z]{2,4}$
# Explanation
# ^ start with
# ^[A-za-za-9._-]+ = capital,small,digits, . _ and - allowed 0 or more time
# @ is fixed you have to add it
# [A-Za-z0-9._-]+= again enter something after @
#\. is fixed you have to add it
# [A-Za-z]{2,4} = any capital or small but min 2 max 4 in length like com,org,edu etc
# $ indication end of pattern









