#!/bin/bash
#Check if the threshold argument is provided.
if [ $# -eq 0 ]; then
	echo "usage: $0 <threshold>"
	exit 1
fi
#get the threshold from argument
threshold="$1"
#check the disk space used by the home directory
disk_usage=$(df "$HOME" | awk 'NR==2 {print $5}' | sed 's/%//')  
#check whether it exceeds the given threshold value
if [ "$disk_usage" -ge "$threshold" ]; then 
	echo "Warning: Disk space usage is ${disk_usage}%, that is more than threshold value" 
	else 
		disk_space_left=$((100 - "$disk_usage")) 
	echo "${disk_space_left}% of disk space is still present"
fi
