# functions

# function definations
def greet():
    print("Heelo user!")

# call
greet()

# parameters and arguments and return keyword
def sum(num1,num2):
    return num1+num2

print(sum(3,5))

# conditional return

# none value

# default values for params

# multiple args -> type(args) == tuples
def sumMultiple(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sumMultiple(2,5,8,4,0,6))

# multiple key:pair items kwargs -> type(kwargs) == dict
def getKwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

getKwargs(value=3, name = "Priyanshu")