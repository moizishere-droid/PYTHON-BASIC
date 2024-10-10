#                                   BOOLEAN IN PYTHON

# DEFINITION --> GIVE TRUE/FALSE BASED ON THE CONDITION OR VALUE --> HELP TO RUM SPECIFIED TASK

# FIST WAY
age= 34
if(age>0):
    print("yes")
else:
    print("no")

# SECOND WAY
def age():
    age = 23
    if(age>0):
        return True
    else:
        return False
if (age):
    print("yes")
else:
    print("no")        

# WHEN GIVE TRUE      AND        WHEN GIVE FALSE
# bool(2.3)                      bool(0)
# bool(True)                     bool(None)
# bool(1)                        bool(false)
# bool(2)                        bool("")
# bool([2,3,5])                  bool([])
# bool((2,3,5))                  bool(())
# bool({2,3,5})                  bool({})

# ISINSTANCE OF FIUNCTION
age = 24
name = "moiz"
print(isinstance(age,int)) # True
print(isinstance(age,int)) # False