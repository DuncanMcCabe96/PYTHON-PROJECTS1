import sqlite3

#Get personal data from user
firstName = input("Enter your frist name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#execute insert statement for supplied person data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)
