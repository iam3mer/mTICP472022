create table books (
	id integer not null primary key,
	title varchar(60) not null,
	isbn varchar(60) not null unique,
	year numeric(4) not null
);

create table stock (
	id_book integer not null primary key,
	amount integer not null,
	foreign key (id_book) references books (id)
);

create table sales (
	sale_date date not null,
	id_book integer not null,
	amount integer not null,
	primary key (sale_date, id_book),
	foreign key (id_book) references books (id)
);

-- Consultar un libro por isbn
SELECT * FROM book WHERE isbn = 'sdgfsdf98798';

-- Obtener todos los libros en book
SELECT * FROM book;

-- Obtener la cantidad de libros en stcok por id
SELECT amount FROM stock WHERE id_book = 2;

-- Venta de libro
-- Comprobar la existencia del libro
-- getStock()

-- Anotar la venta
INSERT INTO sales (sale_date,id_book,amount) VALUES (datetime('now'),2,3);

-- Actualizar existencias
UPDATE stock SET amount = 7 WHERE id_book = 2;