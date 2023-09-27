#   Tuples - 
#       Tuples are used to store multiple items in a single variable.
#       Tuples are created using () brackets
#       Tuples items are ordered, indexed, unchangeable, and allow duplicate values.
#       To work on tuples we can create a list using list constructor, make changes on the new list and later redefine the tuple with this list

# Definition
usersTuple = ('amy', 'mahika', 'genny') # can store multiple 
multiTuple = (23, True, 'true') # data with diff types
empTuple = () # empty list
tupleFromConst = tuple((1,2,3,4)) # creating list by using constructor
print(type(usersTuple),type(multiTuple),type(empTuple),type(tupleFromConst))

# unpacking - getting value in a var from tuple
tupleOfFruits = ("apple")
(apple) = tupleOfFruits
print(apple,tupleOfFruits)