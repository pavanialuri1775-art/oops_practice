#
class Student:
    def display(self,name,marks):
        self.name=name
        self.marks=marks
        return f'{self.name} has scored {self.marks}'
s=Student()
print(s.display("pavani",98))

#2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print(f'Name:{self.name}')
        print(f'Salary:{self.salary}')
e=Employee("pavani",50000)
e.show_details()
#3
class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("deposit cannot be negative")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("withdraw impossible")
    def show_balance(self):
        return self.__balance
b=Bank(50000)
b.deposit(10000)
print(b.show_balance())

#4
class Vehicle:
    def start(self):
        print("vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car strated")
c=Car()
c.drive()
v=Vehicle()
v.start()

#5
class Animal:
    def sound(self):
        print("animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
c=Cat()
c.sound()#Meow
d=Dog()
d.sound()#Bark

#
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>50:
            print("pass")
        else:
            print("fail")
s=Student("pavani",35)
s.grade()#fail

#
class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("depoit cannot be negative")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("withdraw impossible")
    def check_balance(self):
        return self.__balance
a=ATM(5000)
a.deposit(10000)
print(a.check_balance()

#
class Employee:
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("develops")
class Manager(Employee):
    def work(self):
        print("Manages")
d=Developer()
d.work()

#
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass
class Circle(Shape):
    def Area(self,radius):
        return 3.14*self.radius*self.radius
class Rectangle(Shape):
    def Area(self):
        print("rectangle has some area")
r=Rectangle()
r.area()

    
