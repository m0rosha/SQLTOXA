from flask import Flask, session
from aye import gett_question
import random as rd 


def result():
    return '<h1>Hello World</h1>'
def test():
    
    data = gett_question(1,session['cnt'])
    
    return f"<h4>{str(data)}</h4>"
def homepage():
    session['cnt'] = rd.randint(1,2)
    return '<a href="/test">Test</a>'

app = Flask(__name__)
app.config['SECRET_KEY'] ='BARANOVI4I'



app.add_url_rule('/','homepage',homepage)
app.add_url_rule('/result','result', result)
app.add_url_rule('/test','test', test)
app.run()
#ri
