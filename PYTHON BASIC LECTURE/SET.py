#                                   SETS IN PYTHON

# DEFINITION --> sET IS A COLLECTION OF DATA WITH SAME OR DIFFERENT DATA TYPE 
# IMMUTABLE --> CAN ADD OR REMOVE , UNORDER , DUPLICATE NOT ALLOW

# CREATING A SETS
set1 = {1,2,345,5}
set2 = {1,3.33,True}
print(set1)
print(set2)

# ACCESS ELEMENTS/VALES
set1 = {1,2,345,5}
# print(set1[3]) # ERROR --> INDEXING NOT ALLOW IN SETS
print(set1)

#  length and type function
print(len(set1))
print(type(set1))

# SET CONSTRUCTOR
set3 = set((1,2,3,5,6,788,67))
print(set3)

#  ACCESS THROUGHT LOOP
set3 = set((1,2,3,5,6,788,67))
for a in set3:
    print(a)
if 3 in set3:
    print("yes")
else:
    print("NO")

# MRTHOD OF SETS
set3 = set((1,2,3,5,6,788,67))
set4 = set3.add(234)
print(set4)  

set4 = set3.clear()
print(set4)
set4 = set3.copy()
print(set4)
set4 = set3.discard(1)
print(set4)
set4 = set3.pop()
print(set4)

set1 = {1,2,345,5}
set2 = {1,3.33,False}
set4 = set3.update(set1,set2)
print(set4)
set4 = set3.union(set1,set2)
print(set4)
set4 = set3.intersection(set1,set2)
print(set4)
set4 = set3.difference(set1,set2)
print(set4)
set4 = set3.isdisjoint(set1)
print(set4)
set4 = set3.issubset(set1)
print(set4)
set4 = set3.issuperset(set1)
print(set4)
set4 = set3.issuperset(set1)
print(set4)
set4 = set3.symmetric_difference(set1)
print(set4)
set4 = set3.symmetric_difference_update(set1)
print(set4)
set4 = set3.difference_update(set1)
print(set4)
set4 = set3.intersection_update(set1)
print(set4)