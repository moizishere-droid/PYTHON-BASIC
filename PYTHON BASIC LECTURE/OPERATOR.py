#                                       OPERATOR IN PYTHON

# ARITHEMTICS OPERATOR
print(2+3)  # add
print(2-3)  # sub
print(2*3)  # mul
print(2/3)  # div
print(2**3) # power
print(2%3)  # mod
print(2//3) # floor

# COMPARISION OPERATOR
print(2==3) # equal equal to 
print(2!=3) # not equal to
print(2<3)  # graeter than
print(2>3)  # less than
print(2<=3) # graeter and equal to
print(2>=3) # less and equal to

# ASSIGMENT OPERATOR
age = 23
print(age)
age+=2  
print(age)
age-=2 
print(age)
age*=2 
print(age)
age/=2 
print(age)
age**=2
print(age)
age//=2
print(age)
age%=2
print(age)

# LOGICAL OPERATOR
age =23
name = "mois"
if(age==23 and name=="moiz"):
    print("both are correct")
elif(age ==23 or name=="rafay"):
    print("one is correct")
elif(not(age ==23)):
    print("correct convert to wrong and vice versa")

# IDENTITY OPERATOR
one =23
two =23
print(one is two) # TRUE
print(one is not two) # FALSE

# MEBERSHIP OPERATOR
one =23
two =23
print(one in two) # TRUE
print(one not in two) # FALSE

# OPERATOR PRECEDENCE
# ()
# **
# * / // %
# + -
# == != >= <= < > is isnot in notin
# not
# and 
# or