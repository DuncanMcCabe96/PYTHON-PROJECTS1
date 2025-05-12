import sqlite3

#Provided file list
fileList = ['information.docx', 'Hello.txt', 'myImage.png',
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']

# Connect create the sqlite database
conn = sqlite3.connect('files_database.db')

# Create a cursor object to execute sql commands
cur = conn.cursor()

# Create a new table with two fields:
# - id: auto-incrementing primary key
# - filename: text field to store .txt filenames
cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        filename TEXT \
    )")

# Loop through each file name in the list
for file in fileList:
    # Check if the file ends with '.txt'
    if file.endswith('.txt'):
        # Insert the file name into the database
        cur.execute('INSERT INTO txt_files (filename) VALUES (?)', (file,))

# Commit the changes to the database
conn.commit()

# Select all records from the table
cur.execute('SELECT * FROM txt_files')

# Fetch all rows from the result
rows = cur.fetchall()

# Print the records in a readable format
print("Text files stored in the database:")
for row in rows:
    print(f"ID: {row[0]}, Filename: {row[1]}")

# Close the database connection
conn.close()
