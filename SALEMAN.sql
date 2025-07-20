CREATE TABLE IF NOT EXISTS Saleman0(
    Salemans_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission TEXT
);

INSERT INTO Saleman0(Salemans_id, name, city, Comission)
VALUES
    ('5001', 'James Hong', 'New York', '0.15'),
    ('5002', 'Nail Knite', 'Paris', '0.13'),
    ('5005', 'Pil Alex', 'London', '0.13'),
    ('5006', 'Mc Lyon', 'Paris', '0.11'),
    ('5007', 'Pacl Adam', 'Ruman', '0.13'),
    ('5003', 'Lauson Hon', 'Sam Jose', '0.12');
SELECT * FROM Saleman0;
SELECT * FROM Saleman0 WHERE CITY = 'Paris';
SELECT * FROM Saleman0 ORDER BY Comission DESC;