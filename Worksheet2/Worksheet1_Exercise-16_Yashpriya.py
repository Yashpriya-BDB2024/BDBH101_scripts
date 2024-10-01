#To check if the given two strings are anagram of each other or not.
def check_anagram(S1, S2):
#Remove spaces and convert both into lowercase.
    S1=S1.replace(" ", "").lower()
    S2=S2.replace(" ", "").lower()
#Sort the characters of both the strings.
    S1_sorted=sorted(S1)
    S2_sorted=sorted(S2)
#Compare both the sorted strings, if they are equal, then they are anagram of each other.
    return S1_sorted == S2_sorted
def main():
      string1=input("Enter the first string: ")
      string2=input("Enter the second string: ")
      if check_anagram(string1, string2):
        print(f"Both the strings - '{string1}' and '{string2}' are anagram of each other.")
      else:
          print('They are not the anagram of each other.')
if __name__ == "__main__":
        main()
