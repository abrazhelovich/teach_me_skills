'''Дан список. Создать новый список, сдвинутый на 1
элемент влево Пример:12345 -> 23451'''

my_list = [1, 3, 4, 5, 6, 7, 8, 9, 'test']
new_list = []

i = 1
while i < len(my_list):
    new_list.append(my_list[i])
    i += 1

new_list.append(my_list[0])

print(my_list)
print(new_list)
