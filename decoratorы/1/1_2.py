from typing import Callable


def deco_param(text:str):

    def deco(func:Callable):

        def inner(*args,**kwargs):
            print(text)
            result = func(*args,**kwargs)
            return result
        return inner
    return deco


@deco_param('I love basketball')
def summ(*args,**kwargs):
    return sum(args)


print(summ(1,2,3))
