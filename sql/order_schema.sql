CREATE TABLE IF NOT EXISTS trucks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) 
)

CREATE TABLE IF NOT EXISTS burgers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64),
    price NUMERIC,
    truck_id INTEGER,
    FOREIGN KEY truck_id REFERENCES trucks(id)

)

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64),
    amount SMALLINT,
    time CHAR(5),
    FOREIGN KEY burguer_id SMALLINT REFERENCES burgers(id)
)


