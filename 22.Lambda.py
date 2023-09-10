# lambda functions doesn't have any name it will return only function
def add(x,y):
    return x+y

print(add(3,4))

add2=lambda a,b: a+b
print(add2(6,7))

print((lambda a,b: a+b)(9,7))




