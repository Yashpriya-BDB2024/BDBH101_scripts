### Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
### Create a dictionary of numbers and their squares, excluding odd numbers using dictionary comprehension

def squares(num_list):
    squares_of_even_num={i: (i*i) for i in num_list if i%2==0}
    print(f"Square of even numbers: {squares_of_even_num}")
def main():
    num_list=[1,2,3,4,5,6,7,8,9,10]
    squares(num_list)
if __name__ == "__main__":
    main()