from typing import Callable


def deco(func:Callable):
    def inner(*args,**kwargs):
        print('Покупайте наших котиков')
        res = func(*args,**kwargs)
        return res
    return inner


@deco
def summ(*args,**kwargs):
    return sum(args)


print(summ(1,2,3,4))
