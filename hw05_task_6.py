# Задан целочисленный список c n случайных
# элементов. Определить количество участков списка,
# на котором элементы монотонно возрастают (каждое
# следующее число больше предыдущего).
import random

number = int(input('Number: '))
lst = []

for element in range(number):
     lst.append(random.randint(0, number - 2))

len_spisok = len(lst)
count = 0
result = 0

for j in range(len_spisok -2):

    if lst[j + 2] > lst[j + 1] > lst[j]:
        count += 1
    elif count >=1 and lst[j + 1] > lst[j + 2]:
        result += 1
        count = 0
if lst[-1] > lst[-2] > lst[-3]:
    result+=1

print(lst)
print(result)
