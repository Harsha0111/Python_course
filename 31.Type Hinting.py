# Type Hinting is available in python 3.5 / later

# Function with type hints
def add(a: int, b: int) -> int:
    """
    Add two integers and return the result.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
        
    Returns:
        int: The sum of a and b.
    """
    return a + b

# Using the function with type hints
result = add(5, 3)
print(result)  # Output: 8

# Type hints for class attributes
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name}, and I am {self.age} years old."

# Using class with type hints
person = Person("Alice", 30)
print(person.greet())  # Output: Hello, my name is Alice, and I am 30 years old.

