# В списке целых случайных чисел с количеством
# элементов n определить максимальное число и
# заменить им все четные по значению элементы.
import random

number = int(input('Number: '))
lst_number = []

for element in range(number):
    lst_number.append(random.randint(0, number))

max_num = max(lst_number)

for n, step in enumerate(lst_number):
    if step % 2 == 0:
        lst_number[n] = max_num

print('MAX: ' + str(max_num), end='\n\n')
print(lst_number)
