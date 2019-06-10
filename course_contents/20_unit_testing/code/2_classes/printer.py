class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, pages_per_s: int, capacity: int):
        self.pages_per_s = pages_per_s
        self._capacity = capacity
    
    def print(self, pages):
        if pages > self._capacity:
            raise PrinterError('Printer does not have enough capacity for all these pages.')
        
        self._capacity -= pages

        return f'Printed {pages} pages in {pages/self.pages_per_s:.2f} seconds.'