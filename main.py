# A SIMPLE BANKING SYSTEM
class BankAccount:
    """ This block contains the public account opening detailis"""
    def __init__(self,account_name,account_number):

        self.name = account_name
        self.number = account_number
        self.limit = 1000000
        self.balance = 0 #the opening acct balance
        

    def deposit(self,amount):
        self.minimum = 100  # defines the minimum deposit
        self.amount = amount
        if amount > self.minimum and amount <= self.limit:
            self.balance += amount
        elif amount < self.minimum:
            raise ValueError("The amount is too small")
        else:
            raise ValueError("Request Failed : 'The amount is above your limit")

    def getbalance(self):
        balance = self.balance
        return balance

my_account = BankAccount("John Doe", "1234567890")
        