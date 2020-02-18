"""
As well as the `datetime` module, used to deal with objects containing both date and time, we have a `date` module and a `time` module.

Whenever you’re running some code, you can measure the start time and end time to calculate the total amount of time it took for the code to run.

It’s really straightforward:
"""

import time

def powers(limit):
    return [x**2 for x in range(limit)]

start = time.time()
p = powers(5000000)
end = time.time()

print(end - start)

"""
You could of course turn this into a function:
"""

import time

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(500000))

"""
Notice how the `measure_runtime` call passes a lambda function since the `measure_runtime` function does not allow us to pass arguments to the `func()` call.

This is a workaround to some other technique that we’ll look at very soon.

By the way, the `measure_runtime` function here is a higher-order function; and the `powers` function is a first-class function.


If you want to time execution of small code snippets, you can also look into the `timeit` module, designed for just that: [27.5. timeit — Measure execution time of small code snippets — Python 3.6.4 documentation](https://docs.python.org/3/library/timeit.html)
"""

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("map(lambda x: x**2, range(10))"))

"""
This runs the statement a default of 10,000 times to check how long it runs for. Notice how `map()` is faster than list comprehension!
"""