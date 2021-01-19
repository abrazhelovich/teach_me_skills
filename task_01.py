# Создать декоратор для функции, которая принимает
# список чисел. Декоратор должен производить
# предварительную проверку данных - удалять все
# четные элементы из списка.

from typing import Union
from random import randint

def decorator_func(func: list[int]) -> list[int]:
    """This function  get only one argument as function

    Will be careated new list wich will contains odd numbers only

    Parameters
    ----------
    arg : list[int]
        A origin list of numbers

    Returns
    -------
    list[int]
        This new list with odd numbers only
    """

    def wrapper(*args, **kwargs):
        lst = func(*args, **kwargs)
        print(list(filter(lambda arg: arg % 2 != 0 , lst)))
    return(wrapper)

@decorator_func
def function(arg: list[int]) -> list[int]:
    """This function get only one argument as type 'list'

    Parameters
    ----------
    arg : list[int]
        A list of numbers which were made by randint function

    Returns
    -------
    list[int]
        A list of numbers which will send to the decorator
    """

    return arg

def main():
    list_numb = [randint(1, 30) for i in range(int(input('Please enter the number: ')))]
    print(f'Original list: {list_numb}')
    function(list_numb)

if __name__ == '__main__':
    main()
