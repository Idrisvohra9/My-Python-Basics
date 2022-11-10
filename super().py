# super() is an inbuilt OOP function that allows the child class to first access the object/function of that of its parent class. So that before the execution of the function with which the super() is called the function of its parent class that is used with the super() will be called.

"""Benifits of using super(): """
# Need not remember or specify the parent class name to access its methods. This function can be used in single and multiple and Heirarchical inheritances.

# This implements modularity (isolating changes) and code reusability as there is no need to rewrite the entire function.

# Super function in Python is called dynamically because Python is a dynamic language unlike other languages.
"""It is mostly used with __init__() constructructor because it allows the characteristics of the constructructor of the base class to be used in the derived class/classes"""

class Parent:
    name="Shiraj"
    def Description(self):
        print("The Parent to child.")
    def Status(self):# 1
        print(f"Shiraj is Nice")

class Child1(Parent):
    name="Shakir"
    def Description(self): 
        print("The parent to child 2.")
    def Status(self): # 2
        super().Status() 
        print(f"Shakir is Married")

class Child2(Child1):
    name="boy"
    def Study_Description():
        print("Just a child.")
    def Status(self): # 3
        super().Status() 
        print(f"boy is Single")
        
# Making instances and calling the functions:
p=Parent()
c1=Child1()
c2=Child2()

c2.Status()

# Output:
# Shiraj is Nice
# Shakir is Married
# boy is Single