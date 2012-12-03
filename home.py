# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from initClassifier import clf as classifier
from mongoLogger import mngLogger

app = Flask(__name__)

class HomePage(object):
    def __init__(self, classificationThreshold = 0.15):
        self.template = 'home.html'
        self.thres = classificationThreshold

    def render(self, body = None):
        if body is not None:
            renderVariables = self.getVariables(body)
            mngLogger.log(renderVariables)
        else:
            renderVariables = {}
        return render_template(self.template, **renderVariables)

    def getVariables(self, body):
        p = self.spamProbability(body)
        return {'isSpam': self.isSpam(p),
                'isCertain': self.isCertain(p),
                'body': body,
                'probSpam': p}

    def spamProbability(self, string):
        return classifier.predict_proba([string])[0][1]

    def isCertain(self, p):
        isUncertain = (0.5 - self.thres) < p < (0.5 + self.thres)
        return (not isUncertain)

    def isSpam(self, p):
        if self.isCertain(p):
            return (p > 0.5)
        else:
            return False

homePage = HomePage()

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        body = request.form['reviewBody']
        return homePage.render(body)
    except KeyError, e:
        print e
        return homePage.render()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

