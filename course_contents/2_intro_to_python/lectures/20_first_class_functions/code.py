# In Python, functions are first class citizens.
# That means that, just like any other value, they can be passed as arguments to functions or assigned to variables.
# Here's a simple (yet not terribly useful) example to illustrate it:


def greet():
    print("Hello!")


hello = greet  # hello is another name for the greet function now.

hello()

# Let's move on to a more useful example.

# These don't _have_ to be lambdas. They could be normal functions too!
# I'm making them lambdas because they're really short.

avg =  lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)  # could just be `sum`
top = lambda seq: max(seq)  # could just be `max`

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
    
    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(top(grades))

# Here, you can see how we can store functions inside a dictionary—just as we could do with numbers, strings, or any other type of data.
# We're creating a dictionary of what would be user input to the function that we want to run in each case.

operations = {
    "average": avg,
    "total": total,  # could just be `sum`
    "top": top,  # could just be `max`
}

# The `operations` dictionary could also be defined inline:

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),  # could just be `sum`
    "top": lambda seq: max(seq),  # could just be `max`
}

# The rest of the code can make use of the `operations` dictionary

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")
    operation_function = operations[operation]  # This means we don't need an if statement (but could get errors!)

    print(operation_function(grades))

