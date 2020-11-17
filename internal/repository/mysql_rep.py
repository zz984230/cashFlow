class MysqlRep(object):
    def __init__(self, table, fields, primary_key, cli):
        self.__table = table
        self.__fields = fields
        self.__primary_key = primary_key
        self.__cli = cli

    def insert(self, data: list):
        self.__cli.insert(self.__table, self.__fields, data)

    def truncate(self):
        self.__cli.truncate(self.__table)

    def delete_by_key(self, data: list):
        self.__cli.delete_by_key(self.__table, self.__primary_key, data)

    def select_all(self):
        self.__cli.select_all(self.__table, self.__fields)

    def select_by_key(self, fields: list, conditions: dict):
        self.__cli.select_by_key(self.__table, fields, conditions)
