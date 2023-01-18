# Inheritance is a way of creating a new class from an existing class.
# The existing class is called a parent class or a base class.
# And the new class is called a child class or derived class. A child class has the same attributes as its parent class and some methods of its own.
# Also the child class can overwrite the parent class's methods.

# Single Inheritance:
# The definition of single inheritance is the same as the definition of inheritance.
class Employee: # this is the base class or parent class.
     company="Google Inc."
     position="General manager"
     def details(self):
          print(f"The employee works at rs {self.salary}")

class Programmer(Employee): # this is the derived class or child class.
     company="Microsoft"
     def Details(self): 
          print(f"The programmer has mastered the programming language {self.language}")

e=Employee()
p=Programmer()
print(e.company)
print(p.position) # We are printing the position of The Employee class from the child class.
print(p.company) # Notice that the child class Programmer has overwrite the parent class in the company attribute.
p.salary=90000 # The class Programmer doesn't have any attribute named salary but it takes the attribute from the parent Employee in the function details(). thus if we are filling the salary attribute we also have to call the function details() in the child class.
p.details() # Output: The employee works at rs 90000