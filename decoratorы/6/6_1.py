from typing import Callable
from functools import wraps
from random import randint


def parametrize_password(password:str):

    def check_password(func:Callable):

        @wraps(func)
        def inner(*args,**kwargs):
            if input_password := input('Введите пароль: ') == password:
                result = func(*args,**kwargs)
                return result
            else:
                return 'Увы(( Пароль неверный'

        return inner
    return check_password


@parametrize_password('Python2023')
def summ(*args,**kwargs):
    return sum(args)


@parametrize_password('Luchanos_top')
def get_random_number():
    return randint(1,20)


@parametrize_password('Django-TOP')
def get_link_from_vk():
    return 'https://vk.com/mocrop13'


if __name__ == "__main__":
    print("Выберите функцию с какой хотите поработать:")
    print('1 - Сумма всех веденных чисел',
          '2 - Получение рандомного числа от 1 до 20',
          '3 - Получение моей ссылки на ВК',sep='\n')

    command = input('Введите число: ')

    match command.split():
        case ['1']:
            input_numb = list(map(int,input().split()))
            print(summ(*input_numb))
        case ['2']:
            print(get_random_number())
        case ['3']:
            print(get_link_from_vk())



