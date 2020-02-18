"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque

The main purpose of this video is to make you aware that these things exist, in case we have to use them later on (or when you encounter a situation where using one of these would be useful).

Normally what happens in those situations is we struggle to build our own thing to do what we need it to do. Knowing that these exist could save you a lot of effort!
"""

## Counter
"""
Allows us to count things. Give it a iterable or a mapping (such as a dict) and it will turn into a counter of elements.
"""

from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])  # 2

## defaultdict
"""
The `defaultdict` never raises a `KeyError`. Instead, it returns the value returned by the function specified when the object was instantiated.
"""

alma_maters = {}

for coworker in coworkers:
    if coworker[0] in alma_maters:
        alma_maters[coworker[0]] = []
    alma_maters[coworker[0]].append(coworker[1])


from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]  # Rolf got a master's

coworker_alma_maters = defaultdict(list)  # remember list is a function, returns []

for coworker, place in coworkers:
    coworker_alma_maters[coworker].append(place)

print(coworker_alma_maters['Rolf'])
print(coworker_alma_maters['Anne'])  # []

"""
When you need a dictionary and all keys of that dictionary should be associated with an initial value, use `defaultdict`!

Another example is to initialise places where coworkers work:
"""

from collections import defaultdict

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies['Jen'])  # Teclado
print(coworker_companies['Rolf'])  # Apple Inc.

"""
If you want to change the default value in a `defaultdict`, just change its `default_factory` property:
"""

from collections import defaultdict

int_dict = defaultdict(int)

int_dict['first'] += 1
print(int_dict['first'])  # 1

int_dict.default_factory = list
int_dict['second'].append('Rolf')
print(int_dict['second'])  # ['Rolf']

int_dict.default_factory = None  # this is back to being a "normal dictionary"

## OrderedDict

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 10
o['Jen'] = 3

print(o)  # keys are always in the order in which they were inserted

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)

print(o)

o.popitem()

print(o)

"""
As of Python3.7, I expected `OrderedDict` to be less useful since dictionaries themselves will retain the order in which keys are inserted.
"""

## namedtuple
"""
A namedtuple is another object that we can use like a tuple, where each of the elements of the tuple has a name. In addition, the tuple itself also has a name.

It improves on tuples by making more explicit what it means.

Take this as an example using normal tuples:
"""

account = ('checking', 1850.90)

print(account[0])  # name
print(account[1])  # balance

"""
Or, the explicitness of `namedtuple`:
"""

from collections import namedtuple

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
print(account.name)
print(account.balance)

# Or even print the account itself with a nice __repr__
print(account)

"""
I like to think of it very much like defining a class (where `Account` is the class or the type). However, remember it’s not quite the same, and a `namedtuple` is still a tuple after all.

You can do things like these:
"""

name, balance = account  # tuple destructuring

Account('checking', balance=1850.90)  # use positional or named arguments

Account._make(('checking', 1850.90))

accounts = [
    ('checking', 1850.90),
    ('savings', 3658.00),
    ('credit', -450.00)
]

account_tuples = map(Account._make, accounts)

account._asdict()  # returns an OrderedDict representing the tuple

"""
When you’re dealing with data and it doesn’t warrant creating classes for the data elements you’re working with, `namedtuple` is a great choice (and very flexible!).
"""

## Deque
"""
The last element we’ll look at today is the `deque`, which stands for “Double-ended queue”.

(Watch presentation about queues if you haven’t already).

In a `deque`, we can push elements at the start or the end, and we can also remove elements from the start or the end.

It is very efficient, performing very well, and also it’s thread-safe (we’ll be looking at threads soon!). 

When we look at asynchronous development, we’ll be talking more about the `deque` as we use it. For now, just remember it’s like a list on which you do operations like a list:
"""

from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)

"""
For more info on deques and a comprehensive example on everything you can with it, check out the official Python documentation: [8.3. collections — Container datatypes — Python 3.6.4 documentation]
"""