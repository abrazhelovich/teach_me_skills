-- Описать таблицу фильм: id, название, длительность,
-- режиссер, жанр фильма. Обратите внимание на то,
-- что у фильма может быть более одного жанра, а к
-- одному жанру может относится более, чем один
-- фильм.

create table Film(
	Film_Id int primary key,
	Film_Name varchar(60) not null,
	Film_Duration varchar(20) not null,
	Film_Director varchar(30) not null
);

create table Genre(
    Genre_Id int primary key,
    Genre_Name varchar(30) not null
);

create table FilmGenre(
    Film_id int,
    Genre_id int,
    primary key (Film_id, Genre_id),
    constraint fk_genre
                      foreign key (Genre_id)
                          references Genre(Genre_Id)
                          on delete cascade,
    constraint fk_film
                      foreign key (Film_id)
                          references Film(Film_id)
                          on delete cascade
);

insert into film(film_id, film_name, film_duration, film_director) values (1, 'Monster Hunter', ' 1 hr 39 mins', 'Paul William Scott Anderson');
insert into film(film_id, film_name, film_duration, film_director) values (2, 'The Father', ' 1 hr 37 mins', 'PKristina Grozeva');
insert into film(film_id, film_name, film_duration, film_director) values (3, 'The Secret Garden', ' 1 hr 35 mins', 'Grozeva PKristina');
insert into film(film_id, film_name, film_duration, film_director) values (4, 'The Little ThingsA', ' 2 hr 7 mins', 'Unknown');


insert into genre(genre_id, genre_name) values (1, 'Action');
insert into genre(genre_id, genre_name) values (2, 'Fantasy');
insert into genre(genre_id, genre_name) values (3, 'Adventure');
insert into genre(genre_id, genre_name) values (4, 'Drama');
insert into genre(genre_id, genre_name) values (5, 'Family');
insert into genre(genre_id, genre_name) values (6, 'Crime');
insert into genre(genre_id, genre_name) values (7, 'Thriller');


insert into filmgenre(Film_id, Genre_id) values (1, 1);
insert into filmgenre(Film_id, Genre_id) values (1, 2);
insert into filmgenre(Film_id, Genre_id) values (1, 3);
insert into filmgenre(Film_id, Genre_id) values (2, 4);
insert into filmgenre(Film_id, Genre_id) values (3, 4);
insert into filmgenre(Film_id, Genre_id) values (3, 5);
insert into filmgenre(Film_id, Genre_id) values (3, 2);
insert into filmgenre(Film_id, Genre_id) values (4, 4);
insert into filmgenre(Film_id, Genre_id) values (4, 6);
insert into filmgenre(Film_id, Genre_id) values (4, 7);