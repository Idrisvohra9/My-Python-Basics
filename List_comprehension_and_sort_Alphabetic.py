Animals=["Lion","Tiger","Deer","Zebra","Wolf","Leopard"]
print([x for x in Animals if "e" in x])#output=["Tiger","Deer","Zebra","Wolf","Leopard"]

print([x for x in Animals if "e" not in x])#output["Lion","Wolf"]

print([x for x in Animals if "Deer" != x])#output=["Lion","Tiger","Zebra","Wolf","Leopard"]

print([x for x in Animals if "Zebra" != x])#output=["Lion","Tiger","Deer","Wolf","Leopard"]

print([x.upper() for x in Animals])#Output=["LION","TIGER","DEER","ZEBRA","WOLF","LEOPARD"]

Animals.sort()
print(Animals)#output=["Deer","Leopard","Lion","Tiger","Wolf","Zebra"]

Animals.sort(reverse=True)
print(Animals)#output=["Zebra","Wolf","Tiger","Lion","Leopard","Deer"]
