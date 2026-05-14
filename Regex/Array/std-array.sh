#!/bin/bash

names=("alex" "bob" "catty" "john")

echo "First element: ${names[0]}" # 0 is the first index
echo "First element: ${names[3]}" # divide 


# Access Length 

echo "Total No of names: ${#names[@]}"   # indicates count , @ indicates all
echo "All Names: ${names[@]}" # print all names using @

# change bob with your name

names[1]="Sonam Soni"
echo "Updated Element: ${names[1]}"

# print all using loop


for name in "${names[@]}"; do
echo $name
done









