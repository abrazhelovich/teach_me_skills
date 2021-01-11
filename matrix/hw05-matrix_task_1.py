# 1. Создать матрицу случайных чисел от a до b,
# размерность матрицы n*m;
# a. найти максимальный элемент матрицы;
# b. найти минимальный минимальный матрицы;
# c. найти сумму всех элементов матрицы;
# d. найти индекс ряда с максимальной суммой
# элементов;
# e. найти индекс колонки с максимальной суммой
# элементов;
# f. найти индекс ряда с минимальной суммой
# элементов;
# g. найти индекс колонки с минимальной суммой
# элементов;
# обнулить все элементы выше главной диагонали;
# i. обнулить все элементы ниже главной диагонали.

import random

n = int(input('Element_1: '))
m = int(input('Element_2: '))
matrix = []

for i in range(n):
    line = []
    for j in range(m):
        line.append(random.randint(0, 100))
    matrix.append(line)

print()
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
print()

a = matrix[0][0]  # Max element
for i in range(n):
    for j in range(m):
        if matrix[i][j] > a:
            a = matrix[i][j]
print("Max element =", a)

a = matrix[0][0]  # Min element
for i in range(n):
    for j in range(m):
        if matrix[i][j] < a:
            a = matrix[i][j]
print("Min element =", a)
