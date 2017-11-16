CREATE DATABASE IF NOT EXISTS 1311992289_vef1lokaverk;

USE 1311992289_vef1lokaverk;

CREATE TABLE IF NOT EXISTS users
(
	ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name varchar(30) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    PPicFile VARCHAR(255),
    descr TEXT
);

CREATE TABLE IF NOT EXISTS achievs
(
	ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    descr TEXT,
    userID INT NOT NULL,
    FOREIGN KEY (userID) REFERENCES users(ID)
);

CREATE TABLE IF NOT EXISTS submiss
(
	ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    gold INT NOT NULL,
    dead BOOL NOT NULL,
    score BIGINT NOT NULL,
    userID INT NOT NULL,
    FOREIGN KEY (userID) REFERENCES users(ID)
);


INSERT INTO users(name, password, PPicFile, descr)
VALUES
(
	"admin",
    "1234",
    "./static/lol.png",
    "I'M GAY"
);

INSERT INTO submiss(gold, dead, score, userID)
VALUES
(
	2000,
    false,
    5200,
    1
);

SELECT users.name, submiss.gold, submiss.dead, submiss.score
FROM submiss
	JOIN users
		ON users.ID = submiss.userID
ORDER BY submiss.score DESC
LIMIT 10;

SELECT * FROM submiss;


SELECT users.ID FROM users WHERE password='1234';

SELECT * FROM users;

DROP TABLE submiss;
DROP TABLE achievs;
DROP TABLE users;