#  To print the duplicate elements in a list 'L'
def duplicates(L):
# It will iterate through whole list & if any element occurs more than once, then it is stored in 'duplicate'.
    duplicate=set(i for i in L if L.count(i)>1)  # set - to ensure that duplicate elements are listed only once in the output.
    return duplicate

def main():
    L=list(input("Enter the elements (no./alphabets/other characters) separated by space: ").split())
    if len(L)==0:
        return None
    elif len(L)==1:  # If there is single element in the list, then there is no duplicate present.
        print("Please enter more than one element.")
    elif duplicates(L):
        print(f"Duplicate elements: {duplicates(L)}")
    else:
        print("No duplicate element present.")
if __name__ ==  "__main__":
    main()
