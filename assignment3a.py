# Create a db and table to add 100 random integers

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # Delete table if exists and creates a new table
    c.execute("DROP TABLE if exists nums")
    c.execute("CREATE TABLE nums(nums INT)")

    # Create a list of ints

    for i in range(100):
        c.execute("INSERT INTO nums VALUES(?)", (random.randint(0, 100),))

