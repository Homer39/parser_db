CREATE DATABASE vacancy_info

CREATE TABLE vacancies
(
vacancy_id INT PRIMARY KEY,
vacancy_name VARCHAR(100),
city VARCHAR(25),
url VARCHAR(100),
salary_from INT,
salary_to INT,
employer_name VARCHAR(100),
employer_id INT
);