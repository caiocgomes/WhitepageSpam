from ReviewStream import ReviewStream
from Pipeline import Pipeline
from gensim import corpora, models
import re

wordPattern = re.compile(ur'[\w]+', re.UNICODE)

def preProcessing(text):
    return text.lower()

def tokenizer(text):
    return wordPattern.findall(text)

class ReviewCorpusWords(Pipeline):
    def __init__(self, textStream, *args, **kwargs):
        super(ReviewCorpusWords, self).__init__(*args, **kwargs)
        self.pipeline = [preProcessing, tokenizer]
        self.textStream = textStream

    def __iter__(self):
        for item in self.textStream:
            yield self(item)

class ReviewCorpusBoW(ReviewCorpusWords):
    def __init__(self, *args, **kwargs):
        super(ReviewCorpusBoW, self).__init__(*args, **kwargs)
        self.dictionary = corpora.Dictionary(super(ReviewCorpusBoW, self).__iter__())
        self.pipeline = [preProcessing, tokenizer, self.dictionary.doc2bow]

class ReviewCorpusTFIDF(ReviewCorpusBoW):
    def __init__(self, *args, **kwargs):
        super(ReviewCorpusTFIDF, self).__init__(*args, **kwargs)
        self.tfidf = models.TfidfModel(super(ReviewCorpusTFIDF, self).__iter__())
        self.pipeline = [preProcessing, tokenizer, self.dictionary.doc2bow, self.getTFIDF]

    def getTFIDF(self, doc):
        return self.tfidf[doc]

def run():
    rs = ReviewStream(p = 99)
    rc = ReviewCorpusTFIDF(rs)
    model = models.ldamodel.LdaModel(rc, id2word=rc.dictionary, num_topics=100, passes = 1)
    return rs, rc, model
