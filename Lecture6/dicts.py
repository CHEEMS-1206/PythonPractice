#   Dicts - 
#       Dicts are used to store multiple key:value pair items in a single variable.
#       Dicts are created using {} brackets
#       Dicts items are unordered, unindexed, unchangeable, and donot allow duplicate values.
#       Dicts can be altered
#       Dicts can
#  be empty

# Definition
usersdicts = {'amy': 34, 'mahika' : 15, 'genny' : 14} # can store multiple 
multidicts = {23 : "mata", True : 5, 'true' : 90} # data with diff types
empdicts = {90:45} # empty dicts
dictsFromConst = dict({1:2,2:3,3:4,4:5}) # creating dicts by using constructor
print(type(usersdicts),type(multidicts),type(empdicts),type(dictsFromConst))

# Dictionaries - key:value pairs
video = {
    "name" : "Priyanshu",
    "age" : 12,
    "isMale" : True
}

video2 = dict(name="Priyanshu",age = 12, isMale = True)

# type() -> dict
# video["name"], video.get("age"), video.keys(), video.values(), vidoes.items()

# key exists -> "property" in dicts
# mutating values of dicts

# update({key:pair})
# pop(), popitem()

# video["newKey"] = "value" -> update

# del video["key"], video.clear(), del dict

# copy -> 
dicti = {}
newDict = dicti # creates a ref to dict
newDict2 = dicti.copy() # creates a new copy and stores
newDict3 = dict(dicti) # constructor method for new copy

# nested dictionaries

# dictionary methods
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary