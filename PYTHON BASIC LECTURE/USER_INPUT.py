#                               USER INPUT IN PYTHON

# INPUT FROM USER
name = input("Enter your name: ") # --> ITS DEFAULT DATA TYPE IS (STR)
print(type(name)) # str


# INPUT FROM USER THE AGE AND CONVERT INTO INT
age = int(input("Enter your age: ")) 
print(type(age)) # int


# INPUT FROM USER THE SALARY AND CONVERT INTO FLOAT
salary = float(input("Enter your salary: ")) 
print(type(salary)) # float

# YOU CAN ALSO TAKE TWO INPUT AT A TIME --> FIRST NAME AND LAST NAME PURPOSE
info= input("Enter your name first and than age: ")
name = info.split()[0]
age = info.split()[1]
print(name , age)