# File I/O is a way to interact with files. We can read, write and manipulate files by doing this. Unlike in C, in python we don't have to make a file pointer to perform actions on a file.
# The function open() is used to open a file instead.
# It takes a filename and the mode of opening it as two arguments.
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists 

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

f=open("Ztesting_file.txt","r")
# To read the contents of the file the read() function is used.
"""print(f.read())"""
# We can also read specific parts of the file by specifying the number of characters like:
"""print(f.read(5))"""

# Note: We can only read in one print statement at a time. Because of some reason it messes with the other print statements.

# Similarly we can also read by lines by the help of readline() function.
'''
print(f.readline(),end='')
print(f.readline(),end='')
print(f.readline(),end='')
'''

# We can read through the whole file line by line by looping through it

for i in f:
    print(i)
# It is a good practice to close the file after doing file operations
f.close()