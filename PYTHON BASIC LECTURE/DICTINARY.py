#                               DICTINARY IN PYTHON

# DEFINITION --> DICTINARY IS A COLLECTION OF DATA WITH SAME OR DIFFERENT DATA TYPE along with its key
# MUTABLE , ORDER , DUPLICATE NOT ALLOW

# CREATING DICTINARY
dict1 = {"moiz":23,"true":1}
print(dict1)

# LENGTH AND TYPE FUNCTION 
print(len(dict1))
print(type(dict1))

# DICT CONSTRUCTOR
dict2 = dict((("moiz",23),("rafay",False)))
print(dict2)

# CHECK IF EXIST OR NOT
dict2 = dict((("moiz",23),("rafay",False)))
if "moiz" in dict2:
    print("yes")
else:
    print("no") 

# CHANGE THE VALUE
dict2["moiz"]= "haseeb"
print(dict2)
dict2["ANAS"]= 2345
print(dict2)
del dict2["rafay"]
print(dict2)

# LOOP THROGH DICTINARY
for x,y in dict2.items():
    print(x,y)
for x in dict2:
    print(x)
for x in dict2.values():
    print(x)
for x in dict2.keys():
    print(x)

# # NESTED DICTIONATU
# dict1 = {"moiz":23,"true":1}
dict2 = dict((("moiz",23),("rafay",False)))
# dict3 = {"dict1": dict1,"dict2":dict2}

# METHOD OF DICTINARY
dict1 = {"moiz":23,"true":1,"False":0}
dict1.clear()
print(dict1)
dict1.pop("moiz")
print(dict1)
dict1.popitem()
print(dict1)
dictt3 = dict1.copy()
print(dictt3)
result = dict1.get("moiz")
print(result)
result = dict1.values()
print(result)
result = dict1.items()
print(result)
result = dict1.keys()
print(result)
dict1.update(dict2)
print(dict1)
x = ("moiz","rafay","haseeb")
y = "one value to each"
thisdict = dict1.fromkeys(x,y)
print(thisdict)
result = dict1.setdefault("moiz",34)
print(result)