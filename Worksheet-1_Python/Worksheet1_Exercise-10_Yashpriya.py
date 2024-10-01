#To concatenate two strings 'S1' and 'S2'.
def concatenate_strings(S1, S2):
#Check if either or both of the strings is empty, if so, then return None.
    if S1 == "" or S2 == "" or (S1 == "" and S2 == ""):
        return None
    else:
#Remove whitespaces from both the strings.
        S1=S1.strip()
        S2=S2.strip()
#Concatenate both the strings together.
        return ''.join([S1, S2])
def main():
    S1 = input("Enter the first string: ")
    S2 = input("Enter the second string: ")
#Call the concatenate_strings function.
    result = concatenate_strings(S1, S2)
    if result is None:
        print("No valid result to display.")
    else:
        print(f"The concatenated string is {result}")
if __name__ == "__main__":
    main()