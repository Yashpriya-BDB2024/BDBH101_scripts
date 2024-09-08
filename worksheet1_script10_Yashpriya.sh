#!/bin/bash
#check if atleast one argument is provided
if [ $# -eq 0 ]; then
	echo "usage: $0 <file_DNA_sequence>"
exit 1
fi
#get the file name containing DNA sequence from the argument (with extension)
file_DNA_sequence="$1"
#check if it is a valid file name
if [ -f "$file_DNA_sequence" ]; then
	echo "Its a valid file"
else
	echo "File doesn't exists"
fi
#check whether the input contains A,T,G,C or not
if awk 'NR>1' "$file_DNA_sequence" | grep -q '[^ACGT]'; then
echo "Error: Its an invalid sequence"
else
#count the number of A, C, T, G nucleotides
Num_of_A=$(awk 'NR>1' "$file_DNA_sequence" | grep -o "A" | wc -l)
echo "No. of 'A' nucleotides in the given sequence is "$Num_of_A""
Num_of_C=$(awk 'NR>1' "$file_DNA_sequence" | grep -o "C" | wc -l)
echo "No. of 'C' nucleotides in the given sequence is "$Num_of_C""
Num_of_G=$(awk 'NR>1' "$file_DNA_sequence" | grep -o "G" | wc -l)
echo "No. of 'G' nucleotides in the given sequence is "$Num_of_G""
Num_of_T=$(awk 'NR>1' "$file_DNA_sequence" | grep -o "T" | wc -l)
echo "No. of 'T' nucleotides in the given sequence is "$Num_of_T""
fi
