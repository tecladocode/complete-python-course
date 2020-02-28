# -*- coding: utf-8 -*-

friends = {"name":"rolf","age":24}

for key,value in friends.items():
    print(key,value)

# Dictionary is unordered
# dictionary is indexed
# keys in a dictionary are immutable and can not be repeated
# values in a dictionary can be repeated and changed


list_tuple = [("Vernika",27),("Hitesh",22),("Nithin",28)]

dictionary = dict(list_tuple)
print(dictionary)

for name, age in dictionary.items():
    name, age = name, age
    print(f"{name} is {age} years old.")
    
new_dict = dictionary.pop('Hitesh')  # pop delete the specified key and return its value
print(new_dict)

# if key not found, pop return default value if provided, otherwise raise error

dict_after_pop = dictionary.pop(5,None)
print(dict_after_pop)


print(dictionary)


nested_dict = {
        5:'Welcome',
        6:'To',
        7:'Geeks',
        'A':{1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B':{1 : 'Geeks', 2 : 'Life'}              
    }

print("initial dictionary: {}".format(nested_dict))

# Delete a key from a dictionary

del nested_dict[6]
print(nested_dict)

# if key not present in dictionary then it first try to pass default value
# otherwise throw an error
# so either use try/except or first check if key present in dict

if 7 in nested_dict:
    del nested_dict[7]
    print("updated dict: {}".format(nested_dict))
else:
    raise KeyError
    

