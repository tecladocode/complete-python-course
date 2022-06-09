"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""


def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n


g = prime_generator(100)
print(next(g))

# def prime_generator(bound):
#     for n in range(2, bound):
#         for x in range(2, n):
#             if n % x == 0:
#                 print(f'{n} equals {x} * {n // x} ')
#                 break
#         else:
#             print(f'{n} is a prime number')
g = (i for i in range(2,100)if 0 not in [i%j for j in range(2,i)])
g = (i for i in range(2,100)if all([i%j for j in range(2,i)]))