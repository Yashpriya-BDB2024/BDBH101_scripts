### You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
### Create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...].

def capitalize(fruits):
# Each fruit present in the input list will get capitalized & will be stored in the list called 'capitalized_fruits'.
    capitalized_fruits=[fruits.capitalize() for fruits in fruits]   # Use of list comprehension
    print(f"Capitalized fruits: {capitalized_fruits}")
def main():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    capitalize(fruits)
if __name__ == "__main__":
    main()
