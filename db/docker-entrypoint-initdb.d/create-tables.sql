CREATE TABLE users (
    userId BIGINT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(60) NOT NULL,
    date TIMESTAMP,
    isAdmin BOOLEAN
);

CREATE TABLE description (
    descriptionId BIGINT NOT NULL PRIMARY KEY REFERENCES users (userId),
    image BYTEA,
    about TEXT,
    contact JSON
);

CREATE TABLE portfolio (
    portfolioId BIGINT NOT NULL PRIMARY KEY REFERENCES users (userId),
    companyName VARCHAR(100) NOT NULL,
    startDate DATETIME NOT NULL,
    endDate DATETIME,
    skills JSON,
    description TEXT
);

ALTER TABLE USERS
    ADD CONSTRAINT fk_portfolio FOREIGN KEY (userId) REFERENCES description (descriptionId),
        CONSTRAINT fk_description FOREIGN KEY (userId) REFERENCES portfolio (portfolioId);

BEGIN TRANSACTION;
    INSERT INTO users (name, email, password)
    VALUES ('Igor Nadiein', 'nadiein@dev.com', '1234');
COMMIT;