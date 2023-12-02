import sqlite3

conn = sqlite3.connect('Artistc.db')

cursor = conn.cursor()

#cursor.execute('INSERT INTO artists ("Artist ID", Name, Nationality, Gender, "Birth Year") VALUES ("123213","MAX", "Ukr", "Razeto", "2000")')
#conn.commit()

cursor.execute('SELECT * FROM artists WHERE Name =="MAX"')

data = cursor.fetchall()
print (data)

