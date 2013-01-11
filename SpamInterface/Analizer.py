from initClassifier import Classifier

class Analizer(Classifier):
    def __init__(self, thres = 0.15, *args, **kwargs):
        super(Analizer, self).__init__(*args, **kwargs)
        self.thres = 0.15

    def spamProbability(self, review):
        text = review.comentario + ' ' + review.titulo
        return self.clfMixto(text,
                             review.denuncia,
                             review.numLikes,
                             review.userPois,
                             review.userAvaliacoes,
                             review.userFotos,
                             review.poiAvaliacoes,
                             review.poiRating,
                             review.poiUp)
    #def clfMixto(self, text, reportAbuso, numLikes, usrNumPois, usrNumAvaliacoes, usrNumFotos, poiNumAvaliacoes, poiRating, poiThumbsUp):

    def isCertain(self, p):
        isUncertain = (0.5 - self.thres) < p < (0.5 + self.thres)
        return bool(not isUncertain)

    def isSpam(self, p):
        if self.isCertain(p):
            return bool(p > 0.5)
        else:
            return False
