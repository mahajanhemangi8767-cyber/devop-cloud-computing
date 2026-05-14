#!/bin/bash

echo "Health Check Report - $(date)"
echo "--------------------------------"

echo ""
echo "Memory Usage:"
free -h | awk '/Mem:/ {print "Used: "$3" / Total: "$2}'

echo ""
echo "Disk Usage:"
df -h --total | awk '/total/ {print "Used: "$3" / Total: "$2" ("$5" used)"}'

echo ""
echo "CPU Load:"
uptime
