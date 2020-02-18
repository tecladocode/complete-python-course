"""
Let’s look at how we can extract patterns from text using regular expressions in Python with the `re` module.
"""

import re

email = 'jose@tecladocode.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'

"""
Of course, a better way of extracting the name and domain could be:
"""

import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

"""
Or indeed:
"""

email = 'jose@tecladocode.com'
print(email.split('@'))  # lol

"""
Let’s say you’ve got a price of an item in a strange format (e.g. extracted from a file):
"""

import re

price = 'Price: $189.50'
expression = 'Price: \$(\d+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets

"""
Indeed if you can potentially have commas in your number:
"""

import re

price = 'Price: $11,489.50'
expression = 'Price: \$([\d,]+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets

"""
Then you could turn the string matched into a proper Python float:
"""

num = '11,489.50'

num = num.replace(',', '')  # replace ',' for ''
print(float(num))

"""
I would really recommend taking the time to look through regexr and the official Python documentation for `re` module, as it is really quite good:

* https://docs.python.org/3/library/re.html
* http://regexr.com
"""