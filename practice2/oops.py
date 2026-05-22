#5
'''Create base class:
Account
Subclasses:
SavingsAccount
CurrentAccount
Functions:
deposit()
withdraw()
Savings account gives interest.
Current account has minimum balance rule.'''

class Account:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print('withdraw impossible')
class SavingsAccount(Account):
    def add_interest(self):
        interest=self.balance*0.05
        self.balance+=interest
class CurrentAccount(Account):
    def withdraw(self, amount):
        minimum_balance = 1000
        if  self.balance - amount >= minimum_balance:
            self.balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Minimum balance should be maintained")
s = SavingsAccount(5000)
s.deposit(2000)
s.add_interest()
print("Savings Balance:", s.balance)
c = CurrentAccount(8000)
c.withdraw(7500)
print("Current Balance:", c.balance)


    
        