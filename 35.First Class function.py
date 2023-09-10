# Define two functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Create a higher-order function that takes an operation function as an argument
def perform_operation(operation, x, y):
    result = operation(x, y)
    return f"Result: {result}"

# Use the higher-order function with different operation functions
add_result = perform_operation(add, 5, 3)
subtract_result = perform_operation(subtract, 10, 7)

print(add_result)       
print(subtract_result)  
