#1   Student Class
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f'{self.name} has scored {self.marks}')
s1=Student("pavss",98)
s2=Student("gee",99)
s3=Student("keer",100)
s1.display()#pavss has scored 98
s2.display()#gee has scored 99
s3.display()#keer has scored 100


#2  Rectangle
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("rectangle has area:",self.length*self.breadth)
    def perimeter(self):
        print("rectangle has perimeter:",2*(self.length+self.breadth))
r=Rectangle(2,3)
r.area()#rectangle has area: 6
r.perimeter()#rectangle has perimeter: 10

#3
class Mobile:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color
    def details(self):
       print(f"Brand: {self.brand}")
       print(f"Price: {self.price}")
       print(f"Color: {self.color}")
m1=Mobile("samsung",80000,"white")
m2=Mobile("Apple",100000,"red")
m3=Mobile("Redmi",23000,"purple")
m1.details()
m2.details()
m3.details()
