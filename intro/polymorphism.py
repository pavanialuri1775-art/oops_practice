#Polymorphism means one interface, multiple implementations
# The same method behaves differently for different objects.
#overriding
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        pass
s=Dog()
s.sound()#Bark

#Method Overloading
#Method overloading is a feature in OOP where multiple methods have the same name but different parameters
#The method performs different operations based on the arguments passed.
#Python does not support traditional method overloading directly, but it can be achieved using default arguments.
class Calculator:
    def add(self,a,b=0,c=0):
        print(a+b+c)
obj=Calculator()
obj.add(2,3)
obj.add(2,3,4)

#In method overloading:
#Method name remains the same
#Parameters change
#Compiler/interpreter decides which version to execute based on arguments

#operator overloading
#Operators behave differently for different data types.
print(2 + 3)         # Addition
print("Hi" + "All")  # Concatenation

#Difference Between Overloading and Overriding
#Feature	     Overloading	          Overriding
#Method Name	   Same	                    Same
#Parameters	     Different	                Same
#Classes	   Usually same class	Parent & child class
#Purpose	  Multiple behaviors	Changing inherited behavior

