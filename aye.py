import sqlite3

conn = sqlite3.connect("quiz_1.sqlite")

cursor = conn.cursor()

#cursor.execute("DROP TABLE IF EXISTS quiz")
##3cursor.execute("DROP TABLE IF EXISTS question")
#.execute("DROP TABLE IF EXISTS quiz_content")
#.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY, name VARCHAR)
''')

conn.commit()
cursor.execute('''CREATE TABLE IF NOT EXISTS question (id INTEGER PRIMARY KEY, 
               question VARCHAR, 
               answer VARCHAR, 
               wrong1 VARCHAR,
               wrong2 VARCHAR,
               wrong3 VARCHAR
               )''')
conn.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz_content (
               id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                FOREIGN KEY (question_id) REFERENCES question (id)
                 )
''')


questions = [
    ('When ukraine become free','1991','1990','1989','1989'),
    ('What is the capital of France','Paris','London','Berlin','Lviv')

]
cursor.executemany('''INSERT INTO question 
                   (question, answer, wrong1, wrong2, wrong3) 
                   VALUES (?, ?, ?, ?, ?)''', questions)
conn.commit()
quiziz = [("qweqwe",), ("123123",)]

cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quiziz)
conn.commit()

#cursor.execute('''INSERT INTO quiz_content 
 #              (quiz_id, question_id)
##                VALUES (?,?)''', [2, 1])
#conn.commit()   

cursor.execute('''SELECT question.question, question.answer FROM question, quiz_content 
               WHERE question.id == quiz_content.question_id 
               AND quiz_content.quiz_id == ?''', [1])
data = cursor.fetchall()
print(data)