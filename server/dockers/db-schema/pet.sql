CREATE DATABASE pets;

USE pets;

CREATE TABLE dogs(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    PRIMARY KEY (id),
    INDEX (name)
);

<<<<<<< HEAD
CREATE TABLE cats(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    PRIMARY KEY (id),
    INDEX (name)
);

=======
>>>>>>> upstream/master
CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL,
    PRIMARY KEY (id),
    INDEX (username)
);
<<<<<<< HEAD

=======
>>>>>>> upstream/master
INSERT INTO users (username, password) VALUES ('admin', 'admin');
