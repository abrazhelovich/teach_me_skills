# Создать класс MyTime. Атрибуты: hours, minutes,
# seconds. Методы: переопределить магические методы
# сравнения(==, !=, >=, <=, <, >), сложения, вычитания,
# умножения на число, вывод на экран.
# Примечание: список «магических методов» можно
# посмотреть тут: https://pythonworld.ru/osnovy/
# peregruzka-operatorov.html

from datetime import time
from datetime import datetime
import time as my_time


class MyTime:
    def __init__(self, hour: int, minutes: int, seconds: int) -> None:
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return time(self.hour, self.minutes, self.seconds) == time(other.hour, other.minutes, other.seconds)

    def __ne__(self, other):
        return time(self.hour, self.minutes, self.seconds) != time(other.hour, other.minutes, other.seconds)

    def __ge__(self, other):
        return time(self.hour, self.minutes, self.seconds) >= time(other.hour, other.minutes, other.seconds)

    def __le__(self, other):
        return time(self.hour, self.minutes, self.seconds) <= time(other.hour, other.minutes, other.seconds)

    def __lt__(self, other):
        return time(self.hour, self.minutes, self.seconds) < time(other.hour, other.minutes, other.seconds)

    def __gt__(self, other):
        return time(self.hour, self.minutes, self.seconds) > time(other.hour, other.minutes, other.seconds)

    def __add__(self, other):
        result = self.hour * 3600 + self.minutes * 60 + self.seconds
        return my_time.strftime("%H:%M:%S", my_time.gmtime(result + other))

    def __sub__(self, other):
        result = self.hour * 3600 + self.minutes * 60 + self.seconds
        return my_time.strftime("%H:%M:%S", my_time.gmtime(result - other))

    def __mul__(self, other):
        result = self.hour * 3600 + self.minutes * 60 + self.seconds
        return my_time.strftime("%d:%H:%M:%S", my_time.gmtime(result * other))


def main():
    other = 10
    time1 = MyTime(10, 15, 50)
    time2 = MyTime(16, 50, 37)
    pr_time1 = time(time1.hour, time1.minutes, time1.seconds)
    pr_time2 = time(time2.hour, time2.minutes, time2.seconds)

    print(f'{pr_time1} == {pr_time2} ->', time1 == time2)
    print(f'{pr_time1} != {pr_time2} ->', time1 != time2)
    print(f'{pr_time1} >= {pr_time2} ->', time1 >= time2)
    print(f'{pr_time1} <= {pr_time2} ->', time1 <= time2)
    print(f'{pr_time1} < {pr_time2} ->', time1 < time2)
    print(f'{pr_time1} > {pr_time2} ->', time1 > time2)
    print()
    print(f'{pr_time1} + {other} ->', time1 + other)
    print(f'{pr_time2} - {other} ->', time2 - other)
    print(f'{pr_time1} * {other} ->', time1 * other)


if __name__ == '__main__':
    main()
