import pymysql.cursors

class DBase(object):
    config = {
        'host': 'localhost', 
        'user': 'root',
        'password': 'Muh4mm3t',
        'db': 'flask_blog',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    def __init__(self):
        self.conn = pymysql.connect(*self.config)
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self

    def query(self, query, params=None):
        try:
            result = self.cur.execute(query, params)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            self.cur.close()