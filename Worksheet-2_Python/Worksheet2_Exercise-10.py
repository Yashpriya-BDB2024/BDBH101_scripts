# To sum all the values of a dictionary
def sum_all_values(Dict):
    total=sum(Dict.values())
    return total

def main():
    user_input= input("Enter the dictionary (format - key1:value1 key2:value2 ....) separated by space: ")
    items=user_input.split()  # Split the input by spaces to get key-value pairs
    Dict={}
    for item in items:  # Loop through each item
        if ':' in item:  # Check if the item contains ':'
            key, value = item.split(':')   # Split item into key & value parts
            Dict[key]=float(value)
        else:
            print("Invalid format")
            return
    print(f"Sum of all the values in the dictionary: {sum_all_values(Dict)}")

if __name__ == "__main__":
    main()
