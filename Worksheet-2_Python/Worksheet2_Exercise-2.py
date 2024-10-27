# max & min are built-in functions in Python
# To find the maximum number in a list 'L'
def find_max(L):
    max_num=max(num for num in L)
    return max_num

# To find the minimum number in a list 'L'
def find_min(L):
    min_num=min(num for num in L)
    return min_num

def main():
    L = list(input("Enter the numbers separated by space: ").split())
    if len(L) == 0:
        return None
    elif len(L) == 1:
        print("Please enter more than one number.")
        return None
    else:
        print(f"The maximum number present in the given list: {find_max(L)}")
        print(f"The minimum number present in the given list: {find_min(L)}")

if __name__ == "__main__":
    main()
