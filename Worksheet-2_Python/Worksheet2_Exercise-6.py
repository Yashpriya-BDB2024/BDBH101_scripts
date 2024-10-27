# To extract elements of a list, if it occurs more than 'k' times.
def more_than_k_times_occurrence(L, k):
    elem=set(i for i in L if L.count(i)>k)  # set - to ensure that elements occurring more than 'k' times are displayed only once in the output.
    return elem

def main():
    L=list(input("Enter the elements (no./alphabets/other characters) separated by space: ").split())
    if len(L) == 0:
        print("Empty list")
        return
    elif len(L) == 1:
        print("Please enter more than one element.")
        return
    k=input("Enter the minimum no. of occurrences: ")
    if k=="":
        print("No input given.")
        return
    else:
        k=int(k)
    if more_than_k_times_occurrence(L, k):
        print(f"Elements occurring more than {k} times: {more_than_k_times_occurrence(L, k)}")
    else:
        print(f"No elements occur more than {k} times.")
if __name__ == "__main__":
    main()