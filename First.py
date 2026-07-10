# first code using python
print("Hello the crual world")

# python indentation
# python use indetation to indicate a block of code
if 5 > 2:
    print("Five is grater than two!")
# the number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
        print("Five is grater than two!")

# Example
x = 5
y = "Hello, world"

# example
print (3)
print (358)
print (50000)

# exmaple
print(3+4)
print(2*5)

# example
print("I am", 35, "years old.")

# veriable
# A variable is created the moment you first assign a value to it.
# Example
x = 5
y = "john"
print(x,y)
# Example
x = 4
x = "sally"
print(x)
# If you want to specify the data type of a variable, this can be done with casting.
# Example
x = str(3)
y = int(3)
z = float(3)

# for get the variable type
x = 5
y = "John"
print(type(x))
print(type(y))

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# olobal variable
x = "awesome"
def myfunc():
     print("Python is " + x)
myfunc()

# Create a variable inside a function, with the same name as the golbal variable
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
print("Python is " + x)
    
# Example global keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("python is " + x)

# 
x = "awesome"
def myfunc():
    global x
    x = "Fantastic"
myfunc()
print("Python is " + x)

# Python data type 
# Text type: str
# Numeric type:int, float, complex
# Sequence type:  list, tuple, range
# Mapping type: dict
# Set type: set, frozenset
# Boolean type: bool
# Binary type: bytes, bytearray, memoryview
# None type: NoneType


# For Example
# x = "Hello  world" str
# x = 20 int
# x = 20.5 float
# x = 1j complex
# x = ["apple","banana","cherry"] list
# x = ("apple","banana","cherry") tuple
# x = range(6) range
# x = {"name": "John" , "age" : 36} dict
# x = {"apple","banana","chery"} set
# x = frozenset({"apple","banana","cherry"}) frozenset
# x = True  bool
# x = b"Hello" bytes
# x = bytearray(5)  bytearray
# x = memoryview(bytes(5)) memoryview# x = none Nonetype

# Equal : a == b 
# Not Equals: a != b
# less than: a < b
# less than or equal to: a <= b
# greater than: a > b
# greater than or equal to: a >= b

a = 33
b = 200
if b > a:
    print("b is greater than a")
    
number = 15
if number > 0:
    print("The number is positive")
    
age = 20
if age >= 18:
        print("You are an adult")
        print("You can vote")
        print("You have full legal rights")

is_logged_in = True
if is_logged_in:
    print("welcome back")
    
# python elif
a = 33
b = 33
if b > a:
    print("b is bigger than a")
elif a == b:
    print("Number are equal")
# example  
score = 65
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
# example  
age = 25
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are and adult")
elif age >= 65:
    print("You are a seinor")
# example
day = 5
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
    
# example  of else
# The else keyword catches anything which isnt caught by the preceding conditions.
# the else statement is executed when the if condition and any elif conditons evaluate false
a = 200
b = 33
if b > a:
    print("a is not grater than b")
elif a == b:
    print("b and a are same")
else:
    print("a is greater than b")

# example
a = 200
b = 30
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
# example
number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
# example combine if else elif
temperature = 22
if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print ("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside")
    
# example
username = "Email"
if len(username) > 0:
    print(f"Welcome,{username}")
else:
    print("Error: Username cannot be empty")

# exammple one line if statement
a = 5
b = 2
if a > b: print("a is greater than b")

# short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

# asigne value with if else
a = 10
b = 30
bigger = a if a > b else b
print("Bigger is", bigger)

# Multiple condition
a = 222
b = 344
print("A") if a > b else print ("=") if a == b else print("B")

# examples
x = 15
y = 34
max_value = x if x > y else y
print("Maximum value:", max_value)

# examples
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# *****************************
# logical operator
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both condition are true")
    
# example of or operatior
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is true")
    
# example of not operator
a = 33 
b = 200
if not a > b:
    print("a is not greater than b")
    
# combining multiple operators 
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

# example
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining)or is_weekend:
    print("Great day for outdoor IsADirectoryError")

# for complec condition
temperature = 34
is_raining = False
is_weekend = True

if(temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")
    
# example
# username = "Tobias"
# password = "secrete123"
# is_verified = True
# if username and password and if_verfied:
#     print("Login successful")
# else:
#     print("Login failed")
    
# raNGE     chaking 
score = 85
if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")
    
    
# nested if statements
x = 41 
if x > 10:
    print("Abovee ten,")
if x > 20:
    print("and also above 20!")
else:
     print("but not above 20.")
    
# nested multiple condition
age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a lincense")
else:
    print("You are too young to drive")
    
#  multiple level of nestive
score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
     print("Pass but low attendance")
else:
    print("Fail")

       
=================the while loop============
i = 1
while i < 6:
    print(i)
    i += 1
============== the break statement==============
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

the continue statement============
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

the else statement==============
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer lees than 6")

=============== for loop statement==============
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    
===========Looping through a string==============
for x in "banana":
    print(x)
    
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "cherry":
        break
    print(x)

========
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
=================
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

************
for x in range(6):
    print(x)

============= INCREMENT THE RANGE OR NUMBER ================  
for x in range(2,30,3):
    print(x)
=============else in for loop
for x in range(6):
    print(x)
else:
    print("Finaly finished!")


for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finaly finshed!")


================Nested Loops=======================
adj = ["red", "big", "tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

The Pass Statement =================
for x in [0,1,2]:
    pass