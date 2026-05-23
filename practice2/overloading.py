#
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(200)
b2=Book(300)
print(b1+b2)

#2 Student Marks Comparison
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
s1=Student("pavani",95)
s2=Student("geetha",98)
if s1>s2:
    print('student 1 has more marks')
else:
    print('student 2 has more marks')