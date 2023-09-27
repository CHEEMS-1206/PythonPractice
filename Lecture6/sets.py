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

# in keyword
# no indexing or key to directly fetch elements
# add(), update() -> updation can be done from all 4 collection datatypes
# merge -> st1.union(st2)
# intersection -> st1.intersection_update(st2)
# symmetricDiff -> st1.symmetric_difference_update(st2)

# add()	                        Adds an element to the set
# clear()	                    Removes all the elements from the set
# copy()	                    Returns a copy of the set
# difference()	                Returns a set containing the difference between two or more sets
# difference_update()	        Removes the items in this set that are also included in another, specified set
# discard()         	        Remove the specified item
# intersection()	            Returns a set, that is the intersection of two other sets
# intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                Returns whether two sets have a intersection or not
# issubset()	                Returns whether another set contains this set or not
# issuperset()	                Returns whether this set contains another set or not
# pop()	                        Removes an element from the set
# remove()	                    Removes the specified element
# symmetric_difference()Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	                    Return a set containing the union of sets
# update()	                    Update the set with the union of this set and others
