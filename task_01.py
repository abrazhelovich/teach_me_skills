# Описать функцию fact2(n), вычисляющую двойной
# факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! =
# 2·4·6·...·n, если n — четное (n > 0 — параметр целого
# типа). С помощью этой функции найти двойные
# факториалы пяти случайных целых чисел.

from random import randint
from functools import reduce

def main():
    digit = int(input('Please enter the number: '))
    list_num = [randint(1, 10) for i in range(digit)]
    print(list_num)
    for n in list_num:
            result = reduce(lambda x, y: y * x, range(n,1,-2), 1)
            print(n, result)

if __name__ == '__main__':
     main()
