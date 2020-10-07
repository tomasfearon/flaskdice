from flask import Flask, render_template, request
import random
import re
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def roller():
    if request.method == 'POST':
        type = request.form['submit_button']
        sides = str(type).replace('d', '')
        value = random.randint(1,int(sides))
        return render_template('index.html', type=type, value=value)
       
if __name__ == '__main__':
    app.run()
