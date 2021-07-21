DROP DATABASE IF EXISTS flaskapp;

create database flaskapp;

drop user IF EXISTS 'flaskuser'@'localhost';

create user 'flaskuser'@'localhost' identified by 'flaskuser';

GRANT ALL PRIVILEGES ON `flaskapp` . * TO 'flaskuser'@'localhost';

USE flaskapp;

create table Result(

    id int auto_increment,
    a float,
    b float,
    sum float,
    sub float,
    mul float,
    division float,
    PRIMARY KEY(id)
);