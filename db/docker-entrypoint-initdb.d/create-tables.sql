CREATE TABLE users (
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE,
    PASSWORD VARCHAR(60) NOT NULL
);

INSERT INTO users (name, email, password)
    VALUES ('Igor Nadiein', 'nadiein@dev.com', '1234');