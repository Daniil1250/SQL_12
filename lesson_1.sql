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
