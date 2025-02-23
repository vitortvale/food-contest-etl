ALTER TABLE truck ADD CONSTRAINT unique_truck_name UNIQUE (name);
INSERT INTO trucks (name) VALUES
    ('Grill Thrill Express'),
    ('Smoky Wheels BBQ'),
    ('Patty Wagon'),
    ('Bun Voyage'),
    ('The Rolling Flame'),
    ('Melt & Move'),
    ('Cheddar Chariot');
ON CONFLICT (name) DO NOTHING;
