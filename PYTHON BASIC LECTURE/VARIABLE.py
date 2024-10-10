#                                 VARIABLES IN PYTHON

# DEFINITION -->  VARABLES ARE USED TO STORE VALUE OF ANY DATATYPE

# HOW TO CREATE A VARAIBLE
# SYNTAX --> VARIABLE NAME = VALUE
var1 = 23

# HOW TO SET THE VARIABLE NAME 
# CORRECT WAY                   WRONG WAY
# var                           1var
# var_1                         var 1
# Var                           var$12
# VAR                           12
# _var                          print
# var_1                         def
# _var_1_2

# FORMAT FOR THE NAMING OF THE VARIABLE IN REAL LIFE
# PASCAL CONVERSION --> varName
# CAMEL CONVERSION --> VarName
# SNAKE CONVERSION --> var_name

# WHAT TYPE OF VALUE CAN WE STORE INTO THE VARIABLE
num1 = 23 # --> int
num2 = 23.33 # --> float
num3 = 3 + 5j # --> complex
num4 = True # --> bool
num5 = "moiz" # --> str
num6 = [2,3] # --> list
num7 = (2,3) # --> tuple
num8 = {2,3} # --> set
num9 = {"moiz":23} # --> dict 
num10 = None # --> None
num11 = range(5) # --> range

# HOW TO ASSIGN A VALUE TO A VARIBLE
age = 23
print(age)

# HOW TO CHECK A VARIABLE DATA TYPE
age = 23
print(type(age)) # --> int

# NO PARTICULAR TYPE FOR A VARIABLE
number = 2
print(type(number)) # --> int
number = "Two"
print(type(number)) # --> str

# YOU CAN CONVERT ONE DATATYPE INTO ANOTHER DATATYPE
age = 23
print(type(age)) # --> int  --> 23
age = float(23)
print(type(age)) # --> float  --> 23.0
age = str(23)
print(type(age)) # --> str --> '23'

# STRING DELACARATION
single = 'moiz'     # --> str
double = "moiz"     # --> str
triple = """moiz""" # --> str

# CASE SENSITIVE
age = 20
AGE = "twenty"
print(type(age) , age)
print(type(AGE) , AGE)

# MULTIPLE VALUES
a , b , c = 1,2,3
print(a) # --> 1
print(b) # --> 2
print(c) # --> 3

a=b=c = 3
print(a) # --> 3
print(b) # --> 3
print(c) # --> 3

# UNPACKING --> (no of varaible == no of values)
names = ["moiz","rafay","haseeb"]
a,b,c = names
print(a) # --> moiz
print(b) # --> rafay
print(c) # --> haseeb

# PRINT FUNCTION
# DEFINITION --> TO SHOW OUTPUT
print('moiz') # only in one line
print("moiz") # only in one line
print("""moiz
      is here""") # multiple line --> print exactly like you write inside 

string = "moiz"
number = 23

print(string,number) # all work --> moiz 23
print(string,string) # all work --> moiz moiz
print(number,number) # all work --> 23 23

print(string+number) # not wrok --> error
print(string+string) # work --> moizmoiz
print(number+number) # work --> ADDITION --> 46

# GLOBAL AND LOCAL VARIABLE
# DEFINITION --> VARAIBLE THAT DECLARE OUTSIDE OF THE FUNCTION --> GLOBAL
# DEFINITION --> VARAIBLE THAT DECLARE INSIDE OF THE FUNCTION --> LOCAL

# 1
name = "moiz"
def info():
    age = 23
    print(name)
    print(age)
info() # --> moiz 23

# 2
name = "moiz"
def info():
    age = 23
print(name) # moiz
print(age) # error --> not defined 

# 3
name = "moiz"
def info():
    name = "rafay"
    print(name)
info() # rafay
print(name) # moiz

# 4
name = "moiz"
def info():
    global name
    name = "rafay"
    print(name)
info() # rafay
print(name) # rafay

# 5
name = "moiz"
def info():
    global age
    age = 23
print(name) # moiz
print(age) # 23