import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT inventory.make, inventory.model, inventory.quantity, count(inventory.model) FROM orders, inventory WHERE inventory.model = orders.model")
    
    rows = c.fetchall()
    for r in rows:
        print r[0], r[1]
        print "quantity:", r[2]
        print "orders:", r[3]
        print