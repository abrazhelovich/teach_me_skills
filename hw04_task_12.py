'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого
ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце,
старый удаляется)'''

dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

keys = list(dict.keys())

for key in keys:
    new_key = f'{key}{len(key)}'
    dict[new_key] = dict.pop(key)

print(dict)
