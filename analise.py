from homePage import Analizer
from operator import itemgetter

class Analise(Analizer):
    def __init__(self, thres = 0.15, renderer = None):
        super(Analise, self).__init__(thres = thres)
        self.template = 'analise.mkd'
        self.renderer = renderer

    def render(self, body = None):
        if body is not None:
            renderVariables = self.getVariables(body)
        else:
            renderVariables = {}
        return self.renderer(self.template, **renderVariables)

    def getVariables(self, body):
        return {'body': body,
                'probSpam': self.spamProbability(body),
                'series': self.getSeries(body)}


    def getSeries(self, body):
        series = list(self.getSeriesUnordered(body))
        return sorted(series, key=itemgetter('delta'), reverse=True)

    def getSeriesUnordered(self, body):
        words = body.split()
        N = len(words)
        total = self.spamProbability(body)
        for i in xrange(N):
            text = ' '.join(words[0:i] + words[i+1:])
            excluded = words[i]
            p = self.spamProbability(text)
            delta = -(p - total)
            spamMsg = "spam" if self.isSpam(p) else "no spam"
            msg = "uncertain" if not self.isCertain(p) else spamMsg
            yield {'body': text,
                   'excluded': excluded,
                   'prob': p,
                   'delta': delta,
                   'msg': msg}
