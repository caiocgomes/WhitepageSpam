# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from homePage import HomePage
from analise import Analise
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

homePage = HomePage(renderer = render_template)
analisador = Analise(renderer=render_template)

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        body = request.form['reviewBody']
        return homePage.render(body)
    except KeyError, e:
        print e
        return homePage.render()

@app.route('/analise', methods=['GET', 'POST'])
def analise():
    try:
        body = request.form['body']
        return analisador.render(body)
    except KeyError, e:
        print e
        return analisador.render()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

