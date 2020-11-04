# Let's create a greeting function

# Syntax: def name_of_function():

def greeting():
    print("welcome on board")

# if we execute this program now it would display nothing as we have not called this function

# syntax to call the function
greeting()
# this will execute code inside function

# create a new function that takes 2 arguments as ints and adds the value fo the to args

def add(num1, num2):
# creating an add function that takes 2 arguments
    print(num1 + num2)
# Displaying the sum of the args recieved

add(4, 5)

def subtract(num1, num2):
# creating a subtract function that takes 2 args
    print(num1 - num2)

subtract(3, 2)

def multiply(num1, num2):
#creating a multiply function that takes 2 args
    return num1 * num2

print(multiply(4, 3))

def divide(num1, num2):
# creating a divide function that takes 2 args
    return num1 / num2

print(divide(12, 2))

def remainder(num1, num2):
# returns the remainder when num1 is divided by num2
    return num1 % num2

print(remainder(7, 4))

# We use the return statement which is the key to python functions which means return the result of any function
