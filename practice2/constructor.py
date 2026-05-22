#4 Employee Details
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print('id:',self.id)
        print('name:',self.name)
        print('saraly:',self.salary)
e=Employee(6609,"pavani",50000)
e.display()