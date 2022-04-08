"""
It can sometimes be handy to do something with an exception (handle it), but then not silence it.

For example, if an exception is raised in a function and you catch it:
"""


def get_user_score(user):
    try:
        perform_calculation(user.engagement_metrics)
    except ValueError:
        print("Incorrect values provided to our calculation function.")


"""
What happens is that the `ValueError` has been silenced. You caught the error, printed something out, and the program can gracefully continue running.

That’s all good, except now whoever called the function `get_user_score()` is not aware that an error happened. For example, it could re-try if it did know.

If we want, we can _not silence_ the error. In some cases it can be useful so that the caller function will also receive the error:
"""


def get_user_score(user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function.")
        raise


"""
The `raise` keyword here, used without an error class after it, just re-raises the exception that was caught in the current `except` block.
"""

"""
We can also do something when an exception *isn’t raised*. That can be useful, for example, to email to our user when the calculation succeeds:
"""


def most_engaged_user(user):
    try:
        user.score = get_user_score(user)
    except ValueError:
        print("Failed to get user score.")
    else:
        if user.score > 500:
            user.send_engagement_notification()


"""
Note that that’s different than the `finally` block, as it only runs if an exception isn’t raised. The `finally` block runs on all cases—it can also be useful in some scenarios (as we’ll see later on!).

The reading materials at the end of this section contains a few more examples of when this may be useful.
"""
