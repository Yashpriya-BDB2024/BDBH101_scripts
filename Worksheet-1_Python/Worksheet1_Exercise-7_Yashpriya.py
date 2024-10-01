#To print individual digits of a number 'N'
def print_digits(N):
#Check if N is negative, if so, then return.
    if N <= 0:
        return
#Initialize an empty string to hold the digits.
    digits = ""
    while N > 0:
#Get the last digit from N
        digit = N % 10
#Prepend the digit to the digits string.
        digits = str(digit) + digits
#Remove the last digit from N
        N //= 10
#Loop through each digit in the given string.
    for digit in digits:
        print(digit)
    return len(digits)
def main():
    num=int(input("Enter the number: "))
    print_digits(num)
if __name__ == "__main__":
    main()
