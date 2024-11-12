### Write  a lambda function to sort a list of strings by the last character.

def sort_by_last_char(L):
    Sorted_strings = sorted(L, key=lambda s: s[-1])   # By using key, we are telling sorted() to sort based on last character.
    return Sorted_strings
def main():
    L=list(input("Enter the strings separated by space: ").split())
    print(sort_by_last_char(L))
if __name__ == "__main__":
    main()

