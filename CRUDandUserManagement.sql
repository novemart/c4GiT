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

select * from items;

insert into users values (1, 'sholmes', 'sherlock@me.com', 1);

-- read all data from the database
select * from users;

-- incorrect foreign key, will throw error
insert into users values (4, 'watson', 'dr@me.com', 2);

insert into items(item_desc, item_name, price) values('super cool magnifying glass', 'Magnifying glass', 15.95);

insert into items(item_desc, item_name,  price) values('smoking is bad for you', 'Pipe',  15.95);

insert into users(username, email, item_id) values ('myusuf', 'martina@qa.com', 2), ('johnd', 'john.doe@gmail.com', 1);

select * from Users where username = 'myusuf';

alter table users add column lastName varchar(30);

 create table Goods(
 id int primary key auto_increment,
 descrip varchar(100) default 'Description',
 price float(4,2) not null,
 name varchar(20) not null);
 
 insert into Goods(price, name) values (4.5, 'chocolate');
 
 insert into Goods(price, name) values (5.5, 'strawberries');
 
 
 select * from Goods;
 
 update Goods set descrip = 'Yummy chocolate' where id=1;
 
 -- clear rows
delete from Goods where id = 1;

-- will throw and error
delete from Goods where name = 'chocolate';

select descrip as 'Description' , price * 1.2 as 'incl. VAT', name as 'Item name' from Goods;

select concat(name,' - ',descrip) as 'Stock' from Goods;

select username from users order by username desc;

select username from users where id>1 and id<3;

-- between is inclusinve
select username from users where id between 1 and 3;


-- join statement
select username, email, item_desc, item_name from users inner join items on users.item_id = items.id where users.id = 1; 

select * from users;

select username, email, item_desc, item_name from users right outer join items on users.item_id = items.id; 
 
-- user management
create user 'martina1'@'localhost' identified by 'password';

grant select on shopping_cart.* to 'martina1'@'localhost';

grant insert on shopping_cart.* to 'martina1'@'localhost';

revoke insert on shopping_cart.* from 'martina1'@'localhost';

drop user 'martina1'@'localhost';
 
