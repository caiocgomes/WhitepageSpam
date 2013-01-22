import Corpora
import gensim

def parseLDATopic(topic):
    terms = topic.split(' + ')
    topicDict = {}
    for term in terms:
        strWeight, word = term.split('*')
        weight = float(strWeight)
        topicDict[word] = weight
    return topicDict

class CategoryTopics(object):
    def __init__(self, catid, limit=-1):
        self.catid = catid
        self.corpus = Corpora.CategoryCorpus(catid=catid, limit=limit)
        self.bowCorpus = Corpora.BoWCorpus(self.corpus)
        self.doclbsids =self.corpus.doclbsids

    def initTfIdfCorpus(self):
        self.tfidf = gensim.models.TfidfModel(self.bowCorpus)
        self.tfidfCorpus = self.tfidf[self.bowCorpus]

    def getLDATopics(self, numTopics = 100, numTopicsToGet = -1, topWords = 10):
        if not hasattr(self, 'ldamodel'):
            self.initTfIdfCorpus()
            self.ldamodel = gensim.models.ldamodel.LdaModel(self.tfidfCorpus, id2word = self.bowCorpus.dictionary, num_topics= numTopics)
        for topic in self.ldamodel.show_topics(topics=numTopics, topn=topWords):
            yield topic

    def getLDAVectors(self):
        if not hasattr(self, 'ldaCorpus'):
            self.ldaCorpus = self.ldamodel[self.tfidfCorpus]
        for k, doc in enumerate(self.ldaCorpus):
            yield self.doclbsids[k], doc

    def getLbsid(self, k):
        return self.doclbsids.get(k,None)
