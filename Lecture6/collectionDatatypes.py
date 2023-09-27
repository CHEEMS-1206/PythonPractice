# Python features 4 basic collection data types

# --> Lists
# --> Tuples
# --> Dicts
# --> Sets

# Lists - 
#       Lists are used to store multiple items in a single variable.
#       Lists are created using square brackets
#       List items are ordered, indexed, changeable, and allow duplicate values.

# Definition
usersList = ['amy', 'mahika', 'genny'] # can store multiple 
multiList = [23, True, 'true'] # data with diff types
empList = [] # empty list
listFromConst = list((1,2,3,4)) # creating list by using constructor
print(type(usersList),type(multiList),type(empList),type(listFromConst))

#   Tuples - 
#       Tuples are used to store multiple items in a single variable.
#       Tuples are created using () brackets
#       Tuples items are ordered, indexed, unchangeable, and allow duplicate values.

# Definition
usersTuple = ('amy', 'mahika', 'genny') # can store multiple 
multiTuple = (23, True, 'true') # data with diff types
empTuple = () # empty list
tupleFromConst = tuple((1,2,3,4)) # creating list by using constructor
print(type(usersTuple),type(multiTuple),type(empTuple),type(tupleFromConst))