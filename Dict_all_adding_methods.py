diction={
    "Dev": 19,
    "idris": 18,
    "Hardik" : 19,
    "Teerth" : 21,
}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic={}

# 1. making a key and assigning a value to it.
diction["het"] = 18
# output: {'Dev': 19, 'idris': 18, 'Hardik': 19, 'Teerth': 21, 'het': 18}

# 2. Update function.
diction.update({"Milind" : 18})
print(diction)
# Output: {'Dev': 19, 'idris': 18, 'Hardik': 19, 'Teerth': 21, 'het': 18, 'Milind': 18}

# Concatenate dictionary:
# Note that using .update() we can also concatenate many dictionary in one such like this:
dic1.update(dic2)
dic1.update(dic3)
print(dic1)