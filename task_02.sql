-- Описать таблицу песня: id, название, длительность,
-- певец. При этом у песни может быть более одного
-- певца, а певец мог записать более одной песни.

create table Song(
	Song_Id int primary key,
	Song_Name varchar(60) not null,
	Song_Duration time
);

create table Singer(
    Singer_Id int primary key,
    Singer_Name varchar(30) not null
);


create table SongSinger
(
    Song_id   int,
    Singer_id int,
    primary key (Song_id, Singer_id),
    constraint fk_song
        foreign key (song_id)
            references Song (Song_Id)
            on delete cascade,
    constraint fk_singer
        foreign key (Singer_id)
            references Singer (Singer_id)
            on delete cascade
);

insert into Song(song_id, song_name, song_duration) values (1, 'Wind of change', '00:03:12');
insert into Song(song_id, song_name, song_duration) values (2, 'Yellow Butterfly', '00:02:58');
insert into Song(song_id, song_name, song_duration) values (3, 'We Will Rise Again', '00:02:37');
insert into Song(song_id, song_name, song_duration) values (4, 'Englishman In New York', '00:04:07');
insert into Song(song_id, song_name, song_duration) values (5, 'I Can''t Stop Thinking About You', '00:02:45');
insert into Song(song_id, song_name, song_duration) values (6, 'Beautiful Things', '00:03:01');

insert into Singer(singer_id, singer_name) values (1, 'Scorpions');
insert into Singer(singer_id, singer_name) values (2, 'Sting');
insert into Singer(singer_id, singer_name) values (3, 'Roxette');

insert into SongSinger(Singer_id, Song_id) values (1, 1);
insert into SongSinger(Singer_id, Song_id) values (1, 2);
insert into SongSinger(Singer_id, Song_id) values (1, 3);
insert into SongSinger(Singer_id, Song_id) values (2, 4);
insert into SongSinger(Singer_id, Song_id) values (2, 5);
insert into SongSinger(Singer_id, Song_id) values (3, 6);