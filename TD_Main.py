# Main appliccation document
import TD_Classes as classes
import TD_People as people

people.p1.add_brothers([people.p2]) #, people.p3
print(people.p1.brothers)
people.p1.ask_brothers()
people.p2.ask_brothers()

