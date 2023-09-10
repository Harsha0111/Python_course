# class name will begin in Cap's letter
class Student:
    def __init__(self) :
        # self referes to instance being created for obj
        self.name = "Bob"
        self.grades = (67,90,75,87,56)
   
    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student() #create an object i.e., creates new empty container & 
                        #  runs the function/method inside class
print (student.name)
print (student.grades)

print (Student.average(student))
print (student.average()) 


# eg:2
class Student2:
    def __init__(self, name) :
        self.name = name

student2 = Student2("Anuratha") 

print (student2.name)