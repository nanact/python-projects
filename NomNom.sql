CREATE TABLE IF NOT EXISTS nomnom(
    NAME TEXT,
    NEIGHBOR TEXT,
    CUISINE TEXT,
    REVIEW REAL,
    PRICE TEXT,
    HEALTH TEXT
);

INSERT INTO nomnom VALUES
    ('Peter','Remislyn','Streak',4.4,'$$$$','A'),
    ('Jongro', 'Hidtown', 'Korean', 3.5, '$$', 'A'),
    ('Kocha', 'Midtown', 'Pizza', 4.0, '$$$', 'U'),
    ('Lighthouse','Queens', 'Chinese',3.9,'$','A'),
    ('Minca', 'Downtown', 'Amorican',4.6,'$$$','');

SELECT * FROM nomnom;
SELECT DISTINCT NEIGHBOR FROM nomnom;
SELECT DISTINCT CUISINE FROM nomnom;
SELECT * FROM nomnom WHERE CUISINE = 'Chinese';
SELECT * FROM nomnom WHERE REVIEW >= 4.0;
SELECT * FROM nomnom WHERE PRICE = '$$$' AND CUISINE = 'Italine';
SELECT * FROM nomnom WHERE NAME LIKE '%Candy%';
SELECT * FROM nomnom WHERE NEIGHBOR IN ('Midtown', 'Downtown', 'Chinatown');
