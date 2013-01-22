import cx_Oracle

user = 'RAFAEL'
pwd  = 'WEB123'
host = '192.168.1.212'
service = 'AP10'

class Oracle(object):
    def __init__(self, user=user, passwd=pwd, host=host, service=service, *args, **kwargs):
        super(Oracle, self).__init__(*args, **kwargs)
        args = {'user':user, 'passwd': passwd, 'host': host, 'service': service}
        connstring = '{user}/{passwd}@{host}/{service}'.format(**args)
        self.con    = cx_Oracle.connect(connstring)

    def query(self, querystring):
        cursor = cx_Oracle.Cursor(self.con)
        cursor.execute(querystring)
        return cursor

    def fetchOne(self, querystring):
        cursor = self.query(querystring)
        return cursor.fetchone()
