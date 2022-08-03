class Person:

    def __init__(self,pname,age):
        self.pname = pname;
        self.age = age;
    
    def greet(self):
        print(f"Hello{self.pname}")

p1 = Person("Shreyansh", 21)


print(p1.__doc__)
print(p1.__dict__)
print(p1.__class__)
print(p1.__module__)