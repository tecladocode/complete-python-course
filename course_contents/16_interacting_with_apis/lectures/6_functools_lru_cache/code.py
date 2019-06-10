import functools
import time


@functools.lru_cache(2)
def cached_function(value):
    for i in range(value):
        i ** value


def timed():
    start = time.time()
    cached_function(4647)
    print(time.time() - start)


timed()
timed()
