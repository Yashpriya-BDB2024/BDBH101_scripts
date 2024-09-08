#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
	echo "usage: $0 <file_name>"
exit 1
fi
#get the file name from the argument
file_name="$1"
#check if the given name is a valid file
if [ -f "$file_name" ]; then
#display the original contents of the given file
echo "Contents of the original file are: -"
cat "$file_name"
#remove identical or duplicate lines from the given file
sort "$file_name" | uniq > modified_file.txt
echo "Duplicate lines removed successfully"
#display the contents of the modified file
echo "Contents of the modified file are: -"
cat modified_file.txt
else
	echo "Its not a file. Please enter valid file name"
fi
