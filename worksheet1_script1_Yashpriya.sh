#!/bin/bash
#To list all the executable files present in the system.
echo "The list of all executable files are as follows:"
sudo find / -type f -perm -a+x -print
#Optional: Redirect the output of find command to a file called executable_files.txt
#sudo find / -type f -perm -a+x -print > executable_files.txt 
