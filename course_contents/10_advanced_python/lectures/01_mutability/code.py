"""
What are mutable and immutable objects?

An important concept in programming, and particularly in Python, is the concept of mutability. Some things in Python are mutable and some things are immutable.

“What is mutable?” I hear you say…

A mutable datum is one that you can change after it has been created. An immutable datum is one you cannot change.

Here’s an example of a mutable datum:
"""

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

"""
How do you know it’s mutable?

Whenever you create a new dictionary, it is actually stored physically in your computer’s RAM—a type of memory that only lives while the computer is on and your app running.

Python can give you the `id` of the object, which is the address of the object in memory. That’s precisely the first cell of the group of cells in the RAM in which your object is stored.
"""

print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

"""
Notice how even though the dictionaries have the same values, their `id` values are different. New dictionaries were created each time, and hence their memory addresses are different.

The memory address depends on what memory was available at the time of creation, so it won’t be the same for any two objects which exist at the same time.

However, if we do this:
"""

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen['Anne'] = 20

print(id(friends_last_seen))

"""
We can see that the `id` did not change, even though we changed a value in that dictionary.

The dictionary was mutated. 🎉

There are only a few immutable things in Python:

* integers
* floats
* strings
* tuples

That’s pretty much it. All the other types are mutable.

Here’s why numbers are immutable:
"""

age = 20
print(id(age))

"""
You cannot change the 20. 20 is always 20.

You can change what `age` points to:
"""

age = 30
print(id(age))

"""
But then the `id` also changes—it is now an entirely new integer.

It is the same with strings:
"""

greeting = 'hello'
print(id(greeting))

greeting = 'byebye'
print(id(greeting))

greeting = greeting + 'a'
print(id(greeting))

"""
Tuples are also immutable because you cannot change the tuple itself:
"""

my_tuple = (3, 5, 10)
print(id(my_tuple))

my_tuple = (3, 5)
print(id(my_tuple))

"""
Lists however, are mutable. Once you have a list, you can add or remove elements from it. That does not create a new list object, it modifies it.
"""

friends = ['Rolf', 'Jose']
print(id(friends))

friends.append('Jen')
print(id(friends))

"""
Generally you can look at it like this: when you use `=`, you are likely creating a new thing—with a new `id`.

When you call a function, such as `append` or `__setitem__` (that’s the function that gets called when you do `my_dict[‘Rolf’]`), you’re likely mutating the object.
"""