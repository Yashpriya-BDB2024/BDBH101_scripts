#To trim the leading whitespace characters from a string 'S'.
def trim_leading_whitespace(S):
#Check if the string is empty
    if len(S) == 0:
        print('Empty string')
    else:
#Use lstrip() to remove the leading whitespaces in the given string.
        return S.lstrip()
def main():
    string=input("Enter a string with leading whitespace characters, but without quotes: ")
    result=trim_leading_whitespace(string)
    print(result)
if __name__ == "__main__":
    main()

