# To find the maximum & minimum value of a dictionary.
# Approach-1 (using built-in functions)
def find_max_in_dict(Dict):
    max_val=max(Dict.values())
    return max_val
def find_min_in_dict(Dict):
    min_val=min(Dict.values())
    return min_val

# Approach-2
def max_value(Dict):
    max_val=0   # Initialize the maximum value to 0
    for value in Dict.values():   # It will iterate through each value in the dictionary
        if max_val==0 or value > max_val:
            max_val = value   # If the value is greater than the max. value, then the max. value will now be that value.
    return max_val
def min_value(Dict):
    min_val = 0
    for value in Dict.values():
        if min_val==0 or value < min_val:
            min_val = value
    return min_val

def main():
    user_input = input("Enter the dictionary (format - key1:value1 key2:value2 ....) separated by space: ")
    items = user_input.split()
    Dict = {}
    for item in items:
        if ':' in item:
            key, value = item.split(':')
            Dict[key] = float(value)
        else:
            print("Invalid format")
            return
    print(f"Maximum value: {find_max_in_dict(Dict)}")
    print(f"Minimum value: {find_min_in_dict(Dict)}")
    print(f"Max.: {max_value(Dict)}")
    print(f"Min.: {min_value(Dict)}")

if __name__ == "__main__":
    main()