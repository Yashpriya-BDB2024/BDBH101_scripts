### sentence = "Hello, how are you?". Write a dictionary comprehension to map words to their reverse in a sentence.
### The output should be - {'Hello,': ',olleH', 'how': 'woh', 'are': 'era', 'you?': '?uoy'}

def map_reverse(sentence):
    reverse={word: word[::-1] for word in sentence.split()}
    print(reverse)
def main():
    sentence="Hello, how are you?"
    map_reverse(sentence)
if __name__ == "__main__":
    main()