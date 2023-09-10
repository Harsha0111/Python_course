def add(x,y):
    result=x+y
    print(result)

add(5,3)

# add(5)

# eg:2
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Harsha")


def say_hello2(name, surname):
    print(f"Hello, {name} {surname}")

# postional arguments
say_hello2("Harsha","Selvi")

# keyword arguments
say_hello2(surname="Selvi", name="Harsha")

# need to mix both type of arguments na you need to pass postional as first
say_hello2("Selvi", surname="Harsha")