# In Python, functions are first class citizens. That means that, just like any other value, they can be passed as arguments to functions or assigned to variables. Here's a simple (yet not terribly useful) example to illustrate it:


def greet():
    print("Hello!")


hello = greet  # hello is another name for the greet function now.

hello()


# And, you can also pass it to a function:


# `before_and_after` is a higher-order function. That just means it's a function which has another function as a parameter.
def before_and_after(func):  # func is a function passed
    print("Before...")
    func()
    print("After...")


# greet, not greet(). That's because we're passing the function, not the result of calling the function.
before_and_after(greet)


# Let's move on to a more useful example.
# Here, you can see how we can store functions inside a dictionary—just as we could do with numbers, strings, or any other type of data.

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),  # could just be `sum`
    "top": lambda seq: max(seq),  # could just be `max`
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    print(operations[operation](grades))

# As we learn more about Python and we cover more advanced content, this will become more useful!
