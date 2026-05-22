#4 Employee Details
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print('id:',self.id)
        print('name:',self.name)
        print('saraly:',self.salary)
e=Employee(6609,"pavani",50000)
e.display()

#5
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("deposit must be positive")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("withdraw impossible")
    def check_balance(self):
        return f'{self.name} has {self.balance}'
b=BankAccount("pavani",50000)
b.deposit(20000)
b.withdraw(10000)
print(b.check_balance())

#6  Car Information
class Car:
    def __init__(self,company,model,year):
        self.company=company
        self.model=model
        self.year=year
    def car_info(self):
        print("comapny:",self.company)
        print("model:",self.model)
        print("year",self.year)
c=Car("Tesla","Tesla Model 3",2020)
c.car_info()

        