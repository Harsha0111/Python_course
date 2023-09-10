def add(x, y=5):
    result = (x + y)
    print (result)

# default can be specified after non default parameter
add(2)

default_y=3
def add2(x, y=default_y):
    result = (x + y)
    print (result)

# default can be specified after non default parameter
add2(2)
# see the old default value is only taken as value of y
# default_y=6