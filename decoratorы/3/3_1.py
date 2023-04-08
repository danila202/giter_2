from typing import Callable, Any


def cached_true(func:Callable) -> Any:
    cache_memory = {}

    def inner(*args,**kwargs):
        if args[0] not in cache_memory:
            print(f'{args[0]} Нет в кэше, добавляем')
            result = func(*args,**kwargs)
            cache_memory[args[0]] = args[0]
            return result
        else:
            print(f'{args[0]} берём из кэша так как она была уже подсчитана')
            return cache_memory[args[0]]
    return inner


@cached_true
def cache(value:int):
    cache_memory = dict()
    cache_memory[value] = value
    return cache_memory[value]


if __name__ == "__main__":
    cache(3)
    cache(5)
    cache(4)
    cache(3)


