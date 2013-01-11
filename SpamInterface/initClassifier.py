import cPickle as pickle
import unicodedata

def countNumber(text):
    return sum([text.count(str(i)) for i in range(10)])

def strip_accents(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

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
        prob = self.clfuser.predict_proba([numPois, numAvaliacoes, numFotos])
        print prob.shape, prob
        return prob[0][1]

    def clfPoi(self, numAvaliacoes, rating, thumbsUp):
        prob = self.clfpoi.predict_proba([numAvaliacoes, rating, thumbsUp])
        print prob.shape, prob
        return prob[0][1]

    def clfBigram(self, text):
        prob = self.clfbig.predict_proba([text])
        print prob.shape, prob
        return prob[0][1]

    def clfTxt(self, text):
        prob = self.clftxt.predict_proba([text])
        print prob.shape, prob
        return prob[0][1]

    def clfReview(self, denuncia, numLikes, text):
        vec = [denuncia, len(text), numLikes, countNumber(text)]
        prob = self.clfrev.predict_proba(vec)
        print prob
        return prob[0][1]

    def clfMixto(self, text, denuncia, numLikes, usrNumPois, usrNumAvaliacoes, usrNumFotos, poiNumAvaliacoes, poiRating, poiThumbsUp):
        uniText = strip_accents(text.decode('utf-8'))
        print "==============================================================================================="
        print (uniText)
        print "==============================================================================================="

        vec = [self.clfTxt(uniText),
               self.clfBigram(uniText),
               self.clfReview(denuncia, numLikes, uniText),
               self.clfUser(usrNumPois, usrNumAvaliacoes, usrNumFotos),
               self.clfPoi(poiNumAvaliacoes, poiRating, poiThumbsUp)]
        prob = self.clfmix.predict_proba(vec)
        print prob.shape, prob
        return prob[0][1]



