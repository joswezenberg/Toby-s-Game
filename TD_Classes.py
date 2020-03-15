class Person:
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age
    self.parents =[]
    self.siblings =[]
    self.children =[]
  def printname(self):
    print(self.firstname, self.lastname)
  def ask_siblings(self):
    print('The siblings of {0} {1} are: '.format(self.firstname, self.lastname))
    for sibling in self.siblings:
        print('{0} {1}'.format(sibling.firstname, sibling.lastname))
  def add_siblings(self, siblingsList):
    for new_sibling in siblingsList: 
      self.siblings.append(new_sibling)
      new_sibling.siblings.append(self)
  def ask_parents(self):
    print('The parents of {0} {1} are: '.format(self.firstname, self.lastname))
    for parent in self.parents:
        print('{0} {1}'.format(parent.firstname, parent.lastname))
  def add_parents(self, parentsList):
    for new_parent in parentsList: 
      self.parents.append(new_parent)
      new_parent.children(self)
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

