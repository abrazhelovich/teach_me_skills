-- Реализовать таблицу машина: модель,
-- производитель, цвет, цена.
-- • Описать отдельную таблицу производитель: id,
-- название, рейтинг.
-- • Описать отдельную таблицу цвета: id, название.
-- У одной машины может быть только один
-- производитель, а у производителя — много машин. У
-- одной машины может быть много цветов, а у одного
-- цвета может быть много машин.

create table Producer(
    Producer_Id int primary key,
    Producer_Name varchar(30) not null,
    Producer_Rate real

);

insert into Producer(Producer_Id, Producer_Name, Producer_Rate) values (1, 'VW', 8.9);
insert into Producer(Producer_Id, Producer_Name, Producer_Rate) values (2, 'Audi', 9.0);
insert into Producer(Producer_Id, Producer_Name, Producer_Rate) values (3, 'Skoda', 8.5);

create table Car(
	Car_Id int primary key,
	Producer_id int,
	Car_Name varchar(20) not null,
	Car_Price real,
	CONSTRAINT fk_car
                     foreign key (Producer_id)
                         references Producer(Producer_Id)
                         on delete set null
);

insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (1, 1, 'Passat', 15500);
insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (2, 1, 'Polo', 12000);
insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (3, 1, 'Caddy', 13000);

insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (4, 2, 'A8', 16000);
insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (5, 2, 'Q7', 50000);
insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (6, 2, 'Q8', 80000);

insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (7, 3, 'Octavia', 15000);
insert into car(Car_Id, Producer_id, Car_Name, Car_Price) values (8, 3, 'Rapid', 14500);


create table Color(
    Color_ID int primary key,
    Color_Name varchar(15) not null
);

insert into Color(Color_Id, Color_Name) values (1, 'Red');
insert into Color(Color_Id, Color_Name) values (2, 'Blue');
insert into Color(Color_Id, Color_Name) values (3, 'Brown');
insert into Color(Color_Id, Color_Name) values (4, 'Black');
insert into Color(Color_Id, Color_Name) values (5, 'Green');


create table CarColor(
    Car_id int,
    Color_id int,
    primary key (Car_id, Color_id),
    constraint fk_car
                      foreign key (Car_id)
                          references Car(Car_Id)
                          on delete cascade,
    constraint fk_color
                      foreign key (Color_id)
                          references Color(Color_ID)
                          on delete cascade
);

insert into CarColor(Car_id, Color_id) values (1, 1);
insert into CarColor(Car_id, Color_id) values (1, 3);
insert into CarColor(Car_id, Color_id) values (2, 2);
insert into CarColor(Car_id, Color_id) values (2, 4);
insert into CarColor(Car_id, Color_id) values (2, 3);
insert into CarColor(Car_id, Color_id) values (3, 3);
insert into CarColor(Car_id, Color_id) values (3, 5);
