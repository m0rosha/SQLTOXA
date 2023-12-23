import sqlite3
import random as rd

conn = sqlite3.connect("quiz_1.sqlite")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS quiz")
cursor.execute("DROP TABLE IF EXISTS question")
cursor.execute("DROP TABLE IF EXISTS quiz_content")

cursor.execute("DROP TABLE IF EXISTS quiziz")
conn.commit()

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


quiziz = [("Country quiz",), ("Car quiz",)]
cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quiziz)
conn.commit()

questions = [
    ('When ukraine become free', '1991', '1990', '1989', '1989'),
    ('What is the capital of France', 'Paris', 'London', 'Berlin', 'Lviv')
]
cursor.executemany('''INSERT INTO question 
                   (question, answer, wrong1, wrong2, wrong3) 
                   VALUES (?, ?, ?, ?, ?)''', questions)
conn.commit()

quiz_content = [
    (1, 1),
    (1, 2),
]
cursor.executemany('''INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)''', quiz_content)
conn.commit()

cursor.execute('''SELECT question.question, question.answer FROM question, quiz_content
              WHERE question.id == quiz_content.question_id 
          AND quiz_content.quiz_id == ?
          AND quiz_content.question_id==?''',[1,rd.randint(1,2)])



def gett_question(quiz_id, question_id):
    conn = sqlite3.connect('quiz_1.sqlite')
    cursor = conn.cursor()
    cursor.execute('''SELECT question.question, question.answer FROM question, quiz_content
              WHERE question.id == quiz_content.question_id 
          AND quiz_content.quiz_id == ?
          AND quiz_content.question_id == ?''', [question_id,quiz_id])
   
    data = cursor.fetchall()
    return data

data = cursor.fetchall()
print (data)
#china
