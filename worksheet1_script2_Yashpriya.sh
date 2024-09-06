#!/bin/bash
#Read the users.csv file
read -p "Enter the file name:" file
#print userid, username and department in consecutive lines
awk -F'[,:]' '{printf "%s\n", $1; printf "%s\n", $2; printf "%s\n", $3}' < $file 
echo "Exit code: $?"
