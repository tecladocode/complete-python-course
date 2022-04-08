"""
We’ve looked at dictionaries as able to represent what _something_ is. For example, this dictionary represents a student:
"""

my_student = {"name": "Rolf Smith", "grades": [70, 88, 90, 99]}

"""
If we want to calculate the average grade of the student, we could create a function to do so:
"""


def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])


"""
However, there is a flaw with this. This function is separate and unrelated from the student (e.g. in a professional program, they could even be in different files), but it depends on the student variable having a particular structure:

* The `student` must be a dictionary; and
* There must be a `grades` key that must be a list or tuple, so that we can use `sum()` and `len()` on them.

It would be great if we could have something inside our dictionary that would return the average grade. That means the function would live in the same place as the data, and then it’s easier to see whether the data we require has changed or not.

Something /like/ this:
"""


my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99],
    "average": 0,  # something here to calculate
}

"""
It would be fantastic if we could do this, and naturally the `'average'` would have to change when then `'grades` changes. It must be a function.

*There’s no way to do this in a dictionary*.

Sorry!

We must use objects for this. We can begin by thinking of objects as things that can store both data and functions that relate to that data.

Here’s that (incorrect) dictionary in object format:
"""


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


"""
Scary syntax! Don’t worry—what it does is close to the same.

When you have that class, you can create objects using it. Let’s do that first and then explain exactly what is happening:
"""

student_one = Student("Rolf Smith", [70, 88, 90, 99])
student_two = Student("Jose", [50, 60, 99, 100])

"""
To create a new object, we use the class name as if it were a function call: `Student()`.

Inside the brackets, we put arguments that will map to the `__init__` method in the `Student` class.

`Student('Rolf Smith', [70, 88, 90, 99])` maps to `__init__(self, new_name, new_grades)`.

What you end up with is a /thing/ that has two properties, `name` and `grades`.
"""

print(student_one.name)
print(student_two.name)

"""
Inside the `__init__` method, we use `self.name` and `self.grades`. `self` is the current object, so when we assign values we modify only the “current object”.
"""

Student("Rolf Smith", [70, 88, 90, 99])

# def __init__(self, new_name, grades):
#  self.name = new_name
#  self.grades = new_grades

"""
When you do this, `self` is the new object you are creating. You can assign it to a variable:
"""

student_one = Student("Rolf Smith", [70, 88, 90, 99])

"""
As you do that more, every object is a different `self`,  with differently assigned properties depending on what you passed to the `Student()` /constructor/ call.
"""

## Properties

"""
Cool, so now we have the objects, both of which have different properties:
"""

student_one = Student("Rolf Smith", [70, 88, 90, 99])
student_two = Student("Jose", [50, 60, 99, 100])

"""
These are _similar_ to our dictionaries, in that the dictionaries also store values:
"""

d_student_one = {"name": "Rolf Smith", "grades": [70, 88, 90, 99]}
d_student_two = {"name": "Jose", "grades": [50, 60, 99, 100]}

"""
To access them:

```
student_one.name
student_one.grades

student_two.name
student_two.grades

d_student_one['name']
d_student_one['grades']

d_student_two['name']
d_student_two['grades']
```
"""

## Methods

"""
> A method is a function which lives in a class.

The `average()` method in the Student () class also has access to `self`, the current object. When we call the method:
"""

print(student_one.average())

"""
What is really happening in the background is:
"""

print(Student.average(student_one))

"""
As you can see, `student_one` is passed as the first argument (and that is what `self` is in the method definition):
"""


def average(self):
    return sum(self.grades) / len(self.grades)


"""
So again, because `self` is `student_one`, `self.grades` is `student_one.grades`.

Thus:

* The sum of `self.grades` is the sum of `[70, 88, 90, 99]`: 347.
* The length of `self.grades` is 4.

The result will be `86.75`.
"""

## Recap

"""
Just to recap, the class is very similar to the dictionary but it allows us to include methods as well that have access to the properties of the object we created.

Classes also gives us a bunch more functionality, we’ll look at that in the coming videos!
"""
