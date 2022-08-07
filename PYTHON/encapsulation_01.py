class Computer:

    def __init__(self, price):
        self.__maxprice = price
    
    def sell(self):
        print(f"Selling Price is {self.__maxprice}")
    
    def setMaxPrice(self, price):
        self.__maxprice = price

    def getMaxPrice(self):
        return self.__maxprice

    @property
    def maxprice(self):
        return self.__maxprice

    # maxprice1 = property(getMaxPrice)

    @maxprice.setter
    def maxprice(self, value):
        self.__maxprice = value


c = Computer(50000)

c.sell()

c.setMaxPrice(60000)

c.sell()

print(c.getMaxPrice())

# print(c.maxprice)

# print(c.maxprice1)

c.maxprice = 50555

print(c.maxprice)

