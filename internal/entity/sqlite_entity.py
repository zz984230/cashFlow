class SqliteDb(object):
    def __init__(self, db_name, conn_timeout):
        self.db_name = db_name
        self.conn_timeout = conn_timeout

    @property
    def db_name(self):
        return self.db_name

    @db_name.setter
    def db_name(self, db_name):
        self.db_name = db_name

    @property
    def conn_timeout(self):
        return self.conn_timeout

    @conn_timeout.setter
    def conn_timeout(self, conn_timeout):
        self.conn_timeout = conn_timeout
