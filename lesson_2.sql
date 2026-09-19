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
  age INT(12), 
  city VARCHAR(70)
);
INSERT INTO Company VALUES (12, 'Петя', 45, 'Уфа');
INSERT INTO Company VALUES (12, 'Иван', 18, 'Вологда');
INSERT INTO Company VALUES (12, 'Женя', 19, 'Москва');
INSERT INTO Company VALUES (14, 'Вика', 29, 'Владик');

SELECT * FROM Company;
-- SELECT name, age FROM Company where age > 18;
-- SELECT name, age, city FROM Company where age > 18 AND city = 'Москва';
-- SELECT * FROM company WHERE name LIKE 'В%';
-- SELECT * FROM company WHERE age BETWEEN 18 AND 30;
-- SELECT * FROM company WHERE city IN('Москва', 'Владик');


-- SELECT * FROM company ORDER BY age DESC;
-- SELECT * FROM company ORDER BY city ASC, age DESC;

-- SELECT * FROM company LIMIT 2;
-- SELECT DISTINCT city FROM Company;

--Агрегаты
SELECT COUNT(*) FROM Company;
SELECT AVG(age) FROM Company;
SELECT SUM(age) FROM Company;
SELECT MIN(age), MAX(age) FROM Company;



DROP TABLE Company;
DROP TABLE Trip;


-- Операторы 
-- OR, AND, NOT, IN, BETWEEN, LIKE
-- =, <>, >, <, >=, <=

-----------------------------------------------------------------------
-- ДЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗЗ

CREATE TABLE procuts (
  id INT PRIMARY KEY,
  name VARCHAR(100) not NULL,
  price DECIMAL(10, 2) not NULL,
  category VARCHAR(45) NOT NULL
);

SELECT category, AVG(price) AS avg_price FROM procuts GROUP BY category HAVING AVG(price) > 500;

