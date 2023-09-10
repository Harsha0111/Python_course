local = {"Abi", "Balu", "Ravi", "Shalu"}
abroad = {"Balu", "Meena", "Shivani"}

# difference
local_friends=local.difference(abroad)
print(local_friends)

local_friends=abroad.difference(local)
print(local_friends)

# union (Adds all unique name)
union=abroad.union(local)
print(f"Union :{union}")

# both (prints only common name)
both=abroad.intersection(local)
print(f"Common: {both}")
