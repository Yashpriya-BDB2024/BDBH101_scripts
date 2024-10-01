# To find the highest frequency character in a string 'S'
def highest_freq_char(S):
#List to store the characters with the highest frequency.
    highest_chars = []
#Initialize the highest count to 0
    highest_count = 0
#Loop through each character in the given string.
    for char in set(S):
#Count the occurrences of the character.
        count = S.count(char)
#If the count is greater than the highest count
        if count > highest_count:
#Update the highest count
            highest_count = count
            highest_chars = [char]
#If the count is equal to the highest count
        elif count == highest_count:
            highest_chars.append(char)
    return highest_chars
def main():
    string = input("Enter a string: ")
    result = highest_freq_char(string)
    print(f"The highest frequency characters are: {', '.join(result)}")
if __name__ == "__main__":
    main()