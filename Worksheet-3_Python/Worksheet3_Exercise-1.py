### You are given a list called fruits =  ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'].
### Create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...].

def capitalize(fruits):
    capitalized_fruits=[fruits.capitalize() for fruits in fruits]
    print(f"Capitalized fruits: {capitalized_fruits}")
def main():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    capitalize(fruits)
if __name__ == "__main__":
    main()
