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

# golbal variable
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