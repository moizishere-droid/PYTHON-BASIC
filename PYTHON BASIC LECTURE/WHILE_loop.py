#                                       WHILE LOOP IN PYTHON

# DEFINITION --> WHEN YOU WANT TO DO SOME SAME TASK WITH UNLIMITED TIME 

# WHILE LOOP
i = 1
while(i<=5):
    print(i)
    i+=1

# BREAK KEYWORD
i = 1
while(i<=5):
    if(i==4):
        break # break the loop and come out 
    print(i)
    i+=1

# CONTIOUS KEYWORD
i = 1
while(i<=5):
    if(i==4):
        continue # skip only that iteration of the loop and cont to run 
    print(i)
    i+=1

# ELSE STATMENT
i = 1
while(i<=5):
    if(i==4):
        continue # skip only that iteration of the loop and cont to run 
    print(i)
    i+=1
else:
    print("done") # it will when the while loop condition is no longer true