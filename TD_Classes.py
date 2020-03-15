class Person:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age
    self.mothers =[]
    self.fathers =[]
    self.brothers =[]
    self.sisters =[]
  def printname(self):
    print(self.firstname, self.lastname)
  def ask_brothers(self):
    print('The brothers of {0} {1} are:\n'.format(self.firstname, self.lastname))
    for brother in self.brothers:
        print('{0} {1}'.format(brother.firstname, brother.lastname))
  def add_brothers(self, brothersList):
    for new_brother in brothersList: 
      self.brothers.append(new_brother)
      new_brother.add_brother_back(self)
  def add_brother_back(self, new_brother):
    self.brothers.append(new_brother)
  def draw_family_tree(self):
    print("Hello my name is " + self.name)

#-------------------------------------------------------------------------------------------------
class Student(Person):
  def __init__(self, fname, lname, age, subject, year):
    super().__init__(fname, lname, age)			#inheret all methods and properties from its parent
    self.graduationyear = year
    self.subject = subject
  def print(self):
    print('{0} {1} aka "{1}, {0}" will graduate at {2}.'.format(self.firstname, self.lastname, self.graduationyear))

