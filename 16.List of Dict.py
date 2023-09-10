#  Normal list 
list = ["Abi", "Sri", "Charu"]

# need to store multiple value for individual ,then use dict in it.
list = [{"name": "Abi", "age": 21}, {"name": "Sri", "age": 34}, {"name": "Charu","age": 19}]

print(list[0]["name"])
print(list[0]["name"],["age"])

# eg:2
student_attendence = {"Harish": 70, "Mathu": 67, "Sanju": 80}

for student, attendence in student_attendence.items():
    print(f"\n{student}: {attendence}")