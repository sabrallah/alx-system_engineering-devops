#!/usr/bin/env bash
# This script transfers a file from the client to a server using scp.

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
  echo "Usage: $0 PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
  exit 1
fi

# Assign arguments to variables
path_to_file="$1"
ip="$2"
username="$3"
ssh_key="$4"

# Transfer the file using scp with strict host key checking disabled
scp -o StrictHostKeyChecking=no -i "$ssh_key" "$path_to_file" "$username@$ip":~/ 

# Check the exit status of scp
if [ $? -eq 0 ]; then
  echo "File transferred successfully"
else
  echo "File transfer failed"
fi
