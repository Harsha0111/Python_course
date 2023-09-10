 # Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Subclass 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on instances
print(dog.speak()) 
print(cat.speak()) 

# eg:2
# Base class (parent class)
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.year} {self.make} {self.model}'s engine is now running."

# Derived class (child class)
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        return f"{self.year} {self.make} {self.model} car's engine is now running."

# Another derived class (child class)
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return f"{self.year} {self.make} {self.model} motorcycle's engine is now running."

# Create instances of the derived classes
car = Car("Toyota", "Camry", 2023, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, False)

# Call the start_engine method of each instance
print(car.start_engine()) 
print(motorcycle.start_engine()) 

