drop table dept;
drop table emp;
drop table SALARIO;
delete salario;

CREATE TABLE SALARIO (
	ID INTEGER,
	Pago REAL NOT NULL,
	EMP_ID INTEGER,
	CONSTRAINT salario_pk PRIMARY KEY (ID),
	CONSTRAINT emp_fk FOREIGN KEY (EMP_ID) REFERENCES EMP(ID)
);

create table DEPT (
	ID integer,
	NAME varchar(25),
	constraint dept_pk primary key (ID)
	);

create table EMP (
	ID integer,
	LAST_NAME varchar(25),
	FIRTS_NMAE varchar(25),
	DEPT_ID integer,
	constraint emp_pk primary key (ID),
	constraint dept_fk foreign key (DEPT_ID) references DEPT(ID)
	);
	
insert into DEPT (NAME) values ('Sistemas');
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Barrera','Jhonatan',1);
insert into SALARIO (Pago, EMP_ID) values ('700000', 1);
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Tehelen','Simon',1);
insert into SALARIO (Pago, EMP_ID) values ('600000', 2);
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Barbosa','Andres',1);
insert into SALARIO (Pago, EMP_ID) values ('600000', 3);
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Pinilla','Santiago',1);
insert into SALARIO (Pago, EMP_ID) values ('700000', 4);

insert into DEPT (NAME) values ('Comercial');
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Sanchez','Francisco',2);
insert into SALARIO (Pago, EMP_ID) values ('500000', 5);
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Campos','Ivan',2);
insert into SALARIO (Pago, EMP_ID) values ('500000', 6);
insert into EMP (LAST_NAME,FIRTS_NMAE,DEPT_ID) values ('Perez','Gabriel',2);
insert into SALARIO (Pago, EMP_ID) values ('500000', 7);

SELECT * FROM EMP WHERE DEPT_ID = 1;
SELECT LAST_NAME, FIRTS_NMAE from emp where dept_id = 1;