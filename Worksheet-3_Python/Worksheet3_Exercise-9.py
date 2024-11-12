### Create a decorator to measure the execution time of a function.
### Please demonstrate using a sample function (add sleep for checking) and a decorator for this sample function that measures the execution time.

import time
import math
def execution_time(func):
    def wrapper(*args, **kwargs):
        begin=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"Execution time of '{func.__name__}': {end-begin} seconds.")
    return wrapper
@execution_time
def factorial(num):
    time.sleep(2)
    return math.factorial(num)
def main():
    num=int(input("Enter a number: "))
    factorial(num)
if __name__ == "__main__":
    main()