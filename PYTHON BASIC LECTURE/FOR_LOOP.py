#                                       FOR LOOP IN PYTHON

# DEFINITION --> WHEN YOU WANT TO DO SOME SAME TASK WITH LIMITED TIME 

# FOR LOOP

string = "abdul moiz"
for a in string:
    print(a)

for a in range(len(string)):
    print(a)    

list1 = ["moiz","rafay","haseeb","wahab"]
for a in list1:
    print(a)

# BREAK AND CONTIOUS STATMENT
for a in range(11):
    if(a==5):
        break
    else:
        print(a)

for a in range(11):
    if(a==5):
        continue
    else:
        print(a)

# RANGE FUNCTION WITH LOOP
for a in range(11):
    print(a)
    
for a in range(1,11):
    print(a)

for a in range(1,11,2):
    print(a)

# ELSE WITH LOOP
for a in range(1,11,2):
    print(a)
else:
    print("done") # i will not run if the loop is stopped by break keywork

# NESTED FOR LOOP
for a in range(6):
    for b in range(6):
        print(a,"-->",b)    
