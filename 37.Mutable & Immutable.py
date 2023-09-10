# Immutable objects are objects whose state cannot be changed after they are created. 

# Mutable objects,are objects whose state can be modified after they are created. 
# When you modify a mutable object, you are changing its internal state directly.


# Immutable Objects: 
     #1. Integers
     #2. Strings
     #3. Tuples

x = 5
y = x  # y is assigned the value of x (not a reference to x)
y += 1  # This creates a new integer object for y, leaving x unchanged
print(x) 
print(y) 


# **********
# Mutable Objects:
    # 1.List
    # 2.Dictionaries:
    # 3.Sets

numbers = [1, 2, 3]
numbers.append(4)  # Modifies the original list by adding an element
print(numbers) 

