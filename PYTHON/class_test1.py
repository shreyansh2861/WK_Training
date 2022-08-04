class Person:

    def __init__(self,pname,age):
        self.pname = pname; # self._pname = pname becomes protected sel.__pname = pname becomes private
        self.age = age
    
    def greet(self):
        print(f"Hello{self.pname}")

p1 = Person("Shreyansh", 21)
p2 = Person("Arnav", 16)

# print(p1.__doc__)
# print(p1.__dict__)
# print(p1.__class__)
# print(p1.__module__)
del p1.age
print(p1.__dict__)
print(p2.__dict__)
p1.age = 21
print(p1.__dict__)


# builtin class methods

print(getattr(p1,"pname"))
setattr(p1, 'pname', 'Shreyansh')
print(getattr(p1,"pname"))

print(hasattr(p1,"pname"))
print(hasattr(p1, "p_name"))
print(getattr(p1,"age"))
delattr(p1,'age')
print(hasattr(p1, "age"))