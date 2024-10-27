# To find the sum of numbers in a list 'L'
def sum_of_all_num(L):
    total=sum(float(num) for num in L)   # float in Python accepts both float point no. & integers
    return total

# To find the average of numbers in a list 'L'
def avg(L):
    avg=sum_of_all_num(L)/len(L)
    return avg

def main():
    L=list(input("Enter the numbers separated by space: ").split())
    if len(L)==0:
       return None
    elif len(L)==1: # If list has only 1 no., then we can't calculate sum & average
        print("Please enter more than one number.")
        return None
    else:
        print(f"The sum of all the numbers present in the list is {sum_of_all_num(L)}")
        print(f"The average of the numbers present in the list is {avg(L)}")

if __name__ == "__main__":
    main()