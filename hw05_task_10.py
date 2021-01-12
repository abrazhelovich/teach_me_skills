# Создать список поездов. Структура словаря: номер
# поезда, пункт и время прибытия, пункт и время
# отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20
# минут. (Примечание: использовать возможности
# библиотеки datetime).
import datetime
from datetime import time

lst = [{'train_code': '887B', 'station': 'Minsk', 'time_arrive': time(12, 00), 'time_departure': time(5, 40)},
       {'train_code': '411C', 'station': 'Borisov', 'time_arrive': time(11, 15), 'time_departure': time(7, 10)},
       {'train_code': '743L', 'station': 'Brest', 'time_arrive': time(8, 45), 'time_departure': time(1, 25)},
       {'train_code': '113F', 'station': 'Orsha', 'time_arrive': time(13, 30), 'time_departure': time(11, 10)}]

for i in lst:
    print(i['time_departure'])
    #print(datetime.time(i['time_arrive']))
