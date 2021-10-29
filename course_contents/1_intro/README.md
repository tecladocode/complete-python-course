# 01. Python Basic Data Types

### Variables
- A variable is a name associated with a value.
- A variable can be named anything, but it has some rules:
    1. It cannot start with an integer
    2. It cannot contain spaces
    3. It can only contain a symbol, which is the underscore

Examples of variable names:

- Correct:

```
response
top500
one_apple
first_numbers
_usernames
_last_
current_
```


- Incorrect:

```
top 500
one apple
1st_numbers
^last_
$current
response#
```

**Extra resources**

- [What are variables?](https://python.tecladocode.com/1_age_program/2_variables.html#what-are-variables)

### Strings
A string is a sequence of characters surrounded by quotation marks:
Single quotes `''` or Double quotes `""`


- Anything surrounded by the quotation marks indicate a string
- Every opening quote must have a closing quote to form a string
- If opening a string with a single quote, the closing quote must be a single quote as well

Examples:

- Correct:

```python
"This is a sample string using double quotes"
'This is a sample string using single quotes'
'This is a normal string'
'50 + 51'
```

- Incorrect:

```python
'This string will end here.' From here the continuation is not a string'
'This is an Incorrect string"
"Same as this one'
```

**Extra resources**
- [Strings and numbers](https://python.tecladocode.com/1_age_program/1_strings_numbers.html)
- [String formatting](https://python.tecladocode.com/1_age_program/4_string_formatting.html#what-is-string-formatting)
- [Strings, Variables, and Getting Input from Users](https://www.teclado.com/30-days-of-python/python-30-day-2-strings-variables)
- [Formatting Strings and Processing User Input](https://www.teclado.com/30-days-of-python/python-30-day-3-string-formatting)
- [Formatting Numbers for Printing in Python](https://blog.teclado.com/python-formatting-numbers-for-printing/)
- [Nested String Interpolation in Python](https://blog.teclado.com/python-nested-string-interpolation/)

### Integers
An integer is a whole number of any length that can be positive or negative, written without a fractional element.

Example:

`-1` `0` `1` `2` `3` `86400`


### Floats
A float is a number that can be positive or negative written with a fractional element.

Example:

`-100.54` `1.0` `59.1` `10.99`

**Extra resources**
- [Numbers, Arithmetic, and Printing to the Console](https://www.teclado.com/30-days-of-python/python-30-day-1-numbers-printing)

### Booleans
In Python booleans are a bool data type having two values:

```python
True
False
```

**Extra resources**
- [Conditionals and Booleans](https://www.teclado.com/30-days-of-python/python-30-day-5-conditionals-booleans)

### Lists

- A list is an ordered sequential data type
- A list is used to store multiple elements in one place
- A list is created by a pair of square brackets

```python
shopping_list = ['cereals', 'milk', 'cherries']
midterm_grades = [4, 9, 6, 6]
```

- A list can contain different data types

`phone_numbers = ['james', 8067366796]`

- Each element in a list holds a position (index) through which it can be accessed

```python
shopping_list[0]  # cereals
shopping_list[1]  # milk
shopping_list[2]  # cherries
```

**Extra resources**
- [What is a list?](https://python.tecladocode.com/2_countries_visited/1_lists.html)
- [Split, join, and slices](https://www.teclado.com/30-days-of-python/python-30-day-7-split-join)
- [Extending Python Lists](https://blog.teclado.com/python-extending-lists/)

### Tuples
- A tuple is very much like a list, however:
  - A tuple is an ordered sequential data type which is **immutable**
- A tuple is created by a sequence of elements separated by a comma
- For better readability, it can be surrounded by parenthesis

Example:

```python
shopping_list = 'apples', 'milk', 'cherries'
midterm_grades = 4, 9, 6, 6
phone_numbers = 'james', 8067366796
better_readability = ('with', 'parenthesis')
```

**Extra resources**
- [Basic Python Collections](https://www.teclado.com/30-days-of-python/python-30-day-4-lists-tuples)

### Sets
- A set is an **unordered** data type
- Elements of a set cannot be accessed by their indices
- A set is created by a single pair of curly brackets:

`shopping_list = {'apples', 'milk', 'cherries'}`

**Extra resources**
- [Sets](https://www.teclado.com/30-days-of-python/python-30-day-11-sets)
- [Python Set Operators](https://blog.teclado.com/python-set-operators/)

### Dictionaries
- A dictionary is created by 3 key components:
curly braces, keys and values
- The keys must be a string
- The values can be any other data type

Example:

```python
employees = {'ID': 16915, 'name': 'James', 'department': ['Sales', 'Accounting']}
```

```python
employees = {
  'ID': 16915,
  'name': 'James',
  'department': ['Sales', 'Accounting']
}
```

- A dictionary is accessed by keys as such:
`employees['name']  # 'James'`

**Extra resources**
- [What is a dictionary?](https://python.tecladocode.com/2_countries_visited/1_lists.html)
- [Updating Python Dictionaries](https://blog.teclado.com/python-updating-dictionaries/)

# 02. Python Arithmetic Operators

## Addition `+`

Correct uses:

- The use with integers and floats:

`44 + 19.5  # 63.5`

- The use with strings (concatenation):

`"My name is " + "James"`

Incorrect uses:

- Between strings and integers/floats:

```python
"The correct number is" + 5
# TypeError: can only concatenate str (not "int") to str
```

## Subtraction `-`

- The use between integers/floats:

`93.1 - 50`

- The use between sets (return elements of set_1 that aren't in set_2):

```python
set_1 = {3, 6, 9, 7, 5}
set_2 = {3, 6, 9, 95}

set_difference = set_1 - set_2  # {5, 7}
```

## Multiplication `*`

- The arithmetic use:

`8 * 5`

- Multiplying data types:

```python
"Hello " * 2  # Hello Hello
[100] * 2  # [100, 100]
(100, 1) * 2  # (100, 1, 100, 1)
```


## True Division `/`
- The two operands will always result in a float using the `/` operator

Example:

`30.5 / 2` will result `15.5`

## Floor Division `//`
- Will always round the amount to the closest tenth

Example:
`30.5 // 2`  will result `15.0`

## Modulo `%`

- It's based on the Euclidean division ([learn more](https://blog.teclado.com/pythons-modulo-operator-and-floor-division/))
- Start with a **dividend** and a **divisor**
- It's used to get the remainder between the two operands

Example:

The result for `10 % 3` is `1`.


## Exponentiation `**`
`2 ** 3` Can be read as: 2 raised to the power of 3, same as `2 * 2 * 2`.


## Extra resources
- [How do mathematics work in Python?](https://python.tecladocode.com/1_age_program/1_strings_numbers.html#how-do-mathematics-work-in-python)
- [Python's modulo operator and floor division](https://blog.teclado.com/pythons-modulo-operator-and-floor-division/)
- [Python's divmod Function](https://blog.teclado.com/pythons-divmod-function/)

# 03. Python Comparison Operators

Each comparison operator returns True or False
### Equal `==`

```python
4 == 4  # True
4 == 5 # False
```

- Can be used to check the truth value of an operand:

```python
4 is True  #  True
4 is False  # False
0 is False  # True
```

- Can be used to compare two strings or any other data type:

```python
"Hello" == "Hello"  # True
"Hello" == "HELLO"  # False
(100, 50) == 50  # False
(100, 50) == (500, 219)  # False
```

### Not equal `!=`
- The opposite of `==`

```python
4 != 4  # False
4 != 5  # True
```

### Greater than `>`
`10 > 10  # False`

### Less than `<`
- Opposite of higher than
`10 < 10  # False`

### Greater than or equal to `>=`
`10 >= 10  # True`

### Less than or equal to `<=`
`10 <= 10  # True`

### Extra resources
- [Conditionals and Booleans](https://www.teclado.com/30-days-of-python/python-30-day-5-conditionals-booleans)

# 04. Python Assignment Operators

| Operator | Example    |
| -------  | ---------- |
| `=`      | `var = 2`  |
| `+=`     | `var += 2` |
| `-=`     | `var -= 2` |
| `*=`     | `var *= 2` |
| `**=`    | `var **= 2`|
| `/=`     | `var /= 2` |
| `//=`    | `var //= 2`|
| `%=`     | `var %= 2` |


# 05. Python Logical Operators

## AND
- `and` returns the first value if it evaluates to false, otherwise it returns the second value.

Example:

| Statement         | Result     |
| -------------     | ---------- |
| `True and True`   | `True`     |
| `True and False`  | `False`    |
| `False and False` | `False`    |
| `False and True`  | `False`    |


## OR
- `or` returns the first value if it evaluates to true, otherwise it returns the second value.

Example:

| Statement         | Result     |
| -------------     | ---------- |
| `True or True`    | `True`     |
| `True or False`   | `True`     |
| `False or False`  | `False`    |
| `False or True`   | `True`     |

## NOT
- `not` returns True if the operand is False

Example:

| Statement         | Result     |
| -------------     | ---------- |
| `not True`        | `False`    |
| `not False`       | `True`     |


### Extra resources
- [Logical comparisons in Python: and & or](https://blog.teclado.com/logical-comparisons-in-python-and-or/)


# 06. Python Identity Operators

## IS
- Return True if the operands have the same identity

Example:

```python
users = ['James', 'Charlie', 'Ana']
print(id(users))  # 2425142160952

users_copy = users
print(id(users_copy))  # 2425142160952

print(users_copy is users)  # True

users_copy = ['James', 'Charlie', 'Ana']
print(id(users_copy))  # 2425142558551

print(users_copy is users)  # False
```

## IS NOT
- Returns True if the operands don't have the same identity

Example:

```python
users = ['James', 'Charlie', 'Ana']
print(id(users))  # 2425142160952

users_copy = users
print(id(users_copy))  # 2425142160952

print(users_copy is users)  # False

users_copy = ['James', 'Charlie', 'Ana']
print(id(users_copy))  # 2425142558551

print(users_copy is users)  # True
```


# 07. Python Membership Operators

## IN
- Returns True if an element exists inside an object

Example:
```python
users = ['James', 'Charlie', 'Ana']
print("Johnny" in users)  # False
```

## NOT IN
- Returns True if an element does not exist inside an object

Example:
```python
users = ['James', 'Charlie', 'Ana']
print("Johnny" not in users)  # True
```

