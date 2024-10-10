#                               TYPE CASTING IN PYTHON

# DEFINITION --> CONVERT ONE DATATYPE INTO ANOTHER DATATYPE

# INT --> FLOAT , STR ,COMPLEX
age = 23
age = float(age)
age = str(age)
age = complex(age)

# FLOAT --> INT , STR ,COMPLEX
age = 23.34
age = int(age)
age = str(age)
age = complex(age)

# STR --> INT , FLOAT ,COMPLEX
age = "23"
age = int(age)
age = float(age)
age = complex(age)

# LIST --> TUPLE,SET
list1 = [2,4,5,6,7]
num = tuple(list1)
num = set(list1)

# TUPLE --> LIST,SET
tuple1 = (2,4,5,6,7)
num = list(tuple1)
num = set(tuple1)

# SET --> LIST,TUPLE
set1 = {2,4,5,6,7}
num = list(set1)
num = tuple(set1)

# LIST,TUPLE.SET --> DICT
first = [(1,3),(4,2)] 
second = ((1,3),(4,2)) 
third = {(1,3),(4,3)} 
num1 = dict(first)
num2 = dict(second)
num3 = dict(third)

# DICT --> LIST,TUPLE.SET
first = {"moiz":2, "rafay":3}
num1 = list(first)
num2 = tuple(first)
num3 = set(first)
print(num1) # only covert the item not value    
print(num2) # only covert the item not value 
print(num3) # only covert the item not value 

num1 = list(first.items())
num2 = tuple(first.items())
num3 = set(first.items())
print(num1) # convert the items as   
print(num2) # convert the items as
print(num3) # convert the items as
