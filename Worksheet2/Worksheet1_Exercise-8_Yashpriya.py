#To print the first half of a string 'S'
def print_first_half(S):
#Check if the string is empty, if so, then return.
    if len(S) == 0:
        return
#Calculate the index that marks the end of the first half of the string.
    half_string_index=len(S) // 2
#Print it from start to the above calculated index.
    print(S[:half_string_index])
def main():
    string=input('Enter a string: ')
    print_first_half(string)
if __name__ == "__main__":
    main()