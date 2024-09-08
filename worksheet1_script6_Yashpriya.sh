#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
    echo "usage: $0 <dir_name>"
  exit 1
fi
#get the directory name from the argument
dir_name="$1"
#check if the given name is a valid directory
if [ -d "$dir_name" ]; then
#find empty sub-folders & do output redirection
	find "$dir_name" -type d -empty > empty_subfolders.txt
echo "The empty sub-folders that were present in "$dir_name" directory has been listed into a new file called 'empty_subfolders.txt'"
else
	echo "Please enter valid directory name"
fi

