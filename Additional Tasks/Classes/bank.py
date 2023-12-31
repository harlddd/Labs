
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def getbalance(self):
        return self.balance


acct = BankAccount("1234")
print(acct.getbalance()) 
acct.deposit(100)
print(acct.getbalance()) 
acct.withdraw(50)
print(acct.getbalance()) 