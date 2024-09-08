#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
	echo "usage: $0 <threshold>"
exit 1
fi
#get the threshold value from the argument
threshold="$1"
#loop through every no. 1 to 100
for number in {1..100}; do
#print each no. to standard output
   echo "$number"
#check if the number is greater than the given threshold value
if [ "$number" -gt "$threshold" ]; then
	echo "The number "$number" is greater than the given threshold value"
fi
done

