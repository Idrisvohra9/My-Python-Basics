# @property decorator is used to make a function inside a class and act like a property that changes frequently. Rather than a class attribute that we have to change manually every time.
import os
os.system("cls")
class Calculator:
    var1= 300
    var2= 400
    # sum= 700 # this is a Hardcoded avlue and it becomes useless when there is a change in the value of any of the variables. For making this a function that by changing the value of any of the variable it shows its sum and also becomes a property that can be printed, rather than a function that is called inside a print statement we use @property decorator.
    @property # The @property decorator is called @getter method
    def Sum(self):
        return self.var1 + self.var2
    # Now if we made the Sum function a property that means that we can also change it. so to change the sum function such that it sets the avlues of var1 & var2 according to the equation (sum=var1+var2) we have to use a @setter decorator.

    @Sum.setter # The format of the @setter decorator is @property_fun_name".setter"
    def Sum(self, sum): # it takes 2 parameters with the self parameter the second one should be the @property value.  
        self.var1= sum - self.var2
        

c= Calculator()
print("Using property decorator for the Sum function:",c.Sum) # 700
# So the @property decorator makes a function act like a property.
c.Sum=900
print("Getting property value to:",c.Sum) # 900
print("Setting the var1 value to:",c.var1) # 500
print("Setting the var2 value to:",c.var2) # 400
print(c.var1,"+",c.var2,"=",c.Sum) 