#1
#common behaviour-start
#Differet implementation--> overriding
class Vehicle:
    def start(self):
        print("vehicles have to be started to get ride")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")
class Truck(Vehicle):
    def start(self):
        print("Truck starts with heavy engine")
t=Truck()
t.start()

#2  Person Hierarchy
class Person:
    def work(self):
        print("person does some work")
class Student(Person):
    def work(self):
        print("Studies")
class Teacher(Person):
    def work(self):
        print("Teaches")
class Doctor(Person):
    def work(self):
        print("Treats patients")
t=Teacher()
d=Doctor()
s=Student()
t.work()#Teaches
d.work()#Treats patients
s.work()#Studies

#3
class Payment:
    def pay(self,amount):
        print("payment processing")
class CreditCardPayment(Payment):
    def pay(self,amount):
        print(f"{amount}rs paid through Credit Card")
class UpiPayment(Payment):
    def pay(self,amount):
        print(f"{amount}rs paid through upi")
class CashPayment(Payment):
    def pay(self,amount):
        print(f"{amount}rs paid through cash")
cash=CashPayment()
u=UpiPayment()
c=CreditCardPayment()
cash.pay(4000)
u.pay(2000)
c.pay(6000)

#4
class Employee:
    def salary(self):
        print("salary will be credited")
class Manager(Employee):
    def salary(self):
        print("Manager gets high salary")
class Developer(Employee):
    def salary(self):
        print("Developer gets minimum salary")
class Intern(Employee):
    def salary(self):
        print("Intern gets stipend")
employees = [Manager(), Developer(), Intern()]
for employee in employees:
    employee.salary()