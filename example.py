import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query all data based on condition
cursor.execute("SELECT * FROM events WHERE date='2002.03.05'")
row = cursor.fetchall()
print(row)

# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE date='2025.11.20'")
row = cursor.fetchall()
print(row)

# insert new rows
new_row = [('Cats', 'Cat City', '2088.10.17'),
           ('Hens', 'Hens City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_row)
connection.commit()

#query all the data
cursor.execute("SELECT * FROM events")
row = cursor.fetchall()
print(row)