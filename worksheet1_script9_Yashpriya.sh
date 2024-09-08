#!/bin/bash
#get the current hour 
current_hour=$(date +"%H")
#print the appropriate greeting based on the time
if [ $current_hour -ge 5 ] && [ $current_hour -lt 12 ]; then
	echo "Good morning!"
elif [ $current_hour -ge 12 ] && [ $current_hour -lt 18 ]; then
	echo "Good afternoon!"
elif [ $current_hour -ge 18 ] && [ $current_hour -lt 5 ]; then
	echo "Good night!"
fi
