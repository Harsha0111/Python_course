local = {"Abi", "Balu"}
abroad = {"Abi","Balu"}

# '==' used to compare only values are equal in both 
print ( local == abroad)

# 'is' keyword is used check whether 2 elements are same
print ( local is abroad)
print ( id(local) , id(abroad))

local = abroad
print ( local is abroad)