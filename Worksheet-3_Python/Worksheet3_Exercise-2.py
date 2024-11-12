### You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
### Make a variable named fruits_with_only_two_vowels.
### Use list comprehension to produce ['mango', 'kiwi', 'strawberry'], a list of fruits with only two vowels.

def fruits_with_vowels(fruits):
    vowels = 'aeiou'
# For each fruit, count the total occurrences of vowels.
# If the count is 2, then, include it in the resulting list.
    fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(fruit.count(char) for char in vowels) == 2]
    print(f"Fruits with only 2 vowels: {fruits_with_only_two_vowels}")
def main():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    fruits_with_vowels(fruits)
if __name__ == '__main__':
    main()
