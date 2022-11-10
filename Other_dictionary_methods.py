contacts={
    "Ambulance" : 108,
    "Police station" : 100,
    "Fire station" : 101
}
# .fromkeys():
x=("key1","key2","key3","key4")
y={}
n=1
while n<4:
    n+=1
mydict={}
mydict=y.fromkeys(x,n)
print(mydict)