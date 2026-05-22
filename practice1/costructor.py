#
class Person:
    def __init__(self,name):
        self.name=name
        print("Person Constructor")#Person Constructor
class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.rollno=roll_no
        print("student constructor")#Student Constructor
s=Student("Pavani",6609)

#2
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
d=Dog()
d.sound()
