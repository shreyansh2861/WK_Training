class Bank:

    def __init__(self, roi):
        self.roi = roi
    
    def get_roi(self):
        return self.roi
# base classes override the method from parent class

class SBI(Bank):

    def __init__(self, roi):
        self.base = 5
        super().__init__(roi)
    
    def get_roi(self):
        return self.roi + self.base

class HDFC(Bank):

    def __init__(self, roi):
        self.base = 6
        super().__init__(roi)

    def get_roi(self):
        return self.roi + self.base


b1 = SBI(10)
print(b1.get_roi())

b2 = HDFC(8)
print(b2.get_roi())