from .mysql_rep import MysqlRep


class IncomePaymentFlowRep(MysqlRep):
    def __init__(self, cli, db_cfg):
        self.__cli = cli
        self.__table = db_cfg.table_income_payment_flow
        self.__fields = ["date", "itemId", "income", "payment", "propertyTransfer", "remark"]
        self.__primary_key = "itemId"

        super().__init__(self.__table, self.__fields, self.__primary_key, cli)


