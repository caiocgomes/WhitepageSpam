from Oracle import Oracle

class ReviewStream(Oracle):
    def __init__(self, p = 1.0, *args, **kwargs):
        super(ReviewStream, self).__init__(*args, **kwargs)
        self.p = p

    def __iter__(self):
        query = self.__query()
        for rid, comment, oldComment, clf in self.query(query):
            text = self.__selectCorrectText(comment, oldComment, clf)
            yield text

    def __query(self):
        rawQuery = "SELECT review_id, comentario, comentario_old, classificacao FROM meu_apnt_v6.tbl_review SAMPLE({p})"
        return rawQuery.format(p = self.p)

    def __selectCorrectText(self, comment, oldComment, clf):
        return oldComment if clf == 'REJECT' else comment
