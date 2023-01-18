<<<<<<< HEAD
# The try, exept and else are blocks of code normally used for error finding and reporting a defined error message when there is an error found.
# Try statements must have atleast one except or finally claus.
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement
# In this following example the variable 'x' is being printed out without being declared. 
try:
    print(x)

except NameError:
    print("The variable 'x' is not defined.")

except:
    print("An error occurred.")

# Else claus is executed when no errors are found:
y=20
try:
    print(y)

except:
    print("An error has occurred.")

else:
    print("No errors found.")

# If no errors are found then print statement executes by default becuase the try statement has returned False because no errors occurred.

# The finally block, if specified, will be executed regardless if the try block raises an error or not.

z="Idris"
try:
    print(z)

except:
    print("An error has occured.")

finally:
=======
# The try, exept and else are blocks of code normally used for error finding and reporting a defined error message when there is an error found.
# Try statements must have atleast one except or finally claus.
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement
# In this following example the variable 'x' is being printed out without being declared. 
try:
    print(x)

except NameError:
    print("The variable 'x' is not defined.")

except:
    print("An error occurred.")

# Else claus is executed when no errors are found:
y=20
try:
    print(y)

except:
    print("An error has occurred.")

else:
    print("No errors found.")

# If no errors are found then print statement executes by default becuase the try statement has returned False because no errors occurred.

# The finally block, if specified, will be executed regardless if the try block raises an error or not.

z="Idris"
try:
    print(z)

except:
    print("An error has occured.")

finally:
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
    print("Finally out of here..")