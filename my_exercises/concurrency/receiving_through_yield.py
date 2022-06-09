# def greet():
#     friend = yield
#     print(f'Hello, {friend}')
#
#
# g = greet()
# g.send(None) # priming the generator
# g.send('Adam')

from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jan', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)
