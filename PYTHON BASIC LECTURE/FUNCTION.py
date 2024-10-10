#                               FUNCTION IN PYTHON

# DEFINITION --> A BLOCK OF CODE WHICH ONLY RUN WHEN YOU CALLED --> RETURN DATA AS A RESULT

# CREATING A FUNCTION
def add(a,b):
    print(f" The sum is equal to: {a+b}")

# CALLING A FUNCTION
add(2,3)    
add(3,3)    
add(4,3)    
add(5,3)    
add(6,3)

# PARAMETER AND ARGUMENT --> values must be in order 
def full_name(fname,lname): # fname,lname --> parameter
    print(f"The full name is: {fname} {lname} ")
full_name("abdul","moiz") # abdul,moiz --> argument

# ARBITRAY ARGUMENT --> *ARGS
# WHEN YOU DONOT KNOW HOW MANY ARGUMENT YOU HAVE TO PASS
def full_name(*kids):
    print(f"The full name is: {kids}") # --> return the values in the form of tuple
full_name("abdul","moiz","rafay","wahab","anas")

# KEYWORD ARGUMENT --> value not need to be in order
def full_name(lname,fname): 
    print(f"The full name is: {fname} {lname} ")
full_name(fname="abdul",lname="moiz")

# DEFAULT ARGUMENT
def full_name(fname,lname="moiz"): 
    print(f"The full name is: {fname} {lname} ") # abdul moiz
full_name(fname="abdul")

def full_name(fname,lname="moiz"): 
    print(f"The full name is: {fname} {lname} ") # abdul rafay
full_name(fname="abdul",lname="rafay")

# RETURN VALUES
def add(a,b):
    return (f" The sum is equal to: {a+b}")
result = add(2,3)
print(result)

def add(a,b):
    if (a+b>5):
        return True
    else:
        return False
result = add(2,4)
if result:
    print("yes")
else:
    print("no")                