# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from SpamInterface import HomePage
from flaskext.markdown import Markdown
from mongoLogger import MongoLogger

app = Flask(__name__)
Markdown(app)

homePage = HomePage(renderer = render_template)
logger = MongoLogger()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        answer = True if request.form['IsSpam'] == "True" else False
        answerData = homePage.processModeratorAnswer(moderatorAnswer = answer)
        homePage.getNewReview()
        reviewData = homePage.getReviewData()
        logger.log(answerData)
        return homePage.render(reviewData, answerData)
    else:
        homePage.getNewReview()
        reviewData = homePage.getReviewData()
        return homePage.render(reviewData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    print "ready..."
