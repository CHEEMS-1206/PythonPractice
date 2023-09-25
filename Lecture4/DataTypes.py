# Data Types

# 1. Str -> string = They can be assigned in 2 ways
# -> Literal assignment  
first = "Priyanhsu "
print(isinstance(first,str))
print(type(first))

# -> constructor assignment  
last = str("singh")
print(isinstance(last,str))
print(type(last))

# type(var) operator
# isinstance(var,dataType) operator

# Concatenation 
print(' ')
print(first+last)

#multiline = ''' nqecnejfef '''
multiline = '''
Is
  Hello 
       line1
            line2 
                 line3
'''
print(multiline)

# cast to str from int by constructor and literal method
number = 19080
print(type(number))
number = str(19080)
print(type(number))
number = "098"
print(type(number))

# Escape special chars '\', \t, \n
print('I\'m back!')

# String methods -> functions associated with str class
print(first.upper()) # upper, lower, title, replace(with,from), len, strip, lstrip, rstrip, center(len,char), ljust, rjust,startswith

# string indexing -> 0 to n-1, supports negative indexing
print(first[3])

# 2. Boolean data type
true = True
false = False
print(type(true))
print(isinstance(true, int))

# 3. Integers
price = 100
print(type(price))
print(isinstance(price, int))

# 4 Float
marks = 23.4
print(type(marks))
print(isinstance(marks, int))

# 5 complex 
imag = 2 + 3j
print(type(imag))
print(isinstance(imag, complex))
print(imag.imag,imag.real)

# mathematical methods inbuilt to python -> abs, round, ceil, floor, 
import math 