# Setting quantity of two different vehicles

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET Quantity = 10 WHERE Model = 'Civic'")
    c.execute("UPDATE inventory SET Quantity = 8 WHERE Model = 'Mustang'")

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()
    for r in rows:
        print r[0], r[1], r[2]