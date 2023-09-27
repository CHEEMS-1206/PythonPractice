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
#       Tuples cant be altered as well, no element can be added/removed.

# Definition
usersTuple = ('amy', 'mahika', 'genny') # can store multiple 
multiTuple = (23, True, 'true') # data with diff types
empTuple = () # empty tuple
tupleFromConst = tuple((1,2,3,4)) # creating tuple by using constructor
print(type(usersTuple),type(multiTuple),type(empTuple),type(tupleFromConst))

#   Sets - 
#       Sets are used to store multiple items in a single variable.
#       Sets are created using {} brackets
#       Sets items are unordered, unindexed, unchangeable, and donot allow duplicate values.
#       Sets can be altered
#       Sets cant be empty

# Definition
usersSet = {'amy', 'mahika', 'genny'} # can store multiple 
multiSet = {23, True, 'true'} # data with diff types
empSet = {90} # empty set
setFromConst = set({1,2,3,4}) # creating set by using constructor
print(type(usersSet),type(multiSet),type(empSet),type(setFromConst))