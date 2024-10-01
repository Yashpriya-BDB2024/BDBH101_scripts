#To convert the given binary representation into its decimal number
def binary_to_decimal_number(B):
#Convert the binary string B to decimal using base 2
    return int(B, 2)
def main():
    binary_rep=input('Enter the binary representation: ')
    result=binary_to_decimal_number(binary_rep)
    print('The decimal number of the given binary representation is', result)
if __name__ == "__main__":
    main()