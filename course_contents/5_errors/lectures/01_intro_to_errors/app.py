"""
Nobody likes errors. However, they can be extremely helpful if they appear when we want them to!

Let’s say we do something like the below:
"""

print(my_variable)

"""
We’ll quickly get a NameError. That’s a built-in error type in Python that suggests we used a name (in this case, `my_variable`) that didn’t exist. It’s great to receive that error, because once you know what it means you can easily find the source of the problem.

It would be much worse if you just got an `Error`—it may take you hours (or days) to find a simple error in a larger application.

The name of the error is very useful. But even more useful is the *stack trace*, which tells you which files the error touched. Here’s a sample stack trace from an error I saw earlier on:

Traceback (most recent call last):
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 53, in <module>
    menu()
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 10, in menu
    show_movies()
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 36, in show_movies
    show_movie_details(movie)
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 40, in show_movie_details
    print(f"Name: {movies['name']}")
TypeError: list indices must be integers or slices, not str

This error is a `TypeError`, which means we used the wrong type of data for our operation (in this case, we tried to access a list as if it were a dictionary).

It’s really important that you get familiar with the most common errors you’ll see, so that as they appear in your programs you can quickly identify what went wrong.

It’s also very important to start reading the stack traces and understanding what’s going on. Frequently the stack trace will tell you:

1. At the very bottom it gives you the error that was raised and a description.
2. What line of *your* code raised the error;
3. What function that line is in;
4. What function called the function that the line is in;
5. And so on… until you reach the file that you executed.

As you go through the stack trace, it’s possible you’ll see some files and code that you didn’t write. This will happen if you use other modules and libraries (we’ll look at this later on!). If you see that, don’t worry! It’s unlikely those libraries will be the source of the error.

In many cases, the error won’t tell you everything you need to know in order to fix the problem. In that case, you’ll have to do some research:

1. Look at your code!
2. Put the error and message into Google, see if something comes up in StackOverflow.
3. Look at the code you’ve written again, this time more slowly, and run through it as if you were a computer. Do you notice anything that could potentially be a source of the error?
4. Run only some parts of the code in isolation, that’ll help identify which part of your code is giving you an error.
5. Use a debugger (we’ll learn how in the next couple videos).
6. And of course, ask questions in the Course Q&A. We’re here to help!
"""
