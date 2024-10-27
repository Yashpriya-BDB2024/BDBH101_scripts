# To implement an insertion sort algorithm -
import random
def insertion_sort_descending(A):
# Sorting in descending order -
        for j in range(1, len(A)):  # It will iterate from key (j=1) to length of the array
            key=A[j]  # Key - element present at index 'j'
            i=j-1
            while i>=0 and A[i] < key:  # A[i] - previous to key; if previous element is less than the key, then swapping will take place
                A[i+1]=A[i]
                i=i-1
            A[i+1]=key
        return A

def insertion_sort_ascending(B):
# Sorting in ascending order -
    for j in range(1, len(B)):
        key = B[j]   # e.g.: key = B[1] = 8
        i = j - 1  # e.g.: i=1-1=0
        while i >= 0 and B[i] > key:  # A[i] - previous to key; if previous element is greater than the key, then swapping will take place ;  e.g.: B[0]=31 > 8
            B[i + 1] = B[i]  # Swapping - e.g.: B[0+1] = B[0], i.e., 31 will move to key's place
            i = i - 1
        B[i + 1] = key
    return B

def main():
    A = []
    for i in range(1, 50):
        a = random.randint(1, 50)
        A.append(a)
    B=[]
    for i in range(1, 100):
        b = random.randint(1, 50)
        B.append(b)
    print(f"Random array: {A}")
    print(f"Array sorted in descending order (insertion sort algorithm): {insertion_sort_descending(A)}")
    print(f"Random array: {B}")
    print(f"Array sorted in ascending order (insertion sort algorithm): {insertion_sort_ascending(B)}")

if __name__ == "__main__":
    main()
