for x in range(1,11):
    for y in range(1,11):
        for z in range(1,11):
            if z==10:
                print("The z loop is over now. ",end="")
            if y==10 and z==10:
                print("The y loop is over now.",end="")
            if x==10 and y==10 and z==10:
                print("The END.",end="")
            print("x={} y={} z={}".format(x,y,z))
else:
    print("Bravo soldiers!")