#Encapsulation 
#private variables
#protected variables
#getter methods
#setter methods
#Private variables are written using:   __(double underscore)

#ex1
class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
       self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def get_balance(self):
        return self.__balance
account=Bankaccount(8000)
account.deposit(4000)
print(account.get_balance())

#ex2
#Private  variables
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def set_salary(self,salary):
        if salary>=0:
            self.__salary+=salary
        else:
            print("salary cannot be negative")
    def get_salary(self):
        return self.__salary
sal=Employee(60000)
sal.set_salary(20000)
print(sal.get_salary())

