'''Дан список целых чисел.
Создать новый список, каждый элемент которого равен
исходному элементу умноженному на -2'''

list_of_int = [1, 2, 3, 4, 5]
new_list = []

#n = 0
#while n < len(list_of_int):
#    new_list.append(list_of_int[n] * -2)
#    n += 1
#print(new_list)

#i = 0
for i in list_of_int:
    print(i)
    new_list.append(i * -2)
print(new_list)
