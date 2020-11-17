from .mysql_rep import MysqlRep


class PaymentRep(MysqlRep):
    def __init__(self, cli, db_cfg):
        self.__cli = cli
        self.__table = db_cfg.table_payment
        self.__fields = ["itemId", "money"]
        self.__primary_key = "itemId"

        super().__init__(self.__table, self.__fields, self.__primary_key, cli)


