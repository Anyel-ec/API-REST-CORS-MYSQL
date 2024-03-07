create database if not exists svelte;
use svelte;
drop table if exists productos;

create table productos(
    id_productos int primary key auto_increment,
    descripcion varchar(50),
    codigo int,
    categoria varchar(50),
    cantidad int
);

insert into productos(descripcion, codigo, categoria, cantidad) values('papas', 123, 'verduras', 10);
insert into productos(descripcion, codigo, categoria, cantidad) values('cebolla', 124, 'verduras', 20);
insert into productos(descripcion, codigo, categoria, cantidad) values('tomate', 125, 'verduras', 30);
insert into productos(descripcion, codigo, categoria, cantidad) values('lechuga', 126, 'verduras', 40);
insert into productos(descripcion, codigo, categoria, cantidad) values('zanahoria', 127, 'verduras', 50);
insert into productos(descripcion, codigo, categoria, cantidad) values('pimiento', 128, 'verduras', 60);
insert into productos(descripcion, codigo, categoria, cantidad) values('pepino', 129, 'verduras', 70);