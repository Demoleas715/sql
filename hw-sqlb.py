# Inserting vehicles into the inventory table

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
        ('Ford', 'Mustang', 3),
        ('Ford', 'Focus', 2),
        ('Ford', 'Fiesta', 5),
        ('Honda', 'Civic', 4),
        ('Honda', 'Accord', 3)
    ]
    c.executemany("INSERT INTO inventory VALUES (?, ?, ?)", cars)