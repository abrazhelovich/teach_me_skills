# Описать функцию fact2(n), вычисляющую двойной
# факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! =
# 2·4·6·...·n, если n — четное (n > 0 — параметр целого
# типа). С помощью этой функции найти двойные
# факториалы пяти случайных целых чисел.

from random import randint
from functools import reduce


def fact(n):
    result = reduce(lambda x, y: y * x, range(n, 1, -2), 1)
    return result


def main():
    digit = int(input('Please enter the number: '))
    list_num = [randint(1, 20) for i in range(digit)]
    for n in list_num:
        print(f'{n} - {fact(n)}')


if __name__ == '__main__':
    main()
