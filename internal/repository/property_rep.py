from .mysql_rep import MysqlRep


class PropertyRep(MysqlRep):
    def __init__(self, cli, db_cfg):
        self.__cli = cli
        self.__table = db_cfg.table_property
        self.__fields = ["itemId", "money"]
        self.__primary_key = "itemId"

        super().__init__(self.__table, self.__fields, self.__primary_key, cli)


