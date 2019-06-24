"""
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)
"""

# While that is extremely useful when we have conditionals, sometimes we
# just want to create a dictionary out of two lists or tuples.
# That's when `zip` comes in handy!

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

# Remember how we can turn a list of lists or tuples into a dictionary?
# `zip(friends, time_since_seen)` returns something like [("Rolf", 3), ("Bob", 7)...]
# We then use `dict()` on that to get a dictionary.

friends_last_seen = dict(zip(friends, time_since_seen))
print(friends_last_seen)
