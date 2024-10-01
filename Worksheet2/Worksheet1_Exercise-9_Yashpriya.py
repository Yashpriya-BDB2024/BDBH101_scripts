#To print alternate characters of a string 'S'.
def print_alternate_char(S):
#Use slicing to print every alternate characters
    alternate_chars=S[::2]
    print(alternate_chars)
def main():
    string=input('Enter a string: ')
    print_alternate_char(string)
if __name__ == "__main__":
    main()