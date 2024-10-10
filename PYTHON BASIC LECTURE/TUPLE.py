#                                   TUPLE IN PYTHON

# DEFINITION --> TUPLE IS A COLLECTION OF DATA WITH SAME OR DIFFERENT DATA TYPE 
# IMMUTABLE , ORDER , DUPLICATE ALLOW

# CRAETING TUPLE
tuple1 = (1,2,3,4,5)
tuple2 = (1,2.23,True,[1,23],(2,2,2))
print(tuple1)
print(tuple2)

# LENGTH AND TYPWE FUNCTION
print(len(tuple1))
print(type(tuple1))

# CREATE TUPLE WITH ONE VALUE
tuple3 = (23,)
print(tuple3)

# TUPLE CONSTRATUOR
tuple4 = tuple((2,3,4,5,6,7,8,9))
print(tuple4)

# ACCEXX THE TUPLE VALUES
print(tuple4[1])
print(tuple4[3])
print(tuple4[-3])
print(tuple4[-1])

print(tuple4[:])
print(tuple4[0:])
print(tuple4[:8])
print(tuple4[0:8])
print(tuple4[3:5])
print(tuple4[-2:-1])

print(tuple4[::2])
print(tuple4[::3])
print(tuple4[::-1])

# CHECK A PARTIVULAR VALUE
tuple4 = tuple((2,3,4,5,6,7,8,9))
if 2 in tuple4:
    print("yes")
else:
    print("NO") 

# UPDATE THE TUPLE BUT FIRST CONVERT INTO LIST       
tuple4 = tuple((2,3,4,5,6,7,8,9))
LIST1 = list((tuple4))
LIST1[1,3]=56
LIST1[7]=56889
tuple4 = tuple((LIST1))
print(tuple4)

# UNPACKING
tuple4 = tuple((2,3,4,5,6,7,8,9))
first , second , *third = tuple4
print(first)
print(second)
print(third) # store remaining value as a list

# LOOP THORUNG TUPLE
tuple4 = tuple((2,3,4,5,6,7,8,9))
for a in range(len(tuple4)):
    print(tuple4[a])

count = 0
while(count<=len(tuple4)):
    print(tuple4[count])
    count+=1    

# JOIN TWO TUPLE
tuple1 = (1,2,3,4,5)
tuple2 = (1,2.23,True,[1,23],(2,2,2))
tuple4_join = tuple1 + tuple2
print(tuple4_join)

# MULTIPLE TUPLE FRON ONE
tuple1 = (1,2,3,4,5)
tuple_all = tuple1 * 3
print(tuple_all)

# METHOD OF TUPLE
tuple1 = (1,2,3,4,5)
print(tuple1.count[2])
print(tuple1.index(3))