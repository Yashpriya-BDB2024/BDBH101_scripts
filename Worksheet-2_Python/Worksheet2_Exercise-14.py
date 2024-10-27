# To remove all the duplicate words from a given sentence using a dictionary -
def remove_duplicate_words(words):
    unique_dict={}  # Initialize an empty dictionary to store the unique words
    for i in words:  # Loop through each word in the list
        if i not in unique_dict:  #  Add the word to the dictionary if it's not already present.
            unique_dict[i]=None   # Store that word as a key; value is not needed.
    result=' '.join(unique_dict.keys())   # Concatenation
    return result
def main():
    sentence=input("Enter a sentence: ")
    words=sentence.split()
    print(remove_duplicate_words(words))
if __name__=='__main__':
    main()