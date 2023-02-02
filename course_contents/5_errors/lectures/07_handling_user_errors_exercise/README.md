---
description: Review your knowledge of error handling with Python via a number of examples.
sidebar_label: "S05 L07: Handling User Errors Quiz"
---

# Handling User Errors Quiz

This lecture follows a quiz in the course that asks several questions about error handling. Let's take a moment to go over the quiz questions and their answers!

## Question 1

A quick question to warm you up!

Ben and Dan are two novice software developers. They are trying to build a function that asks user for a number and calculate its power of 2. Here is their first version of code:

```python
def power_of_two():
    n = input('Please enter a number: ')
    n_square = n ** 2
    return n_square
```

What do you think of the code, will it work? Before submitting your answer, think about why.

### Answer

The answer here is that this code will never work, because the `input()` function always returns a string, and you can't square a string.

## Question 2

In this second question, Ben and Dan improve the code slightly:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
	n = float(user_input)
    n_square = n ** 2
    return n_square
```

### Answer

Now the code will work on some inputs, but not others. That's because if the user decides to not enter a number (e.g. a letter), the program will crash.

## Question 3

Now, Ben and Dan add some error handling:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
    finally:
        n_square = n ** 2
        return n_square
```

Dan wants to test this function with some different inputs when the program asks for a number. He decides to test with two cases. First case: he enters `4`, which is a valid numeric input. Second case: he enters `'dan'` which is an invalid input.

What do you expect the function to return with Dan's input (Denoted as `[4, 'dan']`)? If the program breaks due to an error, we mark the function's return value as `Error`, and if it does not return anything, we mark the return value as `None`.

This one's a bit of a tricky one! Type the code out and try it in your editor for optimal chances of getting it right!

Potential answers:

- `[16.0, None]`
- `[Error, Error]`
- `[16.0, 0.0]`
- `[16.0, Error]`
- None of the above

### Answer

The `finally` block gets executed regardless of the occurrence of `ValueError`, so the correct answer is `[16.0, Error]`. We only defined `n` in the try block. If the input was invalid, `n` never gets its value assigned, and thus will raise an error when we try to access it in the `finally` block.

## Question 4

As Dan found the error in the code, he decided to make the following change:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        n = 0
    else:
        n_square = n ** 2
        return n_square
```

Dan wants to test with the same test cases from last time: `[4, 'dan']`.

What do you expect the function to return with the two inputs (denoted as `[4, 'dan']`) this time? If the program breaks due to an error, we mark the function's return value as `Error`, and if it does not return anything, we mark the return value as `None`.

### Answer

This one's tricky! The `else` block only gets executed if no error occurs in the `try` block. So the code will finish after assigning `n` with the default value `0` if it ever reaches the `except` block. Since there is no `return` statement other than in the `else` clause, the function returns `None`.

## Question 5

Now that Dan's code still cannot work, Ben insisted on using a finally block, here is his code:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        n = 0
    else:
        n_square = n ** 2
    finally:
        return n_square
```

They decided to use the same test cases: `[4, 'dan']`.

What do you expect the function to return with the two inputs (denoted as `[4, 'dan']`) this time? If the program breaks due to an error, we mark the function's return value as `Error`, and if it does not return anything, we mark the return value as `None`.

Potential answers:

- `[16.0, None]`
- `[Error, Error]`
- `[16.0, 0.0]`
- `[16.0, Error]`
- None of the above.

### Answer

In this case, the answer is `[16.0, Error]`. The `finally` block gets executed regardless of the occurrence of `ValueError`, while the `else` block only gets executed if no error occurs in the `try` block. However, we only defined `n_square` in the `else` block. If the input was invalid, `n_square` never gets its value assigned, thus will raise an error when we try to access it in the `finally` block.

## Question 6

Ben and Dan just won't give up, here's their last try:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
    finally:
        n_square = n ** 2
        return n_square
```

They decided to use the same test cases: `[4, 'dan']`.

What do you expect the function to return with the two inputs (denoted as `[4, 'dan']`) this time? If the program breaks due to an error, we mark the function's return value as `Error`, and if it does not return anything, we mark the return value as `None`.

Potential answers:

- `[16.0, None]`
- `[16.0, 0.0]`
- `[16.0, 0]`
- `[16.0, Error]`
- None of the above.

### Answer

The answer is `[16.0, Error]`. It's a tricky one. The `finally` block will get executed regardless of the `return` statement in both `try` block and `except` block. However, we only defined `n` in the `try` block. If the input was invalid, `n` never gets its value assigned, thus will raise an error when we try to access it in the `finally` block.

## Improvements to the code

This is the latest code that Ben and Dan wrote. As you know, it still has some issues!

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
    finally:
        n_square = n ** 2
        return n_square
```

To fix this, we need to use the `else` clause!

First, let's think about what parts of the code can raise an exception. In our case, that's converting the user input to a float.

That line is already inside the `try` block, so that's good!

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
```

Next up, let's write what should happen if there is no error:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
	else:
		n_square = n ** 2
		return n_square
```

Doing it this way is not absolutely necessary, of course, and you may like writing the `except` part first. It's up to you.

But now we've got the "happy path" of our code, or what happens if there are no errors.

So let's handle any errors that come up. In our case that's just `ValueError`, so let's add an `except` clause for that.

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
    else:
        n_square = n ** 2
        return n_square
```

So all that was needed in the end was to change the `finally` to an `else`, because there wasn't anything that we needed to run _no matter what_.

A small improvement we might do is change the `return 0` for `return 0.0`, so that the function always returns a `float`:

```python
def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0.0
    else:
        n_square = n ** 2
        return n_square
```

That way the caller of `power_of_two()` can always expect a `float` to come back, and not "sometimes a `float`, sometimes an `int`". Consistency helps!