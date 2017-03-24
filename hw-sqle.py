import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders(Make TEXT, Model TEXT, Order_Date DATE)""")

    records = [
        ('Ford', 'Mustang', '2001-10-12'),
        ('Ford', 'Mustang', '2003-12-7'),
        ('Ford', 'Mustang', '2011-5-18'),
        ('Ford', 'Focus', '2013-3-21'),
        ('Ford', 'Focus', '2012-1-4'),
        ('Ford', 'Focus', '2009-8-23'),
        ('Ford', 'Fiesta', '2015-2-19'),
        ('Ford', 'Fiesta', '2007-4-15'),
        ('Ford', 'Fiesta', '2008-9-13'),
        ('Honda', 'Civic', '2005-11-26'),
        ('Honda', 'Civic', '2004-7-6'),
        ('Honda', 'Civic', '2002-6-1'),
        ('Honda', 'Accord', '2006-2-14'),
        ('Honda', 'Accord', '2000-3-31'),
        ('Honda', 'Accord', '2010-11-30')
    ]

    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", records)