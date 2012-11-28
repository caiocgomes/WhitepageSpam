# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

def checkSpam(body):
    return 'spam' in body

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('home.html')
    elif request.method == "POST":
        body = request.form['reviewBody']
        isSpam = checkSpam(body)
        return render_template('home.html', body = body, isSpam=isSpam)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

