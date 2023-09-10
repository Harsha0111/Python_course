# after defining a function only we can call a function
# hello()

def hello():
    print("Hello, Welcome All!!!")

# need to call a function to print the msg in it.
hello() 

# don't use keywords as the function name like print,..

def welcome():
    welcome_msg = input("Enter the Welcome Msg:")
    # hello = hello + welcome_msg
    hello = welcome_msg
    print(f"Welcome_msg: {hello}")
    # hello is defining line 12 only and we can't use in same line i.e., x = x+t (x doesn't have any value)

welcome()


# eg:2
frd=[]

def add_frd():
    frd.append("Rolf")

# frd=[]
# after the line 28 running only function will be called

add_frd()
add_frd()
add_frd()

print(frd)


