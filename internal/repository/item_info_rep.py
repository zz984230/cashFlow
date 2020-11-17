from .mysql_rep import MysqlRep


class ItemInfoRep(MysqlRep):
    def __init__(self, cli, db_cfg):
        self.__cli = cli
        self.__table = db_cfg.table_item_info
        self.__fields = ["itemId", "itemName", "type"]
        self.__primary_key = "itemId"

        super().__init__(self.__table, self.__fields, self.__primary_key, cli)


