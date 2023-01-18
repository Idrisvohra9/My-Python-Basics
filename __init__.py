<<<<<<< HEAD
class Employee:
     def __init__(self, name, age, salary): # __init__ is a costructor that is created when the object of the class is created. it takes the self parameter and we can add more if we want.
          self.name = name
          self.age = age
          self.salary = salary
     def GetDetails(self):
          print(f"Name of the employee: {self.name}")
          print(f"Age of the employee: {self.age}")
          print(f"Salary of the employee: {self.salary}")
          print("All the details have been filled successfully.")
idris=Employee("Idris", 17, 70000)
# idris=Employee() # <-- this throws an error because the class is missing three required parameters.
=======
class Employee:
     def __init__(self, name, age, salary): # __init__ is a costructor that is created when the object of the class is created. it takes the self parameter and we can add more if we want.
          self.name = name
          self.age = age
          self.salary = salary
     def GetDetails(self):
          print(f"Name of the employee: {self.name}")
          print(f"Age of the employee: {self.age}")
          print(f"Salary of the employee: {self.salary}")
          print("All the details have been filled successfully.")
idris=Employee("Idris", 17, 70000)
# idris=Employee() # <-- this throws an error because the class is missing three required parameters.
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
idris.GetDetails()