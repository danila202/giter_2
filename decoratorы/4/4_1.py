from datetime import datetime
from typing import Callable
from time import sleep
from functools import wraps


def time_it(func:Callable):
    @wraps(func)
    def inner(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        print(f'Время работы функции ${func.__name__}$ = {datetime.now() - start}')
        return res
    return inner


@time_it
def factorial(n):
    total = 1
    sleep(.2)
    for i in range(1,n+1):
        total *= i
    return total


print(factorial(20))