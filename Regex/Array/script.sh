#!/bin/bash
while getopts ":f:o:" opt; 
do
  case $opt in

    f)
 echo "File option passed with value: $OPTARG" ;;

    o)
 echo "Output option passed with value: $OPTARG" ;;
  
  \?)
echo "invalid option: -$OPTARG" ;;

   esac
done 
