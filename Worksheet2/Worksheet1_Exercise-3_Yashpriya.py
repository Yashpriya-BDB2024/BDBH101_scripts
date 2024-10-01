#To count the number of 1s present in a given binary representation
def count_num_of_ones(binary):
#Initialize the count to 0
    count=0
#Loop through each bit in the binary string.
    for bit in binary:
#Check if the current bit is 1
        if bit == '1':
#Then, increment the count by 1
            count += 1
        else:
            return 0
#Return the total count of '1s'.
    return count
def main():
    binary=input('Enter the binary representation of any decimal number: ')
    result=count_num_of_ones(binary)
    print('The number of ones present in the given binary representation is', result)
if __name__ == "__main__":
    main()