#Inheritance
#Inheritance means:
#A child class gets properties and methods from parent class.
#syntax
class Parent:
    pass
class Child(Parent):
    pass

#Types of Inheritance
#single inheritance
#single parent-single child
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    pass
d=Dog()
d.sound()#Animal sound

#Dog inherited sound() from Animal.

#Multilevel Inheritance
#grandparent-parent-child
class Grandparent:
    pass
class Parent(Grandparent):
    pass
class Child(Parent):
    pass

#Multiple Inheritance
#Multiple parents-single child
class Father:
    def skills(self):
        print("Driving")
class Mother:
    def talent(self):
        print("cooking")
class Child(Father,Mother):
    pass
c=Child()
c.talent()
c.skills()

