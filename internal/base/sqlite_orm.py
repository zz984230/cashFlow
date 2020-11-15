import sqlite3


class SqliteConn(object):
    def __init__(self, cfg):
        self.__db = cfg["db"]
        self.__timeout = cfg["conn_timeout"]
        self.__conn = None

    def connect(self):
        self.__conn = sqlite3.connect(self.__db, self.__timeout)

    def commit(self):
        self.__conn.commit()

    def close(self):
        self.__conn.close()


class SqliteClient(object):
    def __init__(self, conn):
        self.__conn = conn
        self.__cursor = self.__conn.cursor()

    def insert(self, table, fields: list, data: list):
        field_str = ",".join(fields)
        data_str = ""
        for d in data:
            if data_str != "":
                data_str = "%s," % data_str

            data_str = "%s(%s)" % (data_str, ",".join(['"%s"' % d1 for d1 in d]))

        sql = "INSERT INTO %s (%s) VALUES %s" % (table, field_str, data_str)
        self.__cursor.execute(sql)
        self.__conn.commit()

    def truncate(self, table):
        sql = "TRUNCATE %s" % table
        self.__cursor.execute(sql)
        self.__conn.commit()

    def delete_by_key(self, table, primary_key, primary_key_values: list):
        sql = "DELETE FROM %s WHERE %s IN (%s)" % (table, primary_key, ",".join(primary_key_values))
        self.__cursor.execute(sql)
        self.__conn.commit()

    def select_all(self, table, fields: str):
        sql = "SELECT %s FROM %s" % (fields, table)
        self.__cursor.execute(sql)
        self.__conn.commit()

    def select_by_key(self, table, fields: str, conditions: dict):
        c = ""
        for k, v in conditions:
            if c != "":
                c = "%s AND" % c

            c = "%s %s=\"%s\"" % (c, k, v)

        sql = "SELECT %s FROM %s WHERE %s" % (fields, table, c)
        self.__cursor.execute(sql)
        self.__conn.commit()
