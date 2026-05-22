#1 Student Marks System
class Student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks")
    def get_marks(self):
        return self.__marks
s=Student()
s.set_marks(85)
print(s.get_marks())

#2  Bank Account 
class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
b=BankAccount()
b.deposit(5000)
b.withdraw(2000)
print(b.get_balance())

#3
class Employee:
    def __init__(self):
        self.__salary=0
    def set_salary(self,salary):
        if salary>0:
            self.__salary+=salary
        else:
            print("salary cannot be negative")
    def get_salary(self):
        return self.__salary
e=Employee()
e.set_salary(50000)
print(e.get_salary())      

#4
class Mobile:
    def __init__(self):
        self.__password=""
    def set_password(self,password):
        self.__password=password
    def check_password(self,password):
        if self.__password==password:
            print("Phone Unlocked")
        else:
            print("wrong password")
m=Mobile()
m.set_password("1234")
m.check_password("1234")
m.check_password("5678")

    
        
