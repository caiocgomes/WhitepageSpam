import cx_Oracle

class Oracle(object):
    def __init__(self, user='RAFAEL', passwd='WEB123', ip='192.168.1.212', service='AP10', *args, **kwargs):
        #super(Oracle, self).__init__(self, *args, **kwargs)
        args = {'user':user, 'passwd': passwd, 'ip': ip, 'service': service}
        connstring = '{user}/{passwd}@{ip}/{service}'.format(**args) #'RAFAEL/WEB123@192.168.1.212/AP10'
        self.con    = cx_Oracle.connect(connstring)

    def query(self, querystring):
        cursor = cx_Oracle.Cursor(self.con)
        cursor.execute(querystring)
        return cursor

    def fetchOne(self, querystring):
        cursor = self.query(querystring)
        return cursor.fetchone()

