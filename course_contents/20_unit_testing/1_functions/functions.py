from typing import Union, Tuple

def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError('The divisor cannot be zero.')
    
    return dividend / divisor


def multiply(*args: Tuple[Union[int, float]]):
    if len(args) == 0:
        raise ValueError('At least one value to multiply must be passed.')
    total = 1
    for arg in args:
        total *= arg
    
    return total
