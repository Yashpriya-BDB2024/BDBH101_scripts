#To find the first occurrence of a character in a string 'S'.
def find_first_occurrence(S, c):
#Check if the string is non-empty and input is a single character.
    if (type(S) is not str or len(S) == 0) or (len(c) != 1):
        print("Error: 'S' must be a non-empty string and 'c' must be a single character.")
        return
#Loop through each index in the given string.
    for index in range(len(S)):
#Check if the character at the current index matches the input character.
        if S[index:index+1] == c:
            print(f"The first occurrence of {c} is at index {index}.")
            return
    print(f"The character {c} is not present in the given string.")
def main():
    string=input("Enter a string: ")
    character=input("Enter the character that you want to find in the given string: ")
    find_first_occurrence(string, character)
if __name__ == "__main__":
    main()
