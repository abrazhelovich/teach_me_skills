'''Дан список целых чисел. Подсчитать сколько четных
чисел в списке'''

list_of_numbers = [1, 2, 5, 7, 44, 77, 32]
even_list = []

i = 0
while i < len(list_of_numbers):
    if (list_of_numbers[i]) % 2 == 0:
        even_list.append(list_of_numbers[i])
    i += 1

print('Count of even numbers is: ' + str(len(even_list)))
