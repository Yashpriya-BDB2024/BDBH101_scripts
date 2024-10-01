#To check if a given number is a prime number or not.
def check_prime(N):
#Ensure N is an integer
    N=int(N)
#Check if N is less than 2, as prime numbers are greater than 1
    if N < 2:
        return False
#Loop through potential divisors from 2 to square root of N
    for i in range(2, int(N**0.5)+1):
           if N % i == 0:
               return False
#If no divisors found, then return True
    return True
def main():
    num=int(input('Enter a number: '))
    if check_prime(num):
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')
if __name__ == "__main__":
    main()
