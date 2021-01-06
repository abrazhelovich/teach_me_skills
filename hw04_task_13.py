'''Дан список. Создать новый список, сдвинутый на 1
элемент влево Пример:12345 -> 23451'''

my_list = [3, 4, 5, 6, 7, 8, 9]
new_list = []

for i in my_list[1:]:
    new_list.append(i)
new_list.append(my_list[0])

print(new_list)
