### Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

def rearrange_positive_negative_num(A):
    neg_num=list(filter(lambda n: n<0, A))
    neg_num.sort()
    zeroes=list(filter(lambda n: n==0, A))
    pos_num=list(filter(lambda n: n>0, A))
    pos_num.sort()
    return neg_num + zeroes + pos_num   # concatenation
def main():
    A=list(map(int, input("Enter numbers (separated by comma): ").split(',')))
    print(rearrange_positive_negative_num(A))
if __name__ == "__main__":
    main()