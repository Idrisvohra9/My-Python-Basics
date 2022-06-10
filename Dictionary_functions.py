my_dictionary={"id":1234,"name":"parthiv","rno":25,"pno":841524152,"email":"parthiv@5210gmail.com"}

print(len(my_dictionary))

print(my_dictionary.keys())   

print(my_dictionary.values())

print(my_dictionary.get("id")) #helps us to know value of that key

print(my_dictionary.items()) #print all key-value pairs in dictionary

info=my_dictionary.items()
for a in info:
    print(a)  #print seperately key-value pairs in new line

for a,b in info:
    print(a,b)  #print without brackets and commas
    
a=dict.fromkeys([1,5,89,"name",5],(10,"patel"))    # 1st bracket will act as key and 2nd bracket will act as values
print(a)                                           #2nd brackets values are assigned one by one to all 1st bracket keys 

marks1={"cpp":98,"rtc":72,}
marks1.setdefault("foa",89) #if we add key throgh setdefault it can't be modify
print(marks1)
marks2={"bdos":75,"cpp":73}
marks1.update(marks2) #it merges two dictionary if one key is same in two dictionary then new dict value is replaced to original dict
print(marks1)
a.clear()
print(a) # it delets whole key-value pair but not delete dict it gives empty dict
my_dictionary.pop("rno") #in pop we give specific key to delete it
print(my_dictionary)
print(my_dictionary.pop("aadhar","not here")) #if we give no error if key is not exist in dict we also write  message for it
my_dictionary.popitem() #removes the last item from the dictionary
print(my_dictionary)
a=sorted(my_dictionary) #it sorts the key value in assending order
print(a)
a=sorted(my_dictionary,reverse=True)  #it reverse the key values
print(a)
dict1={2:"vraj",1:"vrajendra",3:"abhay"}
dict2={"id":12,"num":632654102}
b=sorted(dict1.values()) # we sort values if values are same type ex-int,str
print(b)                  # mixing of int and str gives error
b=sorted(dict2.values())
print(b)
b=sorted(dict1.items()) #it gives us sorted items
print(b)
print(min(dict1)) #it gives us minimum number or alphabet
print(max(dict1)) #it gives us maximum number or alphabet
print(sum(dict1)) #it gives us sum of keys
