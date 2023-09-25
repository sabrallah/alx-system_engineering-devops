#!/usr/bin/env bash

if [ $# -lt 3 ]; then
    echo "Usage: $0 PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
    exit 1
fi

file=$1
ip=$2 
user=$3
key=$4

scp -o StrictHostKeyChecking=no "$file" "$user@$ip:~" < "/dev/null" 2>&1
