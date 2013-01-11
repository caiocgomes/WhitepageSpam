import cPickle as pickle


def countNumber(text):
    return sum([text.count(i) for i in range(10)])

class Classifier(object):
    def __init__(self, *args, **kwargs):
        super(Classifier, self).__init__(*args, **kwargs)
        self.clfuser = pickle.load(open('CLFS/100mil-usr.clf', 'rb'))
        self.clfpoi  = pickle.load(open('CLFS/poi.clf', 'rb'))
        self.clfbig  = pickle.load(open('CLFS/text100mil-bigram.clf', 'rb'))
        self.clftxt  = pickle.load(open('CLFS/text100mil.clf', 'rb'))
        self.clfrev  = pickle.load(open('CLFS/100mil-txt.clf', 'rb'))
        self.clfmix  = pickle.load(open('CLFS/misto30mil-duplo.clf', 'rb'))

    def clfUser(self, numPois, numAvaliacoes, numFotos):
        return self.clfuser.predict_proba([numPois, numAvaliacoes, numFotos])[1]

    def clfPoi(self, numAvaliacoes, rating, thumbsUp):
        return self.clfPoi.predict_proba([numAvaliacoes, rating, thumbsUp])[1]

    def clfBigram(self, text):
        return self.clfbig.predict_proba(text)[1]

    def clfTxt(self, text):
        return self.clftxt.predict_proba(text)

    def clfReview(self, denuncia, numLikes, text):
        vec = [denuncia, len(text), numLikes, countNumber(text)]
        return self.clfrev.predict_proba(vec)[1]

    def clfMixto(self, text, denuncia, numLikes, usrNumPois, usrNumAvaliacoes, usrNumFotos, poiNumAvaliacoes, poiRating, poiThumbsUp):
        vec = [self.clfTxt(text),
               self.clfBigram(text),
               self.clfReview(denuncia, numLikes, text),
               self.clfUser(usrNumPois, usrNumAvaliacoes, usrNumFotos),
               self.clfPoi(poiNumAvaliacoes, poiRating, poiThumbsUp)]
        return self.clfmix.predict_proba(vec)[1]



