#                                   CONDITIONAL STATEMENT AND MATCH CASE

# DEFINITION --> TAKE DECISION ON THE BASIC OF THEIR CONDITION , IF CONDITION IS TRUE THAN 
#                SPECIFIED CODE WILL RUN OR IF FALSE THAN SPECIFIED CODE WILL RUN

# IF-ELSE STATEMENT
age = 20
if(age>=18):
    print("yes")
else:
    print("no") 

# IF-ELIF-ELSE STATEMENT
day = "thursday"
if(day=="monday"):
    print(1)
elif(day=="tuesday"):
    print(2)
elif(day=="wednesday"):
    print(3)
elif(day=="thursday"):
    print(4)
elif(day=="friday"):
    print(5)
elif(day=="saturaday"):
    print(6)
elif(day=="sunday"):
    print(7)
else:
    print("invalid")    

# SHORTHAND IF STATEMENT
a,b=2,3
if a>b:print("a is greater than b")

# SHORTHAND IF-ELSE STATEMENT
a,b=2,3
print("a is greater than b") if a>b else("b is graeter than a")

# IF-ELSE STATEMENT WITH LOGICAL OPERATOR
age,country = 20,"pakistan"
if(age>=18 and country=="pakistan"):
    print("yes")
elif(age>=18 or country=="india"):
    print("you also can") 
elif(not(age>=18)):
    print("yes")
else:
    print("invalid")  

# NESTED IF ELSE
age = 20
country="pakistan" 
gender ="male"
if(age>=18):
    if(country=="pakistan"):
        if(gender=="male"):
            print("yes")
        else:
            print("female")    
    else:
        print("Not belong to pakistan") 
else:
    print("under 18") 

# MATCH CASE
month = "jul"
match month:
    case "jan": print(1)
    case "feb": print(2)
    case "mar": print(3)
    case "apr": print(4)
    case "may": print(5)
    case "jun": print(6)
    case "jul": print(7)
    case _: print("invalid")