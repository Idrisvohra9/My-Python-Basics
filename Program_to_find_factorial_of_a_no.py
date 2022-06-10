n=int(input("Enter a number for finding its factorial:"))
factorial=1
for x in range(1,n+1):
    factorial=factorial*x
print("The factorial of {} are {}".format(n,factorial))