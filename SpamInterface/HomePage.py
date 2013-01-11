from ReviewGetter import ReviewGetter
from Analizer import Analizer


class HomePage(Analizer, ReviewGetter):
    def __init__(self, renderer = None, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)
        self.template = 'home.mkd'
        self.renderer = renderer
        self.currentReview = self.getRandomReview()

    def getNewReview(self):
        self.currentReview = self.getRandomReview()

    def processModeratorAnswer(self, moderatorAnswer):
        renderVariables = self.getVariables(self.currentReview)
        algoAnswer = renderVariables['isSpam']
        return {'answer': True, 'algoAnswer': algoAnswer, 'moderatorAnswer': moderatorAnswer, 'oldReview_id': self.currentReview.review_id}

    def getReviewData(self):
        return self.getVariables(self.currentReview)

    def render(self, reviewData, answerData = None):
        data  = reviewData.copy()
        if answerData is not None:
            data.update(answerData)
        return self.renderer(self.template, **data)

    def getVariables(self, review):
        reviewData = {k:v.decode('utf-8') if isinstance(v, str) else v for (k,v) in review.__dict__.iteritems()}
        body = review.comentario #review.comentario.decode('utf-8')
        p = self.spamProbability(review)
        dados = {'answer': False,
                 'isSpam': self.isSpam(p),
                 'isCertain': self.isCertain(p),
                 'body': body.strip(),
                 'probSpam': p}
        dados.update(reviewData)
        return dados
