#To find the sum of squares of first N numbers
def square_of_first_N_numbers(N):
#Return the square of N
    return N * N
def sum_of_squares_of_first_N_numbers(N):
#Check if N is less than or equal to 0
    if N <= 0:
        return None
    else:
#Initialize the total to 0
        total=0
#Loop through all the numbers from range 1 to N
        for i in range(1, N + 1):
#Add the square of the current number to the total
            total += square_of_first_N_numbers(i)
        return total
def main():
    num=input("Enter the number:")
    if num.isdigit():
#Convert the input to integer
        num=int(num)
        result = sum_of_squares_of_first_N_numbers(num)
#Check if result is None (as in case of non-positive input).
        if result is None:
            print('Please enter positive number')
        else:
            print('The sum of square of first', num,'numbers is', result)
    else:
        print('Invalid input')
if __name__ == "__main__":
#Call the main function
    main()
