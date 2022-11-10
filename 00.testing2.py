try:
    inp = int(input("Enter age: "))
    if(inp < 18):
        raise ValueError(inp)

except ValueError:
    print("The age must be more than 18")

else:
    print("Welcome!!")