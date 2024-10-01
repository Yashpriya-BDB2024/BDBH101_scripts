#To convert decimal number 'D' into binary
def decimal_to_binary(D):
#Check if the input is a negative number.
    if D <= 0:
        return None
    else:
#Initialize an empty string
        binary = ""
#Loop until the decimal becomes 0
        while D > 0:
            remainder = D % 2
#Append the remainder to the binary string
            binary += str(remainder)
            D = D // 2
#Return the binary string reversed
        return binary[::-1]
def main():
    decimal_num=int(input('Enter decimal number: '))
    result = decimal_to_binary(decimal_num)
    if result is None:
        print('Please enter positive decimal number')
    else:
#Print the binary representation.
        print('The binary representation of the given decimal number is', result)
if __name__ == "__main__":
    main()
