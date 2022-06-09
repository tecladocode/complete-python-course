import time
import random
from threading import Thread

counter = 0


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New counter value: {counter}')
    time.sleep(random.random())
    print('-----------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
