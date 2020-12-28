'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого
ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце,
старый удаляется)'''

dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
count = list(dict.keys())

i = 0
while i < len(count):
    dict[count[i] + str(len(count[i]))] = dict.pop(count[i])
    i += 1

print(dict)
