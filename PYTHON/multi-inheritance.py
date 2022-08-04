class Base1:
    def sayhi(self):
        print("Hi from Base 1")
    
    def sayhiagain(self):
        print("Hi again from Base 1")
class Base2:
    def sayhi(self):
        print("Hi from Base 2")

class Base12(Base1, Base2):
    def sayhello(self):
        #print("Hello from Base 12")
        super().sayhiagain()

b12 = Base12()
b12.sayhi()
b12.sayhello()

print(Base12.mro())