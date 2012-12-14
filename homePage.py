from initClassifier import clf as classifier
import datetime
import pymongo


class Analizer(object):
    def __init__(self, thres = 0.15):
        self.thres = 0.15

    def spamProbability(self, string):
        return classifier.predict_proba([string])[0][1]

    def isCertain(self, p):
        isUncertain = (0.5 - self.thres) < p < (0.5 + self.thres)
        return bool(not isUncertain)

    def isSpam(self, p):
        if self.isCertain(p):
            return bool(p > 0.5)
        else:
            return False

class HomePage(Analizer):
    def __init__(self, thres = 0.15, renderer = None):
        super(HomePage, self).__init__(thres = thres)
        self.template = 'home.html'
        self.logger = pymongo.Connection()['logger']['spam']
        self.renderer = renderer

    def render(self, body = None):
        if body is not None:
            renderVariables = self.getVariables(body)
            self.log(**renderVariables)
        else:
            renderVariables = {}
        return self.renderer(self.template, **renderVariables)

    def log(self, **kw):
        doc = kw.copy()
        timestamp = datetime.datetime.now()
        doc.update({'timestamp': timestamp})
        self.logger.insert(doc)

    def getVariables(self, body):
        p = self.spamProbability(body.strip())
        return {'isSpam': self.isSpam(p),
                'isCertain': self.isCertain(p),
                'body': body.strip(),
                'probSpam': p}

