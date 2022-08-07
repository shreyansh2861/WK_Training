from abc import ABC,ABCMeta, abstractmethod

class Loan(ABC):

    @abstractmethod
    def cust_verification(self):
        pass

class ICICILoan(Loan):
    def cust_verification(self):
        adhaarNumber = input("Enter Your Adhaar Number : ")
        print("sucessfully Verified")
    
    def issue_loan(self, amount):
        self.cust_verification()
        print(f"Your loan for amount {amount} has been approved and amount disbursed")
    

l1 = ICICILoan()

l1.issue_loan(102000)