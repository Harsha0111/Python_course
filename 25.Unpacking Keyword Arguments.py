# * --> takes multi arguments at a time
# ** --> dictionary format

# packing arg into dict
def named(**allargs):
    print (allargs)

named(name= "Bob", age =32)



# unpacking dict into named arg
def named2(name, age):
    print(name, age)


details = {"name": "Anu", "age": 24}

# named2(details)
# used to pass multiple keyword arg
named2(**details)      # named2(name= "Anu", age =24) 