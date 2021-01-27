# Создать класс Car. Атрибуты: марка, модель, год
# выпуска, скорость(по умолчанию 0). Методы:
# увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака
# скорости). Все атрибуты приватные.

class Car():
    def __init__(self, brand: str, model: str, year: int, speed: int) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_up(self) -> int:
        self.__speed += 5
        return self.__speed

    def speed_down(self) -> int:
        self.__speed -= 5
        return self.__speed

    def speed_revers(self) -> int:
        self.__speed -= 10
        return self.__speed

def main():
    car1 = Car('Ford', 'Fusion', 2015, 0)

    print(car1.speed)
    print(car1.speed_up())
    print(car1.speed_down())
    print(car1.speed_revers())

if __name__ == '__main__':
    main()
