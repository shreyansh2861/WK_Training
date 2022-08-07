class Loan:
    def __init__(self, roi):
        self.roi = roi

    def __add__(self, other):
        return self.roi + other.roi

    def __sub__(self, other):
        return self.roi - other.roi
    
    def __lt__(self, other):
        return self.roi < other.roi
    
    def display(self):
        print(f"The current rate of interest is {self.roi}")

l1 = Loan(7)
l2 = Loan(8)

print(l1 + l2)
print(l1 - l2)
print(l1 < l2)