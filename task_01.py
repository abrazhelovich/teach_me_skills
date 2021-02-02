# Написать программу таймер. Программа при запуске
# принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя
# оставшееся время. Программа должна хранить файл
# логирования с информацией о том кто запускал
# программу и когда.
# Пример :
# 00:00:03
# 00:00:02
# 00:00:01
# ALARM!!!

from time import sleep
from datetime import datetime
import time as my_time
import csv
import argparse
from typing import Generator

def Timer(f_name: str, l_name: str, val_sec: int) -> Generator:
    with open('log.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([f_name + ' ' + l_name, datetime.now().strftime('%d-%m-%Y %H:%M:%S')])
    while val_sec > 0:
        sleep(1)
        f_time = my_time.strftime("%H:%M:%S", my_time.gmtime(val_sec - 1))
        val_sec -= 1
        yield f_time
    yield 'ALARM!!!'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first_name', required=True)
    parser.add_argument('-ln', '--last_name', required=True)
    parser.add_argument('-k', '--hour', required=False)
    parser.add_argument('-m', '--min', required=False)
    parser.add_argument('-s', '--sec', required=False)
    args = parser.parse_args()
    hour_to_sec = int(args.hour) * 3600 + int(args.min) * 60 + int(args.sec)
    gen_iter = Timer(args.first_name, args.last_name, hour_to_sec)
    for i in gen_iter:
        print(i)

if __name__ == '__main__':
    main()
