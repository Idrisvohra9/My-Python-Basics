# Class is a template more like while filling up a form and making it into a proper application.
# class itself doesn't hold space in the memory. only when it is called or instantiated that it allocates memory.

# An object is an instantiation of class

# class example 1:
class Number:
    def sum(self):
        return self.a + self.b

n=Number() # This is the instance to the class Number.
n.a=15
n.b=25
s=n.sum()
print(s)

# class example 2:
class College_Form:
    def FillInfo(self):
        print(f"Name: {self.name}") # Note that we are using f before the string in the print statement that is called f string what it does is makes it viable to use variable names in the print statement.
        print(f"Address: {self.address}")
        print(f"State: {self.state}") 
        print(f"Country: {self.country}")
        print(f"Country code: {self.country_code}")
        print(f"Number: {self.number}")

application=College_Form()
application.name="Idris vohra"
application.address="Relief rd. near zakariya masjid"
application.state="Gujarat"
application.country="India"
application.country_code="+91"
application.number="9106930717"
application.FillInfo()

# Attribute of class:
class Employee:
    company="Google"# This is an attribute.
    salary=100
    def department(self):# self refers to the instance of the class
        # self.dept="ISRO" # <-- This is the hardcoded attribute
        print(f"The department is {self.dept} and the salary is {self.salary}")
idris=Employee()
# print(idris.company)
# Output: Google
# **to change the attribute of class we have to use the class name and not the instance**
Employee.company="Yahoo"
print(idris.company)

# Attribute of instance:
idris.salary="900 $" # There is a variable salary inside the class Employee but the instance attribute salary overwrites the original variable salary in the class.
# ^ If this is commented out the compiler will give importance to the variable salary in the class.  
print(idris.salary)
# Output: 900

# self parameter:
# Employee.dept="NASA"
idris.dept="Google"
idris.department()
# Employee.department(idris) # It can also be typed as this<--
# What i learned: if you hard code an attribute inside a function inside a class that attribute is given the most importance. after that the importance is given to object attribute and atlast the class attribute is given the importance.
# So the compiler checks 1. Attribute inside the function, 2. object attribute, 3. class attribute.
# Special note: Functions and methods are the same, objects and instance are the same and variable and attributes are the same.