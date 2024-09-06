#!/bin/bash
#check the home directory disk space usage
home_usage=$(df "$HOME" | awk 'NR==2 {print $3}')
echo "The home directory usage is $home_usage"
#check the root directory disk space usage
root_usage=$(df "/" | awk 'NR==2 {print $3}')
echo "The root directory usage is $root_usage"
#calculate the percentage of home directory usage relative to the root directory usage
if [ $root_usage != 0 ]; then
	relative_percentage=$(("$home_usage" * 100 / "$root_usage"))
	echo "The percentage of home directory usage relative to the root directory usage is $relative_percentage%"
else
	echo "Error: Root directory is zero"
fi
