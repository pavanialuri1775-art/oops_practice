#Abstraction:Abstraction is the process of hiding implementation details and showing only essential functionality.
#Implemented using:
#Abstract classes
#Abstract methods
from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Circle:
    def area(self):
        print("Area of circle")
c=Circle()
c.area()

#Technical Purpose
#Reduces complexity
#Focuses on essential features
#Improves maintainability