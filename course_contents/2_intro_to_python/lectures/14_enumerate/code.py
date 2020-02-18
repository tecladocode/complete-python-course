# https://blog.tecladocode.com/python-enumerate/

friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends, start=1):
	print(counter, friend)

# 1 Rolf
# 2 John
# 3 Anna


friends = ["Rolf", "John", "Anna"]
print(list(enumerate(friends)))  # [(0, 'Rolf'), (1, 'John'), (2, 'Anna')]
print(dict(enumerate(friends)))  # {0: 'Rolf', 1: 'John', 2: 'Anna'}
