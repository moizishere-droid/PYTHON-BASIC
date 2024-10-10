#                                   STRING IN PYTHON

# DEFINITION --> COLLECTION OF CHARACTER IS KNOW AS STRING
# IMMUTABLE , ORDER , DUPLICATE ALLOW

name1 = 'moiz'
name2 = "moiz"
name3 = """moiz"""
name4 = '''moiz'''

# TYPE OF THE VARIABLE
print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))

# LENGTH OF STRING
print(len(name1))

# QUOTATION INSIDE QUOTE
str1 = " 'moiz' "
str2 = """ "moiz" """
str3 = "\"moiz\""

# MULI LINE STRING
str1 = """ this is 
a multi line 
string and will print
eactly like it"""

# STRING ARE LIKE ARRAY
string = "abdul moiz"
for a in string:
    print(a)

# STRING SLICING

# abdul moiz
# 0123456789
#-10-9-8-7-6-5-4-3-2-1

print(string[0])
print(string[4])
print(string[-4])
print(string[-1])

print(string[:])
print(string[0:])
print(string[:10])
print(string[0:10])

print(string[0:10:2])
print(string[0:10:3])
print(string[::-1])

# CHECK STRING
name = "moiz is here"
if "moiz" in name:
    print("yes")
elif "moiz" not in name:
    print("no")
# or
print("moiz" is name)
print("moiz" is not name)

# STRING CONCATATION
str1 = "moiz"
str12 = "rafay"
print(str1 + str2)

# FORMAT STRING
price = 23
print(f"The price of the book is {price}")

# DOC STRING
def age():
    """this is a doc string"""
    age = 23
    print(age)
age() 

# PLACE HOLDER IN STRING
price = 334.28765456543
print(f"THE price of the book is {price:.2f}")

# ESCAPE SQUENCE
print("\'moiz\'")
print("\"moiz\"")
print("moiz\nrafay")
print("moiz\trafay")

# STRING METHODS
str1 = "moiz"
print(str.capitalize())
str2 = "MOIZ"
print(str2.casefold())
str3 = "MOIZ"
print(str3.lower())
str4 = "moiz"
print(str4.center(10))
str5 = "moiz"
print(str5.count("o"))
str6 = "moiz"
print(str6.endswith("z"))
str7 = "m\to\ti\tz"
print(str7.expandtabs(10))
str8 = "moiz"
print(str8.find("o"))
str9 = "moiz"
print(str.index("o"))
str10 = "moiz"
print(str10.isalnum())
str11 = "moiz"
print(str11.isalpha())
str12 = "moiz"
print(str12.isascii())
str13 = "moiz"
print(str13.isdecimal())
str14 = "moiz"
print(str14.isdigit())
str15 = "moiz"
print(str15.isidentifier())
str16 = "moiz"
print(str16.islower())
str17 = "moiz"
print(str17.isnumeric())
str18 = "moiz"
print(str18.isprintable())
str19 = "moiz"
print(str19.isspace())
str20 = "moiz"
print(str20.istitle())
str21 = "moiz"
print(str21.title())
str22 = "moiz"
print(str22.isupper())
str23 = "moiz rafay haseeb"
print("_".join(str23))
str24 = "moiz"
str24.maketrans("m","k")
print(str24.translate())
str25 = "moiz"
print(str25.partition("o"))
str26 = "moiz"
print(str26.replace("o"))
str27 = "moiz is here"
print(str27.split())
str28 = "moiz\n is\n here"
print(str28.splitlines())
str29 = "moiz is here"
print(str29.startswith("moiz"))
str30 = "      moiz is here       "
print(str30.strip())
str31 = "moiz is here"
print(str31.swapcase())
str32 = "moiz is here"
print(str31.upper())
str33 = "moiz"
print(str31.zfill(8))

# R METHODS
str1 = "moiz was here today"
price(str1.rfind("o"))
price(str1.rindex("o"))
price(str1.rpartition("here"))
price(str1.rstrip())
price(str1.rsplit())
price(str1.rjust())