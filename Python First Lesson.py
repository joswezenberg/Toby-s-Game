import math
def Circ(radius):
  diameter = radius * 2
  circumference = diameter * math.pi
  print(circumference)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = Person("Toebeans", 47)
print(p1.name)
print(p1.age)
p1.myfunc()

del p1.age
del p1



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Toebeans", "Dylias")
x.printname()


#Inheret the person class
class Student(Person):
  pass   #Prevent error for undefined class
  
p5 = Person("Toebeans", "Dylias")
p5.printname()

#-------------------------------------------------------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)			#inheret all methods and properties from its parent
    self.graduationyear = year
	
  def print(self):
    print('{0} {1} aka "{1}, {0}" will graduate at {2}.'.format(self.firstname, self.lastname, self.graduationyear))

p5 = Student("Toebeans", "Dylias", 2020)

#formatting a string
print('{1}, {0} will graduate at {2}.'.format(p5.firstname, p5.lastname, p5.graduationyear))

#How to ask the user for input
val = input("Enter your value: ")
print(val)	#prints the user's input to the terminal


x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))

#formatting a string using a pre-defined format string
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'  #defines the format string
equations = formatStr.format(x, y, x+y, x*y)	 #provides the input values, which can be evaulated within the definition
print(equations)	#prints the result to screen

#What if you actually want to display braces in a formatted string?

a = 5
b = 9
setStr = 'The set is {{{}, {}}}.'.format(a, b)
print(setStr)