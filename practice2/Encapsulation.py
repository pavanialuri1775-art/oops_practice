#7 ATM Machine
class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("deposit amount must be positive")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("withdraw impossible")
    def get_balance(self):
        return self.__balance
a=ATM(40000)
a.deposit(5000)
a.withdraw(2000)
print(a.get_balance())

#8 Password Manager
class PasswordManager:
    def __init__(self,password):
        self.__password=password
    def set_password(self,password):
        self.__password=password
    def get_password(self):
        return self.__password
p=PasswordManager("pavani")
print(p.get_password())
p.set_password("pavani1775")
print(p.get_password())

#9 Marks Validation
class Student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("marks cannot be negative")
    def get_marks(self):
        return self.__marks
s=Student()
s.set_marks(95)
print(s.get_marks())