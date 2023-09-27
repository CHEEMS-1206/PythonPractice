# Lists - 
#       Lists are used to store multiple items in a single variable.
#       Lists are created using square brackets
#       List items are ordered, indexed, changeable, and allow duplicate values.

# Definition
users = ['amy', 'mahika', 'genny'] # can store multiple 
multiList = [23, True, 'true'] # data with diff types
empList = [] # empty list
listFromConst = list((1,2,3,4)) # creating list by using constructor

# --> List Methods 
# append()	Adds an element at the end of the list
# append(), concatenate, extend() -> adding 2 or more lists together

# len()     return length of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list, --> sort(key=str.lower), sort(reverse=True)
# type()    list
# del list  deletes entire list
# sorted(list,options) -> print sorted list without actually overwriting the entire list

# index()	Returns the index of the first element with the specified value
print(multiList.index(23))

# insert()	Adds an element at the specified position --> insert(pos, element)
# [val:val] -> insert, [val:val+n] -> replace

# in keyword
print(23 in multiList) # print true/false

# list indexing in python: positive from 0, negative indexing from -1
print(multiList[0],multiList[-1])

# range of elements from a list [0:2]
n = 2
print(multiList[0:n]) # prints from 0 till n-1