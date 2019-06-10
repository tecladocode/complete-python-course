division_with_remainder = 12 // 5  # should be 2.4
print(division_with_remainder)  # prints 2

# 5 goes into 12 two times. (5 * 2 is 10). The remainder is 2.
# Getting the remainder of a division is such a popular operation, that Python gives us a way to do it really easily.

remainder = 12 % 5
print(remainder)  # prints 2

# Why is it so popular?
# What would the remainder be in these divisions?
#
# 10 / 2
# 14 / 2
# 6 / 2
# 340 / 2
#
# What about these?
#
# 11 / 2
# 27 / 2
# 3 / 2

# For every even number, the remainder when divided by 2 is always 0.
# For every odd number, the remainder when divided by 2 is always 1.

# We can check whether a number is odd or even just by checking the remainder!

x = 37
remainder = x % 2
print(remainder)  # should print 1, therefore it is odd

# We'll look at doing things depending on whether a number is odd or even soon in the course!
