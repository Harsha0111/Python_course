class Person:
    def __init__(self, name,age) :
        self.name = name
        self.age = age
       
    # def __str__(self):
    #     return f"Person {self.name} , {self.age} years old"

    # alter method to str
    # def __repr__(self):
    #     return f"<Person {self.name} , {self.age} years old>"
        
 
bob = Person("Bob", 34)
print(bob)