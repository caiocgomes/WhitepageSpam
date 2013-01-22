from Oracle import Oracle
from Review import MockReview, Review
from random import choice

class ReviewGetter(Oracle):
    def __init__(self, *args, **kwargs):
        super(ReviewGetter, self).__init__(*args, **kwargs)
        print "Loading reviews...",
        self.getAllReviewIds()
        print "done!"

    def getAllReviewIds(self):
        query = "SELECT review_id FROM meu_apnt_v6.tbl_review" #" WHERE classificacao is not null"
        self.reviewIds = [rid[0] for rid in self.query(query)]

    def popRandomReviewId(self):
        rid = choice(self.reviewIds)
        self.reviewIds.remove(rid)
        return rid

    def getRandomReview(self):
        columns = ['review_id', 'usuario_id', 'lbs_id', 'titulo', 'comentario', 'comentario_old', 'numlikes', 'denuncia', 'classificacao']
        rid = self.popRandomReviewId()
        query = """SELECT {columns} FROM meu_apnt_v6.tbl_review
        WHERE review_id = '{rid}'""".format(columns = ','.join(columns), rid = rid)
        revdata = self.fetchOne(query)
        print revdata
        doc = dict(zip(columns, revdata))
        return Review(**doc)

class MockReviewGetter(object):
    def __init__(self, *args, **kwargs):
        super(MockReviewGetter, self).__init__(*args, **kwargs)

    def getRandomReview(self, classified = None):
        return MockReview()
