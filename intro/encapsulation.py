#Encapsulation:Encapsulation is the process of binding data and methods together into a single unit (class) and restricting direct access to some data.
#it is achieved using private variables
#getter/setter methods
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
obj = BankAccount(1000)
obj.deposit(500)
print(obj.get_balance())

#Technical Purpose
#Data hiding
#Security
#Controlled access to data