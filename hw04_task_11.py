'''Дан список целых чисел. Подсчитать сколько четных
чисел в списке'''

list_of_numbers = [1, 2, 5, 7, 44, 77, 32, 8]
even_list = []

counter = 0

for i in list_of_numbers:
    if i % 2 == 0:
        counter += 1

print('Count of even numbers is: ' + str(counter))
