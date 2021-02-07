# Создать программу Pomodoro (https://ru.wikipedia.org/wiki/
# Метод_помидора).
# На вход программа получает имя, фамилию, время для
# фокусировки(по-умолчанию 25 минут), длину перерыва(по-
# умолчанию 5 минут), количество циклов(по-умолчанию 4) и
# название задачи. Программа указывает оставшееся время
# фокусировки, после сигнализирует о наступлении перерыва,
# после сигнализирует о начале нового цикла фокусировки.
# Программа должна вести файл лога о всех запусках.

from time import sleep
from datetime import datetime
import time as my_time
import csv
import argparse
from typing import Generator
import os


def header_template(my_csv):
    with open(my_csv, 'w') as file:
        fieldnames = ['first_name', 'last_name', 'program_name', 'time_stamp']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def fields_csv(my_csv):
    start_with = 'first_name'
    is_exist = os.path.exists(my_csv)

    if not is_exist:
        header_template(my_csv)

    elif os.stat(my_csv).st_size == 0:
        header_template(my_csv)

    elif is_exist:
        with open(my_csv) as file:
            read = csv.reader(file)
            row1 = next(read)
            if start_with not in row1:
                header_template(my_csv)
            else:
                pass


def logging(f_name: str, l_name: str, program: str, my_csv: str) -> None:
    with open(my_csv, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([f_name, l_name, program, datetime.now().strftime('%d-%m-%Y %H:%M:%S')])


def timer(timing: int) -> Generator:
    for n in range(timing):
        sleep(1)
        counter = my_time.strftime("%H:%M:%S", my_time.gmtime(timing - 1))
        timing -= 1
        yield counter


def parser(my_csv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', '--first_name', default='Petr')
    parser.add_argument('-ln', '--last_name', default='Petrov')
    parser.add_argument('-f', '--focus_time', default=1500)
    parser.add_argument('-t', '--time_out', default=300)
    parser.add_argument('-c', '--cycles', default=4)
    parser.add_argument('-p', '--program', default='Method Pomodoro')
    args = parser.parse_args()

    name = args.first_name
    last_name = args.last_name
    cycle = int(args.cycles)
    work = int(args.focus_time)
    pause = int(args.time_out)
    program = args.program

    for i in range(cycle):
        logging(name, last_name, program, my_csv)
        gen_work = timer(work)
        print('Work')
        for time_counter in gen_work:
            print(time_counter)

        gen_break = timer(pause)
        print('Break')
        for break_counter in gen_break:
            print(break_counter)


def main():
    my_csv = 'log.csv'
    fields_csv(my_csv)
    parser(my_csv)


if __name__ == '__main__':
    main()

