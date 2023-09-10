# decorator itself is a function that takes another function as an argument and 
# typically returns a new function that wraps or extends the behavior of the original function


from functools import wraps

def my_decorator(func):
    # @wraps(func)
    def wrapper():
        """Wrapper function docstring."""
        print("Before calling the original function")
        func()
        print("After calling the original function")
    return wrapper

@my_decorator
def say_hello():
    """Original function docstring."""
    print("Hello!")

print(say_hello.__name__)      # Output: "say_hello"
print(say_hello.__doc__)       # Output: "Original function docstring."
