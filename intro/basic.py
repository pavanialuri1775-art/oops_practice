#OOPS
#Object-Oriented Programming (OOP) is mainly built on:
#Classes & Objects
#A class is a blueprint.
#An object is the real thing created from the blueprint.

#p1
class Car:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print("Brand:",self.brand)
c1=Car("BMW")#BMW
c1.display()

#When object is created init constructor runs automatically
class Student:
    def __init__(self,name):
        self.name=name
s=Student("Pavani")
print(s.name)#Pavani

#self keyword
#self refers to the current object
class Mobile:
    def show(self):
        print("Hello") 
m=Mobile
m.show()
