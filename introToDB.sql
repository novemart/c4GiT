create database if not exists cohort4;

use cohort4;

-- this is a comment
show tables;

create table items(
id int primary key auto_increment,
item_desc varchar(120),
item_name varchar(50) not null,
price float not null);

create table users(
id tinyint primary key auto_increment,
username varchar(20) not null,
email varchar(50) not null,
item_id int not null,
foreign key (item_id) references items(id));

insert into items values(1, 'super old-school hat', 'Hat', 9.95);

select * fromsome_table items;

insert into users values (1, 'sholmes', 'sherlock@me.com', 1);

-- read all data from the database
select * from users;

-- incorrect foreign key, will throw error
insert into users values (1, 'watson', 'dr@me.com', 4);

insert into items(item_desc, item_name, price) values('super cool magnifying glass', 'Magnifying glass', 15.95);

insert into items(item_desc, item_name,  price) values('smoking is bad for you', 'Pipe',  15.95);