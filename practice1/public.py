#A protected variable is a variable that is:
#intended to be accessed within the class and its subclasses
#it is written using:_single_underscore
class  Person:
    def __init__(self):
        self._age=25
class Student(Person):
    def display(self):
        print(self._age)
s=Student()
s.display()#25

#2
class Vehicle:
    def __init__(self):
        self._speed=160
class Car(Vehicle):
    def display_speed(self):
        print(self._speed)
c=Car()
c.display_speed()#160