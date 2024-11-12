### Write a function division() that accepts two arguments.
### The function should be able to catch an exception such as ZeroDivisionError, ValueError, or any unknown error you might come across.
### Also, add a “finally” construct.

def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Denominator can't be zero.")
        return None
    except Exception as err:
        print(f"Something else broke: {err}")
        return None
    finally:
        print("Operation completed.")
def main():
    try:
        a=int(input("Enter the numerator: "))
        b=int(input("Enter the denominator: "))
        result=division(a, b)
        if result is not None:
            print(f"Quotient: {result}")
    except ValueError:
        print("Invalid input.")
if __name__ == "__main__":
    main()