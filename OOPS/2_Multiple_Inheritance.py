# Multiple inheritance:
# Multiple inheritance means that the child class inherits from more than one parent class
class Father:
     name="Shakir bhai"
     def occupation(self):
          print(f"The job occupation of Father is {self.job}")
          print(f"The position of Father is {self.position}")
          print(f"The  salary of father is rs{self.salary}")
     
     
class Mother:
     name="Farida ben"
     def occupation(self):
          print(f"The job occupation of Mother is {self.job}")
          print(f"The salary of Mother is rs{self.salary}")


class Child(Father,Mother):# To make a child class inherit the attributes and functions of the multiple parent classes, their names are written in the parentheses of the child class.
     name="Idris"

c=Child()
c.position="Supretendant"#
c.job="Doctor"
c.salary=100000
c.occupation()# if both the parent classes have the same functions in this case the occupation() is the same in both classes. The main inheritance will run in the child class by keeping in mind the first name of the parent class in the parentheses of the child class.

# Therefore in this case the child class will inherit the function from the Father class.
 
# If we want to make the child class inherit from the Mother class we have to make a slight change in the name of the function occupation() and then fill up the parameters such as self.job and self.salary and call the function with the instance of child class.

print(c.name)
# Output:
# The job occupation of Father is Doctor
# The position of Father is Supretendant
# The  salary of father is rs100000
# Idris