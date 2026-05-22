#Astraction
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("every shape  has some area")
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print(3.14*self.r*self.r)
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(self.length*self.breadth)
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print(0.5*self.base*self.height)
c=Circle(2)
r=Rectangle(4,5)
t=Triangle(2,6)
c.area()
r.area()
t.area()

#2 Online Food Delivery

from abc import ABC,abstractmethod
class FoodItem:
    @abstractmethod
    def prepare(self):
        pass
class Pizza(FoodItem):
    def prepare(self):
        print("Pizza is prepared with cheese and toppings")
class Burger(FoodItem):
    def prepare(self):
        print("Burger is prepared with buns and patty")
class Pasta(FoodItem):
    def prepare(self):
        print("Pasta is prepared with sauce and vegetables")
foods = [Pizza(), Burger(), Pasta()]
for food in foods:
    food.prepare()
   
    