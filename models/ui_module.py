from models.db_connection import engine, Base, session
from sqlalchemy.orm import sessionmaker
from models.brand import Brand
from models.car import Car

Base.metadata.create_all(engine)


def ui():
    val = int(input('''1.Create a new Brand and Car
2.Show all Brands, Cars and Release year
3.Update by product id
4.Delete by product id
5.Update by product id
Make a choice: \n\n'''))

    if val == 1:
        brand_name = input('New Brand please: ')
        car_name = input('New Car please: ')
        r_year = int(input('Release year please: '))

        for brand in session.query(Brand):
            if brand.name == brand_name:
                print(f'Brand "{brand_name}" already exist.')
                # car_1 = Car(model=car_name, release_year=r_year, brand=brand.id)  # Not working
                # session.add(car_1)
                # session.commit()
                # break
            else:
                brand_1 = Brand(name=brand_name)
                car_1 = Car(model=car_name, release_year=r_year, brand=brand_1)
                session.add_all([brand_1, car_1])
                session.commit()

        #brand_1 = Brand(name=brand_name)
        #car_1 = Car(model=car_name, release_year=r_year, brand=brand_1)
        #session.add(brand_1)
        # session.commit()

    if val == 2:
        for brand in session.query(Brand):
            print(f'{brand.id} - {brand.name} - {brand.cars}')

    if val == 3:
        brand_id = int(input('Brand ID: '))
        brand = session.query(Brand).filter_by(id=brand_id).first()
        brand.name = input('New Brand please: ')
        session.commit()
        print(f'Updated brand name {brand.name}')

        # for brand in session.query(Brand):
        #     print(f'{brand.id} - {brand.name} - {brand.cars}')

    if val == 4:  # not working
        brand_id = int(input('Brand ID: '))
        brand = session.query(Brand).filter_by(id=brand_id).first()
        session.delete(brand.car)
        session.delete(brand)
        session.commit()
        print('Done')
