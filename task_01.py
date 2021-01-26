# Создать три класса, описывающие реальные объекты.
# Каждый класс должен содержать минимум три
# приватных атрибута, конструктор, геттеры и сеттеры
# для каждого атрибута, два метода.

class Car():
    def __init__(self, brand: str, model: str, year: int, owner: str) -> None:
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.owner = owner

    def check_owner(self) -> str:
        if len(self.owner) > 10:
            return self.owner
        return 'Unknow owner'

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
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: int) -> int:
        self.__year = year

class Door():
    def __init__(self, length: int, width: int, thickness: int, comment: str) -> None:
        self.__length = length
        self.__width = width
        self.__thickness = thickness
        self.comment = comment

    def volume_door(self) -> int:
        volume = self.__length * self.__width * self.__thickness
        return volume

    def add_comment(self, new_comment: str) -> str:
        self.new_comment = new_comment
        if not len(self.comment):
            text = self.comment + '' + self.new_comment
            return text

    @property
    def thickness(self) -> int:
        return self.__thickness

    @thickness.setter
    def thickness(self, thickness: int)-> int:
        self.__thickness = thickness
        return self.__thickness

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int) -> int:
        self.__length = length
        return self.__length

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int) -> int:
        self.__width = width
        return self.__width

class Cat():
    def __init__(self, name: str, age: int, breed: str, owner: str):
        self.__name = name
        self.__age = age
        self.__breed = breed
        self.owner = owner

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> str:
        self.__name = name
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> int:
        self.__age = age
        return self.__age

    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str) -> str:
        self.__breed = breed
        return self.__breed

def main():
    car_1 = Car('Ford', 'Fusion', 2015, 'Tim')
    car_1.brand = 'Volvo'
    car_1.model = 'S60'
    car_1.year = 2020
    car_1.owner = 'Uladzislau Tuk'
    #car_1.change_brand('- Five generation')
    print(car_1.brand, car_1.model, car_1.year, car_1.owner)
    print(car_1.check_owner())
    print(car_1.change_brand('- Five generation'))


    door = Door(2, 4, 3, '')
    door.thickness = 5
    #print(door.comment, door.thickness)
    print(f'The volume is {door.volume_door()}')
    print(door.add_comment('This is new comment'))


    cat1 = Cat('Tom', 5, 'British', 'Andrei')
    cat1.breed = 'Scotish'
    cat1.age = 22
    print(cat1.owner, cat1.age, cat1.breed)

if __name__ == '__main__':
    main()
