<<<<<<< HEAD
# In Multilevel inheritance every class is inherited from the parent class before them. And only one parent class is the main.

class Parent:# This is the main class.
    name="Shiraj"
    def Description(self):# self parameter is important as it makes a connection to the later class indtance. Even if we do not print any self.variable inside the function.
        print("The Parent to child.")

class Child1(Parent):# The child class to the (Main) parent class
    name="Shakir"
    def description(self): 
        print("The parent to child 2.")
    def Status(self):
        print(f"He is {self.status}")

class Child2(Child1):# The child1 class is the child class to the Child2 parent class.
    name="boy"
    def Study_Description():
        print("Just a child.")
    def hobby(self):
        print(f"My hobby is to {self.hobby}")
# Making instances and calling the functions:
p=Parent()
c1=Child1()
c2=Child2()
c2.status="a Boy"
c2.Status()# This goes for child1
c1.description()# description of child1
c2.Description()# The case change in the description() leads to the Description() of the (Main)parent class being called.
# In the Multilevel inheritance the child class only takes the parent class's functions that is not already present in it. And if there is already a function in the class then it will be given the importance and it will be called. If the parent class and the parent of the parent class has the same function then the importance will be given to the parent class, Because it has directly inherited from it.  

# Output:
# He is a Boy
# The parent to child 2.
=======
# In Multilevel inheritance every class is inherited from the parent class before them. And only one parent class is the main.

class Parent:# This is the main class.
    name="Shiraj"
    def Description(self):# self parameter is important as it makes a connection to the later class indtance. Even if we do not print any self.variable inside the function.
        print("The Parent to child.")

class Child1(Parent):# The child class to the (Main) parent class
    name="Shakir"
    def description(self): 
        print("The parent to child 2.")
    def Status(self):
        print(f"He is {self.status}")

class Child2(Child1):# The child1 class is the child class to the Child2 parent class.
    name="boy"
    def Study_Description():
        print("Just a child.")
    def hobby(self):
        print(f"My hobby is to {self.hobby}")
# Making instances and calling the functions:
p=Parent()
c1=Child1()
c2=Child2()
c2.status="a Boy"
c2.Status()# This goes for child1
c1.description()# description of child1
c2.Description()# The case change in the description() leads to the Description() of the (Main)parent class being called.
# In the Multilevel inheritance the child class only takes the parent class's functions that is not already present in it. And if there is already a function in the class then it will be given the importance and it will be called. If the parent class and the parent of the parent class has the same function then the importance will be given to the parent class, Because it has directly inherited from it.  

# Output:
# He is a Boy
# The parent to child 2.
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
# The Parent to child.