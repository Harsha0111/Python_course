# Can change the oder, add/delete any item in List:
list = ["Hi", "I'Am", "A", "List[]"]

print (list)
print(f"Before Modify: {list[-1]}")
list[-1]="Modified!!!.."
print(f"After Modify: {list[-1]}\n")
list.append("New")
print (list)
list.remove("New")
print (list)
print("\n")

# Can't modify i.e., we can't add/delete any item in Tuple:
tuple = ("Hi", "I'Am", "A", "Tuple()")
tuple2 = "Hi", "I'Am", "A", "Tuple"

print(tuple)
print(tuple2)
print(f"Value of 0th element: {tuple[0]}\n")
# tuple.remove("Hi")

# Can add/delete any item, but no duplicate element can be added in Sets 
# and also can't access items in subscript notation i.e., sets[1] since they willn't be in oder:
sets = ["Hi", "I'Am", "A", "Sets{}"]

print(sets)
print(sets[3])
sets.append("Hello")
print(sets)
sets.remove("Hello")
print(sets)