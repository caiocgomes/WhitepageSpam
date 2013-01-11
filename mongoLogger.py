import datetime
import pymongo

class MongoLogger(object):
    def __init__(self, dbname = 'logger', colname = 'spam'):
        self.conn = pymongo.Connection()
        self.col = self.conn[dbname][colname]

    def listAll(self):
        return list(self.col.find())

    def log(self, doc):
        timestamp = datetime.datetime.now()
        doc.update({'timestamp': timestamp})
        self.col.insert(doc)
