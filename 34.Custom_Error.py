class MyCustomError(ValueError):
    pass

# Using the custom exception
def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed.")
    return a / b

try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"Custom Error: {e}")
else:
    print(f"Result: {result}")
