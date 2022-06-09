# Define a PrimeGenerator class
class PrimeGen:
    x: int

    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop  # stop defines the range (exclusive upper bound) in which we search for the primes
        self.numbers = list(range(2, self.stop))

    def __next__(self):
        if len(self.numbers) == 0:
            raise StopIteration
        prime = self.numbers[0]
        self.numbers = [x for x in self.numbers if x % prime != 0]
        return prime


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop  # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.start = n + 1
                return n


g = PrimeGenerator(100)
for i in range(10):
    print(next(g))

g = PrimeGenerator(100)

for i in range(9):
    print(next(g))

