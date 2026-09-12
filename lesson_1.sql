CREATE TABLE users(
	id INT(20),
  	name VARCHAR(120),
  	email VARCHAR(90),
  	price INT(12)
);

INSERT INTO users VALUES(12, 'Иван', 'ivaN23@MAIL.RU', 344);
INSERT INTO users(id, email) VALUES(22, 'alena67@MAIL.RU');

SELECT * FROM users;
SELECT price FROM users;

drop table users;

-----------------------------------------------------------------------
CREATE TABLE Trip (
  id INT(12),
  company INT(12),
  plance VARCHAR(90),
  town_from VARCHAR(78),
  town_to VARCHAR(78),
  town_out DATETIME,
  time_in DATETIME
);


CREATE TABLE Company (
  id INT(12),
  name VARCHAR(34),
  age INT(12)
);


INSERT INTO Company VALUES (12, 'Петя', 45);
INSERT INTO Company VALUES (12, 'Иван', 18);
INSERT INTO Company VALUES (12, 'Женя', 17);
INSERT INTO Company VALUES (14, 'Вика', 15);

SELECT * FROM Company;
SELECT name, age FROM Company where age > 18;

DROP TABLE Company;
DROP TABLE Trip;




