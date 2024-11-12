### Create a logging decorator to record function calls, arguments, and return values.

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result=func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
    return wrapper

@logging_decorator
def add(a, b):
    return a+b
def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    add(a, b)
if __name__ == "__main__":
    main()