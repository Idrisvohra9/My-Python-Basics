# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# Appending New content in the file and also reading it after:
"""
f=open("Ztesting_file.txt","a")
f.write("\nNew Content")
f=open("Ztesting_file.txt","r")
print(f.read())

f.close()
# """
# To overwrite existing content "w" mode is used:
f=open("Ztesting.txt","w")
f.write("Woops i deleted all the content but take this text instead.")
f=open("Ztesting.txt","r")
print(f.read())
