# operator overloading means giving the operator extended meaning beyond their pre-defined operational meaning.
# For example the '+' operator can be used to add int data type , str data type and Even list can be added together because it's functionality is already in-built. When we use "+" operator the magic method __add__ is automatically invoked.
# The double underscore methods that are also called dunder methods are used to do operator overloading and these methods are also called magic methods.
# Code Showing operator overloading:

class Num:
    def __init__(self,n1):
        self.n1 = n1
    
    def __add__(self,n2):
        self.n2 = n2
        print("Add magic method under loading")
        return self.n1 + n2.n1 # By commenting the return statement out it will print the above print statement.

n1= Num(10)
n2= Num(20)
n1+n2 # Output will be The print statement WHY?
# because the class Num got the 2 necessary variables in order to work the second variable goes to the __add__ method That causes the print statement  to be executed.
# Now to get the output to be sensible we do this:
sum=n1+n2
print(sum)
# Note the print statement will always be executed whenever the 2nd variable goes to the __add__ method. because we have coded it there.