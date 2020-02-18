"""
Passing by value, reference, and assignment.

Let’s look at a couple examples of calling functions in Python.
"""

friends_last_seen = {
    'Rolf': 20,
    'Jose': 1,
    'Charlie': 9
}

def see_friend(friends, name):
    friends[name] = 0

id(friends_last_seen)
id(friends_last_seen['Rolf'])
see_friend(friends_last_seen, 'Rolf')

id(friends_last_seen['Rolf'])
id(friends_last_seen)
print(friends_last_seen)

"""
As you can see if you run that code, `friends` has the value of `friends_last_seen` when we run it—it’s the same thing exactly.

Same dictionary, same `id`.

`friends_last_seen` does not change before and after running the function, but `friends_last_seen['Rolf']` does change.

We used an `=` sign, and also `friends_last_seen['Rolf']` is an integer which is an immutable type.

If we pass an immutable type to the function though, we cannot change it. Let’s try:
"""

age = 20

def increase_age(current_age):
    current_age = current_age + 1

id(age)
increase_age(age)
id(age)

"""
I know, I know. We used an equal sign. Can we not use some `.increment()` function or something?

No… 

Integers are objects—but they don’t have such a method.

So what about this?
"""

primes = [2, 3, 5]

id(primes)

primes += [7, 11]  # We know += is 'like' primes = primes + [7, 11]...

id(primes)

"""
You get the same `id` back!!!

That’s because `+=` is not `=`.

When you do `=`, this happens:
"""

primes = primes.__add__([7, 11])

"""
When you do `+=`, this happens:
"""

primes = primes.__iadd__([7, 11])

"""
Thus, it’s all up to whether `__add__` and `__iadd__` create new objects or modify the existing objects. It’s easy to check their implementations by doing this:


>>> primes = [2, 3, 5]
>>> primes.__add__([7, 11])
[2, 3, 5, 7, 11]

>>> id(primes)
4366591880
>>> primes
[2, 3, 5]

>>> id(primes.__add__([7, 11]))
4366592456
>>> primes
[2, 3, 5]
>>> id(primes.__iadd__([7, 11]))
4366591880
>>> primes
[2, 3, 5, 7, 11]


You can see that when we did `primes.__add__`, it did not change `primes`.

But when we did `primes.__iadd__`, it did change `primes`. Interesting stuff!

---

Enough of this.

Just remember, when you pass something to a function you can mutate that thing—then the value outside the function will have changed too.


Unless it’s immutable, then it won’t have changed.
"""