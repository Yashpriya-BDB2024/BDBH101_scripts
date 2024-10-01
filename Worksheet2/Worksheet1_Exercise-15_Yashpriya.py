#To count the number of occurrences of a word 'W' in a sentence 'S'.
def count_word_occurrences(S, W):
#Convert both the sentence and word into lowercase.
    S_lower = S.lower()
    W_lower = W.lower()
#Split the given sentence into a list of words.
    words = S_lower.split()
#Count the occurrences of a given word in the given sentence.
    count = words.count(W_lower)
    return count
def main():
    sentence = input("Enter a sentence: ")
    word = input("Enter a word that you want to count: ")
    if len(sentence) == 0:
        return
    if len(word) == 0:
        return
    result=count_word_occurrences(sentence, word)
    print(f"The word '{word}' occurs {result} times in the sentence.")
if __name__ == "__main__":
    main()