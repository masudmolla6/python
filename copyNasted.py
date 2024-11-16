thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# myDict=thisdict.copy()
# myDict=dict(thisdict)
# print(myDict)

child1={
    "name":"rahim",
    "id":67
}
child2={
    "name":"kadir",
    "id":56
}
child3={
    "name":"rahul",
    "id":89
}

family={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

# print(family["child2"]["name"])

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x,object in myfamily.items():
    print(x, object)
    for y in object:
        print(y + ':', object[y])