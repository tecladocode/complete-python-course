# Complete Python Course — Jose Salvatierra
# Link:

my_string = "Hello, world!"
single_quote_string = "Hello, world!"

# Strings can use either single or double quotes. It's up to you which one you use!
# Try to pick one and stick to it throughout all your code.
# If you work with others, and they prefer a specific style, you can all agree on which to use.

string_with_quotes = "Hello, it's me."
another_with_quotes = 'He said "You are amazing!" yesterday.'

# If your string has quotation marks, make sure to use the other mark for the string itself
# Another option is to escape the quotation marks, but it is uglier and generally advised against:

escaped_quotes = 'He said "You are amazing!" yesterday.'

# Multi-line strings are useful when you have very long ones and you want to be able to write them a bit more easily.
# Multi-line strings keep the lines in the strings!

multiline = """Hello, world.

My name is Jose. Welcome to my program.
"""
print(multiline)

## String operations

# You can add strings together to concatenate them (join them together).

name = "Jose"
greeting = "Hello, " + name

print(greeting)

# You cannot add strings and numbers, as that always results in an error:

age = 34
print("You are " + age)

# But you can if you turn the number into a string first:
age = 34
age_as_string = str(34)
print("You are " + age_as_string)
