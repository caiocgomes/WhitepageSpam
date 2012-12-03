import pymongo
import datetime

class MongoLogger(object):
    def __init__(self, colname = 'spam'):
        self.conn = pymongo.Connection()
        self.col = self.conn.logger[colname]

    def log(self, doc):
        timestamp = datetime.datetime.now()
        doc.update({'timestamp': timestamp})
        self.col.insert(doc)

mngLogger = MongoLogger()

