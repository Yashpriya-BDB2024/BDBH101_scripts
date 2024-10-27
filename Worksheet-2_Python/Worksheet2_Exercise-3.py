# To find even numbers in a list 'L'
def find_even_num(L):
# It will iterate through whole list & if it finds remainder as 0, then that number will be stored in the list called 'even'
    even=[num for num in L if num % 2 == 0]
    return even

def main():
    L=list(map(int, input("Enter the numbers separated by space: ").split()))  # map(int, ...) applies the float() to each substring, converting them into integers.
    if len(L)==0:
       return None
    if find_even_num(L):
        print(f"Even numbers: {find_even_num(L)}")
    else:
        print("No even no. present")
if __name__ == "__main__":
    main()