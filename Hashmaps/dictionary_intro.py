# Into to Dictionaries and methods
mydict = dict()
print(type(mydict))

# Insertion - no  add or insert or append method in doctionary. SO ust have to manually add
mydict["a"] = "Jagriti"
mydict["b"] = "Andrew"

# get keys
print(mydict.keys())

# Get Values
print(mydict.values())

# get items
print(mydict.items())

# to be able to access the items in the dictionary like a list
list(mydict.items())
list(mydict.items())[1][0]
list(mydict.items())[1][1]

# delete items
del mydict["a"]

print(mydict.items())

# $ python dictionary_intro.py
# <class 'dict'>
# dict_keys(['a', 'b'])
# dict_values(['Jagriti', 'Andrew'])
# dict_items([('a', 'Jagriti'), ('b', 'Andrew')])
# dict_items([('b', 'Andrew')])


# Change an item
thisdict= { "brand": "Ford", "model": "Mustang","year": 1964}
thisdict["year"] = 2018

thisdict.update({"year": 2020}) 

# check if a key is already present, as keys are unique. basically containsKey
key = "c"
list_version = list(mydict.items())
for i in range (0, len(list_version)):
    print(list_version[i])
    if list_version[i] == key:
        mydict["key"] = "Jagriti + 1"
    else:
        mydict["key"] = "New Jagriti"

print(mydict.items())

