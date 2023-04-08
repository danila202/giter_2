from typing import Callable


class InvalidTarget(Exception):
    """Вызывается когда получено неверное значение"""
    pass


def deco(func:Callable):
    def inner(*args,**kwargs):
        attempt = 10
        while attempt > 0:
            if func(*args,**kwargs) == 10:
                res = func(*args,**kwargs)
                return res
            else:
                print(f'Функция отработала неверно. Количество ошибок = {attempt} ')
                attempt -= 1
        else:
            raise InvalidTarget('Неверное итоговое значение')

    return inner


def target_summ_10(*args,**kwargs) -> int:
    if sum(args) == 10:
        result = sum(args)
        return result


res = deco(target_summ_10)
print(res(1,2,3))
