from flask import Flask

import os

app=Flask(__name__)

@app.route('/')
def home():
    name="muskan"
    return f"Hello {name}"

@app.route('/about')
def about():
    return "<h3> This is Umer a Python Dev</h3>"

if __name__=="__main__":
    app.run(host='0.0.0', port=5000, debug=True)
