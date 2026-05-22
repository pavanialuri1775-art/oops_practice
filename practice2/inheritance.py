#10
'''class Vehicle:
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car is 4-wheeler")
class Bike(Vehicle):
    def start(self):
        print("Bike is 2-wheeler")
vehicles=[Car(),Bike()]
for v in vehicles:
    veh.start()

#11 Person → Teacher
class Person:
    def __init__(self,name):
        self.name=name
class Teacher(Person):
    def __init__(self,name,subject,salary):
        super().__init__(name)
        self.subject=subject
        self.salary=salary
    def display(self):
        print("person name:",self.name)
        print("subject:",self.subject)
        print("salary:",self.salary)
t=Teacher("pavani","maths",50000)
t.display()'''

#Animal Sounds
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
class Cow(Animal):
    def sound(self):
        print("cow makes some sound")
animals=[Dog(),Cat(),Cow()]
for a in animals:
    a.sound()