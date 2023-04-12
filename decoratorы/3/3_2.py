from typing import Callable
from datetime import timedelta
from datetime import datetime
from time import sleep


def cached_deco(func:Callable):
    memory = {}

    def inner(*args,**kwargs):
        time_saving = datetime.now()
        if not args[0] in memory:
            result = func(*args,**kwargs)
            memory[args[0]] = (args[0],time_saving)
            return f'Новое значение {result}'
        else:
            if timedelta(seconds=10) + memory.get(args[0])[1] >= datetime.now():
                return f'Берём из кэша {memory.get(args[0])[0]}'
            result = func(*args, **kwargs)
            memory[args[0]] = args[0]
            return f'Обновляем значение в кэше {result}'

    return inner


@cached_deco
def cache(value:int):
    cache_memory = dict()
    cache_memory[value] = value
    return cache_memory[value]


if __name__ == "__main__":
    print(cache(1))
    print(cache(12))
    sleep(9)
    print(cache(1))
    print(cache(3))






