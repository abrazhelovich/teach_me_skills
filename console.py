# Создать таблицы Brand(name), Car(model, release_year,
# brand(foreign key на таблицу Brand)). Реализовать
# CRUD(создание, чтение, обновление по id, удаление
# по id) для бренда и машины. Создать
# пользовательский интерфейс (использовать
# разделение логики по модулям - ui отдельно, работа с
# БД отдельно, запуск программы из консоли отдельно и
# т.д. в зависимости от логики приложения).

from models.car import Car
from models.brand import Brand
from sqlalchemy.orm import sessionmaker
from models.db_connection import engine, Base, session
from models.ui_module import ui

Base.metadata.create_all(engine)


def main():
    ui()

    brand_1 = Brand(name='Audi')
    brand_2 = Brand(name='Skoda')
    brand_3 = Brand(name='BMW')

    car_2 = Car(model='A5', release_year=2010, brand=brand_1)
    car_3 = Car(model='Octavia', release_year=2018, brand=brand_2)
    car_4 = Car(model='Fabia', release_year=2013, brand=brand_2)
    car_5 = Car(model='X3', release_year=2012, brand=brand_3)
    car_6 = Car(model='X6', release_year=2017, brand=brand_3)

    # session.add_all([brand_1, brand_2, brand_3,
    #                  car_1, car_2, car_3, car_4, car_5, car_6])
    # session.commit()

    # for brand in session.query(Brand):
    #     print(f'{brand.name} - {brand.cars}')


if __name__ == '__main__':
    main()
