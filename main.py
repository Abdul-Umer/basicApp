from flask import Flask

import os

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1> Hello</h1>"

@app.route('/about')
def about():
    return "<h3> This is Umer a Python Dev</h3>"

if __name__=="__main__":
    
    app.run(debug=True)