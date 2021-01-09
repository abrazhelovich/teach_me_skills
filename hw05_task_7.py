# Дана целочисленная квадратная матрица размерности
# n. Заполнить ее случайными целыми числами. Найти в
# каждой строке наибольший элемент и поменять его
# местами с элементом главной диагонали.
import random

n = int(input('Number: '))
matrix = []

for i in range(n):
    line = []
    for j in range(n):
        line.append(random.randint(0, 100))
    matrix.append(line)

print('Original matrix:')
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
print()

k = 0
for row in matrix:
    max_num = max(row)
    max_idx = row.index(max_num)
    print(f'Max value of {k + 1} list is {max_num} -> Index {max_idx}')
    row[k], row[max_idx] = row[max_idx], row[k]
    k += 1
print()

print('New matrix:')
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
