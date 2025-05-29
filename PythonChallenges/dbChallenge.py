import sqlite3

#Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

#Create the Roster table
cursor.execute("""
    CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        IQ INTEGER
      )
""")

#Insert data into the Roster Table
roster_data = [
    ('Jean-Baptiste Zorg','Human',122),
    ('Korben Dallas','Meat Popsicle',100),
    ('Ak\'not','Mangalore',-5)
]

cursor.executemany('INSERT INTO Roster VALUES(?,?,?)', roster_data)

cursor.execute("""
    UPDATE Roster
    SET Species = 'Human'
    WHERE Name = 'Korben Dallas'
""")

cursor.execute("""
    SELECT Name, IQ
    FROM Roster
    WHERE Species = 'Human'
""")

#Fetch and print results
human = cursor.fetchall()
for name, iq in human:
    print('{}: IQ {}'.format(name, iq))
