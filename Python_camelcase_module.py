import camelcase as cc
cc=cc.CamelCase()
# print(text.hump("hello my name is idris and i wish to be the best of the best."))
text=input("Enter some text to convert it into camelcase:")

print(cc.hump(text))