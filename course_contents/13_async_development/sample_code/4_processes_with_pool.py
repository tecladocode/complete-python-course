import time
from concurrent.futures import ProcessPoolExecutor

####### SINGLE PROCESS

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


####### TWO PROCESSES


# With two processes, we can do them both at once...
start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(complex_calculation)

print('Two process total time: ', time.time() - start)

# Run this and see what happens!

