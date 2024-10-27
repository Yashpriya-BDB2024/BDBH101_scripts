# To extract words from a string list 'L', whose first character is 'k'
def extract_words_based_on_first_char(L, k):
    words=[i for i in L if i[0].lower()==k.lower()]  # lower() - to avoid case-sensitive issue
    return words

def main():
    L=list(input("Enter the words (separated by space): ").split())
    if len(L) == 0:
        print("Empty list")
        return
    k=input("Enter the first character you want to look for: ")
    if k=="":
        print("No first character specified.")
    else:
        print(f"The word(s) starting with '{k}' is/are: {extract_words_based_on_first_char(L, k)}")
if __name__ == "__main__":
    main()
