class ClassTest():
    def instance_method(self):
        print(f"Called instance method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called Static method")

# obj creation
test = ClassTest()

# ClassTest.instance_method(test)
test.instance_method()

ClassTest.class_method()
ClassTest.static_method()
