#                                   LIST IN PYTHON

# DEFINITION --> LIST IS A COLLECTION OF DATA WITH SAME OR DIFFERENT DATA TYPE
# MUTABLE , ORDER , DUPLICATE ALLOW

myList1 = [1,2,3,4]
myList2 = [1,2.34,True,[1,22],{6,7}]

# LENGTH OF LIST
print(len(myList1))
print(len(myList2))

# LIST WITH SAME AND DIFFERENT DATA TYPE
list1 = [1,23,5,7,8]
list2 = [1,2,3.44,5.32,True]
list3 = [[2,35],{"moiz":123},{23,3},(2,)]

# TYPE FUNCTION
list1 = [1,2,3,4,5,6,7]
print(type(list1))

# LIST CONSTRUCTOR
list1 = [1,2,4,6]
list1 = list((1,2,3,5))

# ACCESS LIST ITEMS
list1 = [1,2,4,6]
print(list1[0])
print(list1[2])
print(list1[4])
print(list1[-2])
print(list1[-1])

print(list1[0:5])
print(list1[0:])
print(list1[:5])
print(list1[:])
print(list1[2:3])
print(list1[:2])
print(list1[0:2])
print(list1[-4:-1])
print(list1[-1:])

print(list1[::2])
print(list1[::3])
print(list1[::-1])

# CHECK IF ITEMIS IN LIST OR NOT
list1 = [1,2,3,4,5,6,7,8,9]
if 2 in list1:
    print(":found")
else:
    print("not found") 
# or
print(2 in list1)    
print(2 not in list1)    

# CHANGE AM ITEMS
list1 = [1,2,3,5,6]
list1[0]=99
list1[0:2]=[1,2,4,5]
list1[0:3] = 2

# DEL LIST
list1 = [1,2,3,5,6]
del list1

# LOOP ON LIST
list1 = [1,2,3,5,6]
for a in list1:
    print(a)

# LOOP THROUGH INDEX RANGE
list1 = [1,2,3,5,6]
for a in range(len(list1)):
    print(list1[a])

count = 0
while(count<=len(list1)):
    print(list1[count])
    count+=1

# LIST COMPREHENSION
list1 = [1,2,4,5,7]
square = [items**2 for items in list1]
print(square)

list2 = ["apple","bananna","cherry"]
only_a = [x for x in list2 if "a" in x ]
print(only_a)

list3 = ["apple","bananna","cherry"]
upper = [x.upper() for x in list3]
print(upper)


# LIST METHODS
list1 = [1,2,3,5]
print(list1.append(11))
list2 = [1,2,3,5]
print(list2.insert(1,99))
list3 = [1,2,3,5]
print(list3.pop())
print(list3.pop(2))
list4 = [1,2,3,5]
print(list4.clear())
list5 = [1,2,3,5]
print(list5.copy())
list6 = [1,2,3,5]
print(list6.count(1))
list7 = [1,2,3,5]
print(list7.index(1))
list8 = [1,2,3,5]
list88 = [1,2,3,5]
print(list8.extend(list88))
list9 = [1,2,3,5]
print(list9.remove(1))
list11 = [1,2,3,5]
print(list11.reverse())
list10 = [1,2,3,5]
list11 = ["apple","bananna","cherry"]
list10.sort()
print(list10)
list11.sort(reverse=True)
print(list11)