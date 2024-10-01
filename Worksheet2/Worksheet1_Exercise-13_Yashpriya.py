#To replace all the occurrences of a particular character with another character.
def replace_occurrences(S, c, d):
#Use the replace method to substitute all the occurrences of a particular character with another character.
    replaced_string=S.replace(c , d)
#Return the modified string
    return replaced_string
def main():
    string=(input("Enter a string: "))
    character=(input("Enter a character that you want to replace: "))
    another_character=(input("Enter a replacing or new character: "))
    result=replace_occurrences(string, character, another_character)
    print("Modified string: ",result)
if __name__ == "__main__":
    main()

