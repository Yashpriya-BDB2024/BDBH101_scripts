# To iterate over a dictionary & print key and values
def print_key_values(Dict):
    for key, value in Dict.items():
        print(f"Key: {key}, Value: {value}")

def main():
    Dict=input("Enter the dictionary (format - key1:value1 key2:value2 ....): ")
    items=Dict.split()
    key_value_pairs=[]
    for item in items:
        if ":"  not in item:  # To handle those cases when there is other character instead of ':'
            print("Invalid format")
            return
        key, value = item.split(":")
        if key in dict(key_value_pairs): # To handle those cases when keys are not unique.
            print("Duplicate keys found.")
            return
        key_value_pairs.append((key, value))
    Dict=dict(key_value_pairs)
    print_key_values(Dict)

if __name__ == "__main__":
    main()


