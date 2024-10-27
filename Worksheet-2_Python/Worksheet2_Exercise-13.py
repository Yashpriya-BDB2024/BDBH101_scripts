# To extract the key whose value has the most unique values -
def most_unique_values(test_dict):
    set_val=[len(set(i)) for i in test_dict.values()]   # remove duplicates (using set()) & to get no. of unique elements present in each list (using len())
    max_elem_index=set_val.index(max(set_val))  # to find out which has the most unique elements & at which index in the list
    get_key=list(test_dict.keys())[max_elem_index]  # to retrieve the key from the given dictionary based on the above index
    return get_key

def main():
    test_dict={"Gfg": [5,7,7,7,7], "is": [6,7,7,7], "Best": [9,9,6,5,5]}
    print(f"Key whose value has most unique values: {most_unique_values(test_dict)}")
if __name__ == "__main__":
    main()
