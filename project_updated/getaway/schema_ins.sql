
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS TRANSPORTATION;
DROP TABLE IF EXISTS COUNTRIES;
DROP TABLE IF EXISTS CONTINENTS;

CREATE TABLE IF NOT EXISTS Customers(
	email varchar(20) PRIMARY KEY,
	likes_heat boolean default False,
	plane_pref boolean default False,
	boat_pref boolean default False, 
	train_pref boolean default False,
    Budget int,
	password varchar(120),
	name varchar(60)
);

INSERT INTO public.customers(EMAIL, likes_heat, plane_pref, boat_pref, train_pref, Budget, password, name) VALUES ('hej@mail.dk', TRUE, TRUE, FALSE, FALSE, 3000, 'hej1234',  'Johanne');
INSERT INTO public.customers(EMAIL, likes_heat, plane_pref, boat_pref, train_pref, Budget, password, name) VALUES ('dav@mail.dk', TRUE, FALSE, TRUE, FALSE, 20000, '$2b$12$KFkp1IEMGT4QrWwjPGhE3ejOv6Z3pYhx',  'Morten');




CREATE table if not exists COUNTRIES 
	(
		ctryName varchar PRIMARY KEY, 
		id_cont integer not NULL, 
		hot Boolean, 
		Price int
    )
;


CREATE TABLE IF NOT EXISTS CONTINENTS
	(
		contID INTEGER NOT NULL PRIMARY KEY,
        contName VARCHAR(25) NOT NULL
    )
;


CREATE TABLE IF NOT EXISTS TRANSPORTATION
	(
		ctryName varchar ,
		avg_plane_price INT, 
		avg_train_price INT, 
		avg_boat_price INT,
		PRIMARY KEY (ctryName),
		FOREIGN KEY (ctryName) REFERENCES Countries ON DELETE CASCADE
    )
;

INSERT INTO CONTINENTS (contID, contName) VALUES (1, 'AFRICA'), (2, 'EUROPE'), (3, 'ASIA'), (4, 'SOUTH AMERICA'), 
(5, 'NORTH AMERICA'), 
(6, 'AUSTRALIA'), 
(7, 'ANTARCTICA')
;


INSERT INTO COUNTRIES (ctryName, id_cont, hot, price) VALUES 
	('Italy', 2, True, 3000),
    ('Greece', 2, True, 2700),
    ('Spain', 2, True, 2650),
    ('Portugal', 2, True, 3200),
    ('Germany', 2, False, 800),
    ('Romania', 2, False, 1000),
    ('Croatia', 2, True, 1200),
    ('United Kingdom', 2, False, 1400),
    ('Ireland', 2, False, 1300),
    ('Turkey', 8, True, 2500),
    ('Russia', 8, False, 4200),
    ('Holland', 2, False, 2000),
    ('France', 2, True, 3800),
    ('Australia', 6, False, 10000), 
	('Antarktis', 7, False, 20000),
	('USA', 6, False, 5600) ;

INSERT INTO TRANSPORTATION (ctryName,
		avg_plane_price, 
		avg_train_price, 
		avg_boat_price) VALUES ('Italy', 400, 268, NULL), 
		('Greece', 500, 343, 1000), 
		('Portugal', 249, 195, 300),
		('Spain', 400, 125, 419	),
		('Germany', 136, 98, 130), 
		('Romania', 340, 220, NULL),
		('Croatia', 600, 370, NULL),
		('United Kingdom', 220, 587, 330), ('Ireland', 239, 783, 900), ('Turkey', 1200, 345, NULL), ('Russia', 2000, 450, NULL), ('Holland', 260, 120, NULL), ('France', 300, 430, 45), ('Australia', 10000, NULL, 23000), ('Antarktis', 45000, 43000, NULL),
		('USA', 3000, NULL, 2240);
		
