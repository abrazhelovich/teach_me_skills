# Создать список поездов. Структура словаря: номер
# поезда, пункт и время прибытия, пункт и время
# отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20
# минут. (Примечание: использовать возможности
# библиотеки datetime).

from datetime import datetime

lst = [
    {
        'train_code': '88',
        'from': 'Minsk',
        'to': 'Brest',
        'departure': datetime(2021, 1, 14, 10, 15),
        'arrival': datetime(2021, 1, 14, 18, 44)
    },
    {
        'train_code': '34',
        'from': 'Minsk',
        'to': 'Vilnus',
        'departure': datetime(2021, 1, 15, 12, 24),
        'arrival': datetime(2021, 1, 15, 14, 25)
    },
    {
        'train_code': '95',
        'from': 'Piter',
        'to': 'Moscow',
        'departure': datetime(2021, 1, 13, 12, 55),
        'arrival': datetime(2021, 1, 15, 21, 17)
    },
    {
        'train_code': '100',
        'from': 'Moscow',
        'to': 'Kiev',
        'departure': datetime(2021, 1, 16, 10, 00),
        'arrival': datetime(2021, 1, 18, 20, 23)
    }]

for i in lst:
    delta = 7 * 3600 + 20 * 60
    diff = (i['arrival'] - i['departure']).seconds
    if diff > delta:
         print(i)
