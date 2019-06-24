# Complete Python Course — Jose Salvatierra
# Link:

"""
We use input() to present the user with a prompt.
They can then type, and when they press Enter everything they typed gets returned.
We can assign that to a variable if we want!
"""

my_name = "Jose"
# your_name = '?'
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}.")

## Calculating months

age = input("Enter your age: ")  # Enter 3
print(
    f"You have lived for {age * 12} months."
)  # Prints You have lived for 333333333333 months.

"""
It doesn't work quite as we'd expect.

That's because we're multiplying the string '3' by 12, which concatenates the string twelve times.
Instead we want to multiply the number. We'll have to convert our string to a number first.
"""

age = input("Enter your age: ")  # Enter 3
age_num = int(age)
print(
    f"You have lived for {age_num * 12} months."
)  # Prints You have lived for 36 months.

"""
We could do it in one line, a bit more simply.
After all, `age` doesn't need to be a string at any point.
"""

age = int(input("Enter your age: "))  # Enter 3
print(f"You have lived for {age * 12} months.")  # Prints You have lived for 36 months.

"""
A better option would be to create a `months` variable, as that is cleaner to read.
"""

age = int(input("Enter your age: "))  # Enter 3
months = age * 12
print(f"You have lived for {months} months.")  # Prints You have lived for 36 months.

"""
A small exercise: calculate number of seconds lived instead of months!
"""
