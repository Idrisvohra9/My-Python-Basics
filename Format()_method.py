#The format() method takes the passed arguments, formats them, and places them in the string
#where the placeholders {} are:
x="Teri"
X="maa"
y="Ka"
Y="saki"
z="naka."
txt="{} {} {} {} {}"
A=txt.format(x,X,y,Y,z)
print(A)
#output-Teri maa ka saki naka.
#Array method
x="Teri"
X="maa"
y="Ka"
Y="saki"
z="naka."
txt="{0} {1} {2} {3} {4}"
B=txt.format(x,X,y,Y,z)
print(B)
print(len(B))
C="Length of this"
print(C)
print(len(C))
