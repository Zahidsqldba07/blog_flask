CREATE TABLE users (
    userId BIGSERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(60) NOT NULL,
    date TIMESTAMP,
    isAdmin BOOLEAN
);

CREATE TABLE description (
    descriptionId BIGSERIAL PRIMARY KEY,
    image BYTEA,
    about TEXT,
    contact JSON,
    FOREIGN KEY (descriptionId) REFERENCES users (userId)
);

CREATE TABLE portfolio (
    portfolioId BIGSERIAL PRIMARY KEY,
    companyName VARCHAR(100) NOT NULL,
    startDate TIMESTAMP NOT NULL,
    endDate TIMESTAMP,
    skills JSON,
    description TEXT,
    FOREIGN KEY (portfolioId) REFERENCES users (userId)
);

-- ALTER TABLE users
--     ADD CONSTRAINT fk_description FOREIGN KEY (userId) REFERENCES description (descriptionId);
-- ALTER TABLE users
--     ADD CONSTRAINT fk_portfolio FOREIGN KEY (userId) REFERENCES portfolio (portfolioId);

BEGIN TRANSACTION;
    INSERT INTO users (name, email, password)
    VALUES ('Igor Nadiein', 'nadiein@dev.com', '1234');

    INSERT INTO description (image, about)
    VALUES (NULL, 'Hi, Im Igor!');

    INSERT INTO portfolio (companyName, startDate, endDate)
    VALUES ('DataRobot', '2020-09-14 10:00:00', NULL);
COMMIT;