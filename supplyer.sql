CREATE TABLE supplier(
    SNO TEXT PRIMARY KEY,
    SHAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier  VALUES
    ('51', 'Smith', 20, 'London'),
    ('52','Jones', 18, 'Paris'),
    ('53','Blake',38, 'Paris'),
    ('54', 'Clarke',28,'London'),
    ('55','Adam',38,'Albema');

SELECT * FROM supplier;