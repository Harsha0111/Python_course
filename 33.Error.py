
try:
    result = 10 / 0
    # result = 10 / h
except ZeroDivisionError as e:
    print(f"Error: {e}")
except NameError as e:
    print (f"Value Error: {e}")
else:
    print (result)
finally:
    print ("I'll be running always!!!")


