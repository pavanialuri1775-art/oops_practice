#1   Student Class
class Student:
   def display(self,name,marks):
        self.name=name
        self.marks=marks
        print(f'{self.name} has scored {self.marks}')
s1=Student()
s2=Student()
s3=Student()
s1.display("pavss",99)
s2.display("gee",100)
s3.display("keer",98)


#2  Rectangle
class Rectangle:
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("rectangle has area:",self.length*self.breadth)
    def perimeter(self):
        print("rectangle has perimeter:",2*(self.length+self.breadth))
r=Rectangle()
r.area(2,3)#rectangle has area: 6
r.perimeter()#rectangle has perimeter: 10

#3
class Mobile:
    def details(self,brand,price,color):
       print("Brand:",brand)
       print("Price:",price)
       print("Color:",color)
m1=Mobile()
m2=Mobile()
m3=Mobile()
m1.details("samsung",80000,"white")
m2.details("Apple",100000,"red")
m3.details("Redmi",23000,"purple")
