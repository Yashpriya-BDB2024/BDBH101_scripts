# To remove all the occurrences of an element from a list 'L'
def remove_all_occurrences_of_elem(L, elem_list):
    list=[i for i in L if i not in elem_list]
    return list

def main():
    L=list(input("Enter the elements (no./alphabets/other characters) separated by space: ").split())
    if len(L) == 0:
        print("Empty list")
        return
    elem_list=list(input("Enter the element(s) (separated by space) whose all the occurrences you want to remove: ").split())
    if len(elem_list) == 0:
        print("No elements specified for removal.")
        return
    updated_list=remove_all_occurrences_of_elem(L, elem_list)
    if len(updated_list)==len(L):
        print(f"No occurrences of {elem_list} found.")
    else:
        updated_list=print(f"Updated list after removing {elem_list} from the given list: {remove_all_occurrences_of_elem(L, elem_list)}")
if __name__ == "__main__":
    main()

