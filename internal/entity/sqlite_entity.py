class SqliteDb(object):
    def __init__(self,
                 db,
                 conn_timeout,
                 table_debts,
                 table_income,
                 table_income_payment_flow,
                 table_investment_flow,
                 table_investment_info,
                 table_item_info,
                 table_payment,
                 table_property):
        self.__db = db
        self.__conn_timeout = conn_timeout
        self.__table_debts = table_debts
        self.__table_income = table_income
        self.__table_income_payment_flow = table_income_payment_flow
        self.__table_investment_flow = table_investment_flow
        self.__table_investment_info = table_investment_info
        self.__table_item_info = table_item_info
        self.__table_payment = table_payment
        self.__table_property = table_property

    @property
    def db(self):
        return self.__db

    @property
    def conn_timeout(self):
        return self.__conn_timeout

    @property
    def table_debts(self):
        return self.__table_debts

    @property
    def table_income(self):
        return self.__table_income

    @property
    def table_income_payment_flow(self):
        return self.__table_income_payment_flow

    @property
    def table_investment_flow(self):
        return self.__table_investment_flow

    @property
    def table_investment_info(self):
        return self.__table_investment_info

    @property
    def table_item_info(self):
        return self.__table_item_info

    @property
    def table_payment(self):
        return self.__table_payment

    @property
    def table_property(self):
        return self.__table_property
