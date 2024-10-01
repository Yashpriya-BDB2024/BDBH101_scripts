#To compute the power -
def compute_power(base, exponent):
#Calculate base raised to the power of exponent
    return base ** exponent
def main():
    base=int(input("Enter a number to be considered as base: "))
    exponent=int(input("Enter a number to be considered as n-th power: "))
#Compute the power using the compute_power function.
    result=compute_power(base, exponent)
    print(f"{base} raised to the power {exponent} is {result}")
if __name__ == "__main__":
    main()