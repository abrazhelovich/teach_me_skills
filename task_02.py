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
        #self.add_speed = add_speed
        self.__speed += 5
        return self.__speed

    def speed_down(self) -> int:
        #self.down_speed = down_speed
        self.__speed -= 5
        return self.__speed

    def speed_revers(self) -> int:
        #self.down_speed = down_speed
        self.__speed -= 10
        return self.__speed

    def change_brand(self, generation: str) -> str:
        self.generation = generation
        text = self.brand + ' ' + self.generation
        return text

    def change_brand(self, generation: str) -> str:
        self.generation = generation
        text = self.brand + ' ' + self.generation
        return text

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, brand: str) -> str:
        self.__brand = brand
        return self.__brand

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str) -> str:
        self.__model = model
        return self.__model

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> int:
        self.__year = year

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int) -> int:
        self.__speed = speed

def main():
    car1 = Car('Ford', 'Fusion', 2015, 0)

    print(car1.speed)
    print(car1.speed_up())
    #print(car1.brand, car1.year, car1.speed)
    #print(car1.speed)
    print(car1.speed_down())
    print(car1.speed_revers())
    #print()



if __name__ == '__main__':
    main()
